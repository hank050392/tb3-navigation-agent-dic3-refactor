# Navigation Mission Delta

## Purpose

Define the proposed user-visible contract for a single indoor robot mission, from Chinese destination requests through validated dispatch, monitored execution, cancellation and evidence-based terminal reporting.

## ADDED Requirements

### Requirement: Clarify ambiguous destinations
The system SHALL ask the user to choose among registered candidates when a destination is ambiguous and SHALL NOT dispatch until the ambiguity is resolved.

#### Scenario: Two entrances
- **WHEN** the user requests 「去門口」 and two registry entries match
- **THEN** the system returns CLARIFY with the candidates and sends no navigation goal

#### Scenario: Clarification answer
- **WHEN** the user selects one offered destination for the pending request
- **THEN** the system validates that destination and reruns all pre-dispatch checks before dispatch

### Requirement: Constrain intent and destination
The system SHALL accept only supported intents and registered destination IDs through a validated schema; it SHALL reject unknown destinations, arbitrary coordinates, unknown tools and extra fields without dispatch.

#### Scenario: Unsupported destination
- **WHEN** a parsed request identifies a destination absent from the current registry
- **THEN** the system returns REJECTED with the reason and sends no goal

#### Scenario: Model proposes coordinates
- **WHEN** model output adds x and y to a navigate request
- **THEN** schema validation rejects that request and no navigation goal is sent

### Requirement: Handle parsing failure explicitly
The system SHALL report clarification or an explicit error when parsing fails, exceeds its configured deadline or returns malformed output, without guessing a destination.

#### Scenario: Model timeout
- **WHEN** the language service exceeds the configured request deadline
- **THEN** the user receives a parsing error and no goal is sent

### Requirement: Permit one active mission
The system SHALL allow at most one active movement mission, give cancellation priority, and block new movement while a previous goal has no confirmed terminal result.

#### Scenario: New destination while busy
- **WHEN** a new navigate request arrives during an active mission
- **THEN** the system returns BUSY without replacing or duplicating the goal

### Requirement: Require current state and valid path
The system SHALL dispatch only when localization, TF, scan freshness, navigation readiness and a path to the registered destination satisfy the configured checks on the active map.

#### Scenario: Stale state
- **WHEN** scan or localization age exceeds its configured threshold or TF is unavailable
- **THEN** the system returns NOT_READY with observed reasons and sends no goal

#### Scenario: No valid path
- **WHEN** the path check returns no valid path or exceeds its deadline
- **THEN** the system returns NO_PATH with a distinct no-path or check-timeout reason and sends no goal

#### Scenario: Map mismatch
- **WHEN** the destination registry refers to a map different from the robot's active map
- **THEN** the system refuses dispatch and identifies the mismatch

### Requirement: Monitor execution faults
The system SHALL monitor feedback and state during execution, request cancellation on stale or invalid state, and report FAULT with evidence rather than arrival.

#### Scenario: Sensor data lost in motion
- **WHEN** an active mission loses fresh scan data
- **THEN** the system requests cancellation, checks the outcome and reports FAULT with the observed cancellation and stopping status

### Requirement: Bound agent retries
The system SHALL allow at most one Agent-level redispatch after a failed navigation attempt, only after the preceding attempt has terminated and new readiness and path checks pass; canceled or timed-out missions SHALL NOT trigger retries.

#### Scenario: Repeated navigation failure
- **WHEN** navigation fails after one Agent-level retry
- **THEN** the system returns FAILED without any further redispatch

### Requirement: Confirm cancellation and stopping separately
The system SHALL distinguish cancellation request acceptance, terminal action state and observed stopping; it SHALL NOT claim the robot has stopped without fresh motion evidence satisfying configured speed thresholds and observation duration.

#### Scenario: Cancel accepted but result unknown
- **WHEN** cancellation is accepted but the action result or fresh motion observations cannot be obtained before the cancellation deadline
- **THEN** the system reports FAULT with stop_confirmed false, identifies unresolved state and blocks new movement

#### Scenario: Cancel confirmed
- **WHEN** the action is terminal CANCELED and fresh motion evidence meets the stopping criteria
- **THEN** the system returns CANCELED with stop_confirmed true and supporting evidence IDs

### Requirement: Enforce mission deadline
The system SHALL request cancellation when the mission deadline expires and report TIMEOUT, including whether termination and stopping were confirmed; unresolved state SHALL block new movement.

#### Scenario: Navigation exceeds deadline
- **WHEN** an active mission reaches its configured deadline
- **THEN** cancellation is requested and TIMEOUT is reported without ARRIVED or an automatic retry

### Requirement: Ground final reports in evidence
The system SHALL report ARRIVED only when navigation returns SUCCEEDED and a fresh final pose satisfies the configured position and heading tolerances on the active map. Every terminal report SHALL include mission identity, timestamps, backend and evidence references.

#### Scenario: Verified arrival
- **WHEN** navigation succeeds and the final pose satisfies the configured end conditions
- **THEN** the report is ARRIVED with the action result, final pose and evidence references

#### Scenario: Success without verified endpoint
- **WHEN** navigation returns SUCCEEDED but final pose evidence is stale, missing or outside tolerance
- **THEN** the system reports FAULT with an endpoint-verification reason instead of claiming arrival
