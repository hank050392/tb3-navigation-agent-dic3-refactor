# Offline Contract

## Purpose

Describe the repository's existing offline JSON demonstration so readers can distinguish implemented validation and mock outcomes from the proposed language interface and physical navigation capabilities.

## Requirements

### Requirement: Validate structured requests
The offline demo SHALL accept only the exact fields for navigate, cancel, clarify and reject; navigation targets SHALL belong to the supplied landmark registry.

#### Scenario: Unknown target or extra coordinate
- **WHEN** a request contains an unknown landmark or an extra coordinate field
- **THEN** the demo returns REJECTED with goal_sent false

### Requirement: Block mock dispatch when unavailable
The demo SHALL return BUSY, NOT_READY or NO_PATH for the corresponding busy, stale or blocked scenario without entering the mock dispatch branch.

#### Scenario: Stale input
- **WHEN** a valid navigate request is evaluated with the stale scenario
- **THEN** the response is NOT_READY and goal_sent is false

### Requirement: Identify mock outcomes
The demo SHALL label every output demo_only true and navigation_backend mock, and SHALL distinguish mock ARRIVED, FAILED and TIMEOUT outcomes.

#### Scenario: Ready scenario
- **WHEN** a valid navigate request is evaluated with the ready scenario
- **THEN** the output contains ARRIVED, goal_sent true and explicit mock provenance, without implying physical motion

### Requirement: Avoid claiming physical stop
The demo SHALL mark cancellation stop_confirmed false because it has no access to physical robot observations.

#### Scenario: Cancel during mock busy state
- **WHEN** a valid cancel request is evaluated with the busy scenario
- **THEN** the output is mock CANCELED with stop_confirmed false and goal_sent false
