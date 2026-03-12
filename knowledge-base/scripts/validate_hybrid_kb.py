#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

NUMBERED_FLAT_REQUIRED = [
    "knowledge-base/00-master.md",
    "knowledge-base/01-business-flows.md",
    "knowledge-base/02-architecture.md",
    "knowledge-base/03-risk-model.md",
    "knowledge-base/04-active-sprint.md",
    "knowledge-base/.kb-config.yml",
]
NUMBERED_TREE_REQUIRED = [
    "knowledge-base/00-master.md",
    "knowledge-base/01-business-flows/00-index.md",
    "knowledge-base/02-architecture/00-index.md",
    "knowledge-base/03-risk-model/00-index.md",
    "knowledge-base/04-active-sprint/00-index.md",
    "knowledge-base/.kb-config.yml",
]
LEGACY_FLAT_REQUIRED = [
    "knowledge-base/00-index.md",
    "knowledge-base/architecture.md",
    "knowledge-base/business-flows.md",
    "knowledge-base/active-sprint.md",
    "knowledge-base/risks.md",
    "knowledge-base/.kb-config.yml",
]
TIER1_CANONICAL_FILES = [
    "knowledge-base/00-master.md",
    "knowledge-base/01-business-flows.md",
    "knowledge-base/02-architecture.md",
    "knowledge-base/03-risk-model.md",
    "knowledge-base/04-active-sprint.md",
]
OPTIONAL_BY_KEY = {
    "decision-log": "knowledge-base/advanced/decision-log.md",
    "incident-log": "knowledge-base/advanced/incident-log.md",
    "feature-history": "knowledge-base/advanced/feature-history.md",
    "integration-map": "knowledge-base/advanced/integration-map.md",
    "metrics": "knowledge-base/advanced/metrics.md",
    "known-constraints": "knowledge-base/advanced/known-constraints.md",
}
ENTRY_REFS_BY_LAYOUT = {
    "numbered-flat": [
        "01-business-flows.md",
        "02-architecture.md",
        "03-risk-model.md",
        "04-active-sprint.md",
    ],
    "numbered-tree": [
        "01-business-flows/00-index.md",
        "02-architecture/00-index.md",
        "03-risk-model/00-index.md",
        "04-active-sprint/00-index.md",
    ],
    "legacy-flat": [
        "architecture.md",
        "business-flows.md",
        "active-sprint.md",
        "risks.md",
    ],
}
REQUIRED_TIER1_HEADINGS = [
    "Purpose",
    "Scope",
    "What is true today",
    "Key rules",
    "Known gaps / uncertainty",
    "Linked evidence",
    "Next review trigger",
]
FRONT_MATTER_FIELDS = [
    "id",
    "title",
    "owners",
    "audiences",
    "last_reviewed",
    "review_cycle_days",
    "confidence",
    "change_frequency",
    "source_refs",
    "tags",
]
TIER1_MAX_LINES = {
    "knowledge-base/00-master.md": 180,
    "knowledge-base/01-business-flows.md": 240,
    "knowledge-base/02-architecture.md": 240,
    "knowledge-base/03-risk-model.md": 220,
    "knowledge-base/04-active-sprint.md": 260,
}
APPEND_ONLY_LOGS = {
    "knowledge-base/advanced/decision-log.md",
    "knowledge-base/advanced/incident-log.md",
    "knowledge-base/advanced/feature-history.md",
}
SECTION_HEADING_PATTERN = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
ENTRY_HEADING_PATTERN = re.compile(r"^###\s+(.+?)\s*$", re.MULTILINE)
ISO_DATE_PREFIX_PATTERN = re.compile(r"^(?P<date>\d{4}-\d{2}-\d{2}):")


def strip_quotes(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_top_level_yaml(lines: list[str]) -> dict[str, object]:
    parsed: dict[str, object] = {}
    current_list_key: str | None = None
    for raw in lines:
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if raw.startswith("  - ") and current_list_key:
            value = strip_quotes(raw.strip()[2:].strip())
            existing = parsed.setdefault(current_list_key, [])
            if isinstance(existing, list):
                existing.append(value)
            continue
        if raw.startswith(" "):
            current_list_key = None
            continue
        if ":" not in raw:
            current_list_key = None
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            parsed[key] = []
            current_list_key = key
        elif value == "[]":
            parsed[key] = []
            current_list_key = None
        elif value.startswith("[") and value.endswith("]"):
            items = [strip_quotes(item.strip()) for item in value[1:-1].split(",") if item.strip()]
            parsed[key] = items
            current_list_key = None
        else:
            parsed[key] = strip_quotes(value)
            current_list_key = None
    return parsed


def split_front_matter(text: str) -> tuple[dict[str, object] | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    front_matter_lines = text[4:end].splitlines()
    body = text[end + 5 :]
    return parse_top_level_yaml(front_matter_lines), body


def get_block_lines(lines: list[str], key: str) -> list[str]:
    block: list[str] = []
    in_block = False
    prefix = f"{key}:"
    for raw in lines:
        if not in_block:
            if raw.startswith(prefix):
                in_block = True
            continue
        if raw.strip() and not raw.startswith(" "):
            break
        block.append(raw)
    return block


def read_enabled_tier2(config_path: Path) -> list[str]:
    lines = read_text(config_path).splitlines()
    enabled: list[str] = []
    for raw in get_block_lines(lines, "enabled_tier2"):
        stripped = raw.strip()
        if stripped.startswith("- "):
            enabled.append(stripped[2:].strip())
    return enabled


def read_loading_default_refs(config_path: Path) -> list[str]:
    lines = read_text(config_path).splitlines()
    refs: list[str] = []
    for raw in get_block_lines(lines, "loading_defaults"):
        stripped = raw.strip()
        if stripped.startswith("- "):
            refs.append(stripped[2:].strip())
    return refs


def read_loading_default_groups(config_path: Path) -> set[str]:
    lines = read_text(config_path).splitlines()
    groups: set[str] = set()
    for raw in get_block_lines(lines, "loading_defaults"):
        stripped = raw.strip()
        if stripped.endswith(":") and not stripped.startswith("- "):
            groups.add(stripped[:-1])
    return groups


def read_owner_identifiers(config_path: Path) -> set[str]:
    lines = read_text(config_path).splitlines()
    identifiers: set[str] = set()
    for raw in get_block_lines(lines, "owners"):
        stripped = raw.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        identifiers.add(key.strip())
        scalar = strip_quotes(value.strip())
        if scalar:
            identifiers.add(scalar)
    return identifiers


def has_required_config_keys(config_path: Path, errors: list[str]) -> None:
    text = read_text(config_path)
    if not re.search(r"(?m)^version:\s*", text):
        errors.append("missing config key: version")
    if not re.search(r"(?m)^enabled_tier2:\s*", text):
        errors.append("missing config key: enabled_tier2")
    if not re.search(r"(?m)^loading_defaults:\s*", text):
        errors.append("missing config key: loading_defaults")

    project_lines = get_block_lines(text.splitlines(), "project")
    has_project_name = any(line.strip().startswith("name:") for line in project_lines)
    if not has_project_name:
        errors.append("missing config key: project.name")


def detect_layout(root: Path) -> str | None:
    if (root / "knowledge-base/01-business-flows.md").exists():
        return "numbered-flat"
    if (root / "knowledge-base/01-business-flows/00-index.md").exists():
        return "numbered-tree"
    if (root / "knowledge-base/00-index.md").exists():
        return "legacy-flat"
    return None


def validate_required(root: Path, required: list[str], errors: list[str]) -> None:
    for rel in required:
        if not (root / rel).exists():
            errors.append(f"missing required file: {rel}")


def validate_entry(entry: Path, refs: list[str], errors: list[str]) -> None:
    if not entry.exists():
        return
    entry_text = read_text(entry)
    for ref in refs:
        if ref not in entry_text:
            errors.append(f"entry file does not reference: {ref}")


def validate_front_matter(
    path: Path,
    owner_identifiers: set[str],
    errors: list[str],
    warnings: list[str],
    strict_freshness: bool,
) -> dict[str, object] | None:
    front_matter, body = split_front_matter(read_text(path))
    rel = path.as_posix().split("/knowledge-base/", 1)[-1]
    rel = f"knowledge-base/{rel}"

    if front_matter is None:
        errors.append(f"missing front matter: {rel}")
        return None

    for field in FRONT_MATTER_FIELDS:
        if field not in front_matter:
            errors.append(f"missing front matter field in {rel}: {field}")

    owners = front_matter.get("owners", [])
    if isinstance(owners, str):
        owners = [owners]
    if not isinstance(owners, list) or not owners:
        errors.append(f"front matter owners must be a non-empty list in {rel}")
    elif owner_identifiers:
        for owner in owners:
            if owner not in owner_identifiers:
                warnings.append(f"owner reference not found in .kb-config.yml for {rel}: {owner}")

    audiences = front_matter.get("audiences", [])
    if isinstance(audiences, str):
        audiences = [audiences]
    if not isinstance(audiences, list) or not audiences:
        errors.append(f"front matter audiences must be a non-empty list in {rel}")

    last_reviewed = str(front_matter.get("last_reviewed", "")).strip()
    cycle_raw = str(front_matter.get("review_cycle_days", "")).strip()
    if "{{" in last_reviewed or not last_reviewed:
        warnings.append(f"last_reviewed is still a placeholder or missing in {rel}")
    else:
        try:
            reviewed_on = date.fromisoformat(last_reviewed)
            review_cycle_days = int(cycle_raw)
            age_days = (date.today() - reviewed_on).days
            if age_days > review_cycle_days:
                message = f"stale last_reviewed in {rel}: {last_reviewed} is {age_days} days old"
                if strict_freshness:
                    errors.append(message)
                else:
                    warnings.append(message)
        except ValueError:
            warnings.append(f"could not parse freshness metadata in {rel}")

    if body.strip() == "":
        warnings.append(f"file body is empty after front matter: {rel}")
    return front_matter


def validate_tier1_headings(path: Path, errors: list[str]) -> None:
    _, body = split_front_matter(read_text(path))
    headings = SECTION_HEADING_PATTERN.findall(body)
    normalized = [heading.strip().lower() for heading in headings]
    last_index = -1
    for required in REQUIRED_TIER1_HEADINGS:
        try:
            current_index = normalized.index(required.lower())
        except ValueError:
            rel = path.as_posix().split("/knowledge-base/", 1)[-1]
            errors.append(f"missing required heading in knowledge-base/{rel}: {required}")
            continue
        if current_index < last_index:
            rel = path.as_posix().split("/knowledge-base/", 1)[-1]
            errors.append(f"required headings out of order in knowledge-base/{rel}: {required}")
            return
        last_index = current_index


def validate_tier1_size(path: Path, warnings: list[str]) -> None:
    _, body = split_front_matter(read_text(path))
    non_empty_lines = [line for line in body.splitlines() if line.strip()]
    rel = path.as_posix().split("/knowledge-base/", 1)[-1]
    rel = f"knowledge-base/{rel}"
    if len(non_empty_lines) < 12:
        warnings.append(f"{rel} looks undersized; confirm it has enough project truth to be useful")
    max_lines = TIER1_MAX_LINES.get(rel)
    if max_lines and len(non_empty_lines) > max_lines:
        warnings.append(f"{rel} exceeds the recommended Tier 1 size budget ({len(non_empty_lines)} > {max_lines})")


def collect_canonical_claims(path: Path) -> list[str]:
    _, body = split_front_matter(read_text(path))
    claims: list[str] = []
    capture = False
    for raw in body.splitlines():
        stripped = raw.strip()
        if stripped.lower() == "## what is true today":
            capture = True
            continue
        if capture and stripped.startswith("## "):
            break
        if not capture or not stripped.startswith("- "):
            continue
        if "{{" in stripped or stripped.lower().startswith("- example:"):
            continue
        normalized = " ".join(stripped[2:].split())
        if len(normalized) >= 30:
            claims.append(normalized)
    return claims


def validate_append_only_log(path: Path, errors: list[str], warnings: list[str]) -> None:
    _, body = split_front_matter(read_text(path))
    rel = path.as_posix().split("/knowledge-base/", 1)[-1]
    rel = f"knowledge-base/{rel}"
    entry_titles = ENTRY_HEADING_PATTERN.findall(body)
    if not entry_titles:
        errors.append(f"append-only log has no entries or entry template headings: {rel}")
        return

    parsed_dates: list[date] = []
    for title in entry_titles:
        if title.startswith("{{DATE}}:"):
            continue
        match = ISO_DATE_PREFIX_PATTERN.match(title)
        if not match:
            warnings.append(f"append-only log entry heading should start with YYYY-MM-DD in {rel}: {title}")
            continue
        try:
            parsed_dates.append(date.fromisoformat(match.group("date")))
        except ValueError:
            warnings.append(f"append-only log entry has an invalid date in {rel}: {title}")
    if parsed_dates != sorted(parsed_dates, reverse=True):
        warnings.append(f"append-only log entries are not newest-first in {rel}")


def validate_config(
    root: Path,
    layout: str,
    errors: list[str],
    warnings: list[str],
) -> tuple[list[str], set[str]]:
    config_path = root / "knowledge-base/.kb-config.yml"
    if not config_path.exists():
        return [], set()

    has_required_config_keys(config_path, errors)
    enabled = read_enabled_tier2(config_path)
    owner_identifiers = read_owner_identifiers(config_path)

    if not owner_identifiers:
        warnings.append("no owners block found in knowledge-base/.kb-config.yml; owner-link validation will be limited")

    for module in enabled:
        rel = OPTIONAL_BY_KEY.get(module)
        if rel is None:
            errors.append(f"unknown enabled Tier 2 module in config: {module}")
        elif not (root / rel).exists():
            errors.append(f"enabled Tier 2 file missing: {rel}")

    loading_groups = read_loading_default_groups(config_path)
    for group in ["code_review", "planning", "sprint_work", "onboarding", "incident_response"]:
        if group not in loading_groups:
            warnings.append(f"missing recommended loading_defaults group: {group}")

    if layout == "numbered-flat":
        for ref in read_loading_default_refs(config_path):
            target = root / "knowledge-base" / ref
            if not target.exists():
                errors.append(f"loading_defaults references a missing file: knowledge-base/{ref}")

    for module, rel in OPTIONAL_BY_KEY.items():
        if (root / rel).exists() and module not in enabled:
            warnings.append(f"optional KB file exists but is not enabled in config: {rel}")

    return enabled, owner_identifiers


def validate_canonical_layout(
    root: Path,
    owner_identifiers: set[str],
    errors: list[str],
    warnings: list[str],
    strict_freshness: bool,
) -> None:
    duplicate_claims: dict[str, set[str]] = defaultdict(set)

    for rel in TIER1_CANONICAL_FILES:
        path = root / rel
        validate_front_matter(path, owner_identifiers, errors, warnings, strict_freshness)
        validate_tier1_headings(path, errors)
        validate_tier1_size(path, warnings)
        for claim in collect_canonical_claims(path):
            duplicate_claims[claim].add(rel)

    for claim, files in duplicate_claims.items():
        if len(files) > 1:
            joined_files = ", ".join(sorted(files))
            warnings.append(f"possible duplicate canonical claim across Tier 1 files ({joined_files}): {claim}")

    for rel in OPTIONAL_BY_KEY.values():
        path = root / rel
        if not path.exists():
            continue
        validate_front_matter(path, owner_identifiers, errors, warnings, strict_freshness)
        if rel in APPEND_ONLY_LOGS:
            validate_append_only_log(path, errors, warnings)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a hybrid KB installation")
    parser.add_argument("project_root", nargs="?", default=".", help="Path to the target project root")
    parser.add_argument(
        "--strict-freshness",
        action="store_true",
        help="Treat stale last_reviewed metadata as a validation error instead of a warning",
    )
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    errors: list[str] = []
    warnings: list[str] = []
    layout = detect_layout(root)

    if layout == "numbered-flat":
        validate_required(root, NUMBERED_FLAT_REQUIRED, errors)
        validate_entry(root / "knowledge-base/00-master.md", ENTRY_REFS_BY_LAYOUT[layout], errors)
    elif layout == "numbered-tree":
        validate_required(root, NUMBERED_TREE_REQUIRED, errors)
        validate_entry(root / "knowledge-base/00-master.md", ENTRY_REFS_BY_LAYOUT[layout], errors)
        warnings.append("deep Tier 1 schema validation is skipped for numbered-tree compatibility installs")
    elif layout == "legacy-flat":
        validate_required(root, LEGACY_FLAT_REQUIRED, errors)
        validate_entry(root / "knowledge-base/00-index.md", ENTRY_REFS_BY_LAYOUT[layout], errors)
        warnings.append("deep Tier 1 schema validation is skipped for legacy-flat compatibility installs")
    else:
        errors.append(
            "knowledge base entry file not found: expected knowledge-base/00-master.md or knowledge-base/00-index.md"
        )

    enabled_tier2, owner_identifiers = validate_config(root, layout or "", errors, warnings)

    if layout == "numbered-flat" and not errors:
        validate_canonical_layout(
            root,
            owner_identifiers,
            errors,
            warnings,
            args.strict_freshness,
        )

    if errors:
        print("Hybrid KB validation failed:")
        for error in errors:
            print(f"- {error}")
        if warnings:
            print("\nWarnings:")
            for warning in warnings:
                print(f"- {warning}")
        return 1

    if warnings:
        print(f"Hybrid KB validation passed ({layout} layout) with {len(warnings)} warning(s):")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print(f"Hybrid KB validation passed ({layout} layout).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
