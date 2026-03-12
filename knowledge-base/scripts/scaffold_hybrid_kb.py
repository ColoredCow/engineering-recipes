#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = ROOT / "knowledge-base" / "templates"
SCRIPT_ROOT = ROOT / "knowledge-base" / "scripts"
PROJECT_FILES_ROOT = ROOT / "knowledge-base" / "project-files"
KB_MANAGER_AGENT = ROOT / "claude" / "agents" / "knowledge-base-manager" / "knowledge-base-manager.md"
CORE_FILES = [
    "00-master.md",
    "01-business-flows.md",
    "02-architecture.md",
    "03-risk-model.md",
    "04-active-sprint.md",
    ".kb-config.yml",
]
ADVANCED_MAP = {
    "decision-log": "advanced/decision-log.md",
    "incident-log": "advanced/incident-log.md",
    "feature-history": "advanced/feature-history.md",
    "integration-map": "advanced/integration-map.md",
    "metrics": "advanced/metrics.md",
    "known-constraints": "advanced/known-constraints.md",
}
OPTIONAL_PROJECT_FILES = {
    "kb_process": (PROJECT_FILES_ROOT / "KB-PROCESS.md", Path("docs/kb-process.md")),
}
CLAUDE_SECTION = TEMPLATES / "CLAUDE.section.md"
SUPPORT_SCRIPTS = [
    "validate_hybrid_kb.py",
]
KB_MANAGER_DESCRIPTION = (
    "- `knowledge-base-manager`: When the user wants to sync the KB from issue or sprint activity, "
    "or update KB sections with the designated write-enabled flow."
)


def copy_file(src: Path, dest: Path, overwrite: bool) -> str:
    if dest.exists() and not overwrite:
        return f"skip {dest}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return f"write {dest}"


def replace_tokens(path: Path, replacements: dict[str, str]) -> None:
    text = path.read_text(encoding="utf-8")
    updated = text
    for old, new in replacements.items():
        updated = updated.replace(old, new)
    if updated != text:
        path.write_text(updated, encoding="utf-8")


def append_section(lines: list[str], heading: str, content: list[str]) -> list[str]:
    if any(line.strip() == heading for line in lines):
        return lines
    if lines and lines[-1].strip():
        lines.append("")
    return lines + content


def append_to_section(lines: list[str], heading: str, content: list[str]) -> list[str]:
    start = None
    for index, line in enumerate(lines):
        if line.strip() == heading:
            start = index
            break
    if start is None:
        return append_section(lines, heading, [heading, ""] + content)

    end = len(lines)
    for index in range(start + 1, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break

    insertion = content[:]
    if end > start + 1 and lines[end - 1].strip():
        insertion = [""] + insertion
    return lines[:end] + insertion + lines[end:]


def section_contains(lines: list[str], heading: str, needle: str) -> bool:
    start = None
    for index, line in enumerate(lines):
        if line.strip() == heading:
            start = index
            break
    if start is None:
        return False

    end = len(lines)
    for index in range(start + 1, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break
    return needle in "\n".join(lines[start:end])


def ensure_claude_guidance(project_root: Path, install_kb_manager: bool) -> list[str]:
    claude_path = project_root / "CLAUDE.md"
    existing_lines = claude_path.read_text(encoding="utf-8").splitlines() if claude_path.exists() else []
    actions: list[str] = []

    kb_section = CLAUDE_SECTION.read_text(encoding="utf-8").rstrip().splitlines()
    updated_lines = append_section(existing_lines[:], "## Knowledge Base", kb_section)
    if updated_lines != existing_lines:
        actions.append(f"update {claude_path}")
    else:
        actions.append(f"skip {claude_path}")

    if install_kb_manager:
        if not section_contains(updated_lines, "## Custom Agents", "`knowledge-base-manager`"):
            updated_lines = append_to_section(updated_lines, "## Custom Agents", [KB_MANAGER_DESCRIPTION])
            actions[-1] = f"update {claude_path}"

    claude_path.write_text("\n".join(updated_lines).rstrip() + "\n", encoding="utf-8")
    return actions


def configure_kb_config(config_path: Path, enabled: list[str]) -> str:
    lines = config_path.read_text(encoding="utf-8").splitlines()
    new_lines: list[str] = []
    in_enabled = False
    in_incident = False
    for line in lines:
        stripped = line.strip()
        if stripped == "enabled_tier2:":
            in_enabled = True
            new_lines.append("enabled_tier2:")
            if enabled:
                for module in enabled:
                    new_lines.append(f"  - {module}")
            else:
                new_lines.append("  # Add optional module keys here when enabled for the project.")
            continue
        if in_enabled:
            if stripped.startswith("-") or stripped.startswith("#"):
                continue
            if stripped and not line.startswith(" "):
                in_enabled = False
            else:
                continue

        if stripped == "incident_response:" and line.startswith("  "):
            in_incident = True
            new_lines.append(line)
            new_lines.append("    - 03-risk-model.md")
            if "incident-log" in enabled:
                new_lines.append("    - advanced/incident-log.md")
            else:
                new_lines.append("    # Add advanced/incident-log.md when incident-log is enabled.")
            continue
        if in_incident:
            if stripped.startswith("-") or stripped.startswith("#"):
                continue
            if stripped and not line.startswith("    "):
                in_incident = False
            else:
                continue

        new_lines.append(line)

    config_path.write_text("\n".join(new_lines).rstrip() + "\n", encoding="utf-8")
    return f"configure {config_path}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold the hybrid knowledge base into a target project")
    parser.add_argument("project_root", help="Path to the target project root")
    parser.add_argument(
        "--enable",
        default="",
        help="Comma-separated Tier 2 modules to enable (decision-log,incident-log,feature-history,integration-map,metrics,known-constraints)",
    )
    parser.add_argument("--install-kb-manager", action="store_true", help="Install the write-enabled KB manager agent")
    parser.add_argument("--install-kb-process", action="store_true", help="Install the KB working-agreement doc")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    if not project_root.exists():
        print(f"error: project root not found: {project_root}", file=sys.stderr)
        return 1

    kb_root = project_root / "knowledge-base"
    (kb_root / "advanced").mkdir(parents=True, exist_ok=True)
    (kb_root / "scripts").mkdir(parents=True, exist_ok=True)

    enabled = [item.strip() for item in args.enable.split(",") if item.strip()]
    unknown = [item for item in enabled if item not in ADVANCED_MAP]
    if unknown:
        print(f"error: unknown Tier 2 modules: {', '.join(unknown)}", file=sys.stderr)
        return 1

    token_replacements = {
        "{{LAST_REVIEWED_DATE}}": date.today().isoformat(),
    }
    actions: list[str] = []
    for rel in CORE_FILES:
        destination = kb_root / rel
        actions.append(copy_file(TEMPLATES / rel, destination, args.overwrite))
        if destination.suffix == ".md" and actions[-1].startswith("write "):
            replace_tokens(destination, token_replacements)

    for module in enabled:
        rel = ADVANCED_MAP[module]
        destination = kb_root / rel
        actions.append(copy_file(TEMPLATES / rel, destination, args.overwrite))
        if actions[-1].startswith("write "):
            replace_tokens(destination, token_replacements)

    for script_name in SUPPORT_SCRIPTS:
        actions.append(copy_file(SCRIPT_ROOT / script_name, kb_root / "scripts" / script_name, args.overwrite))

    if args.install_kb_manager:
        actions.append(
            copy_file(KB_MANAGER_AGENT, project_root / ".claude" / "agents" / "knowledge-base-manager.md", args.overwrite)
        )

    if args.install_kb_process:
        src, dest = OPTIONAL_PROJECT_FILES["kb_process"]
        actions.append(copy_file(src, project_root / dest, args.overwrite))

    actions.append(configure_kb_config(kb_root / ".kb-config.yml", enabled))
    actions.extend(ensure_claude_guidance(project_root, args.install_kb_manager))

    print("Hybrid KB scaffold summary:")
    for action in actions:
        print(f"- {action}")
    print(f"- enabled Tier 2: {', '.join(enabled) if enabled else 'none'}")
    print(f"- KB manager installed: {'yes' if args.install_kb_manager else 'no'}")
    print(f"- KB process doc installed: {'yes' if args.install_kb_process else 'no'}")
    print("- validate from the project root with: python3 knowledge-base/scripts/validate_hybrid_kb.py .")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
