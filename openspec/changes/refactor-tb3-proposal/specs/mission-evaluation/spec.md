# Mission Evaluation Delta

## Purpose

Define a reproducible evaluation contract that separates language understanding, dispatch decisions, navigation outcomes and reporting quality, with explicit provenance for offline, simulated and physical observations.

## ADDED Requirements

### Requirement: Freeze data and comparison conditions
Evaluation SHALL separate the 60 planned Chinese commands into 20 development and 40 locked test commands by semantic template, and SHALL record model, prompt, registry, map and navigation configuration versions.

#### Scenario: Paraphrased duplicate
- **WHEN** two commands differ only by destination name within the same semantic template
- **THEN** both are assigned to the same split to avoid template leakage

### Requirement: Compare task interfaces fairly
Evaluation SHALL compare B0 destination menu, B1 direct language-to-goal and B2 full Agent under shared navigation and stopping settings, and SHALL compare language-processing correctness only for B1 and B2.

#### Scenario: B0 has no language input
- **WHEN** language-processing accuracy is reported
- **THEN** B0 is marked not applicable and its menu selections are not counted as correct language parsing

### Requirement: Report failures and denominators
Evaluation SHALL retain all failed, canceled, rejected and timed-out runs; report handling correctness, inappropriate dispatch, mission completion, report consistency and latency with explicit denominators; and distinguish correct non-dispatch from successful arrival.

#### Scenario: Correct rejection
- **WHEN** an unreachable task is correctly refused
- **THEN** it can count toward handling correctness but cannot count as an arrival

### Requirement: Distinguish observation sources
Every evaluation record SHALL identify mock, simulation or physical provenance. Unit-test results SHALL NOT be presented as language accuracy, navigation success or physical robot performance.

#### Scenario: Offline demonstration succeeds
- **WHEN** the ready mock scenario returns ARRIVED
- **THEN** the run remains an offline logic demonstration and is excluded from navigation success claims

### Requirement: Report statistical uncertainty
Binary outcome summaries SHALL include sample counts and Wilson 95 percent intervals; latency summaries SHALL include median and p95 with the measurement boundary and quantile convention.

#### Scenario: No observed collision
- **WHEN** the physical trials record no collision
- **THEN** the report states the sample count and uncertainty instead of claiming zero collision risk
