---
id: kb.metrics
title: Metrics
owners:
  - metrics
audiences:
  - engineering
  - product
  - qa
last_reviewed: "{{LAST_REVIEWED_DATE}}"
review_cycle_days: 90
confidence: medium
change_frequency: low
source_refs: []
tags:
  - tier2
  - metrics
---

# Metrics: {{PROJECT_NAME}}

## Purpose

Capture a small set of baseline product or operational metrics so teams and agents understand normal operating context before reacting to change.

## Scope

Keep only metrics that materially affect prioritization, delivery risk, or support expectations.

## Update rules

- Prefer a few stable metrics over a long dashboard export.
- Record the current baseline, directional trend, and any caveats.
- Link the source report or dashboard in `source_refs` when possible.

## Metric table

| Metric | Baseline | Trend | Notes |
|---|---|---|---|
| {{METRIC_1}} | {{BASELINE_1}} | {{TREND_1}} | {{NOTES_1}} |
| {{METRIC_2}} | {{BASELINE_2}} | {{TREND_2}} | {{NOTES_2}} |

## Example

| Metric | Baseline | Trend | Notes |
|---|---|---|---|
| Weekly learner submissions | 2,400 | rising | Peaks after partner training days |
