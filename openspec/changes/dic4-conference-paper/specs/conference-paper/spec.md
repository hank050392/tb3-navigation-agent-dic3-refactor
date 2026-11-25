## ADDED Requirements

### Requirement: IEEE conference manuscript

The project SHALL provide a conference manuscript in IEEE double-column format through Overleaf.

#### Scenario: Compile manuscript
- **WHEN** the manuscript is compiled in Overleaf
- **THEN** a readable IEEE conference PDF is generated

### Requirement: Evidence traceability

The manuscript SHALL distinguish verified offline results from planned simulation and physical experiments.

#### Scenario: Report offline verification
- **WHEN** offline test results are reported
- **THEN** the manuscript identifies their mock execution scope

### Requirement: MCP-assisted workflow

The project SHALL document actual MCP tool usage in the manuscript development or verification workflow.

#### Scenario: Execute MCP tool
- **WHEN** an MCP tool is successfully invoked
- **THEN** the tool name, purpose, and observed result are recorded

### Requirement: GitHub reproducibility

The project SHALL maintain manuscript source and OpenSpec artifacts in the individual GitHub repository.

#### Scenario: Publish project artifacts
- **WHEN** DIC4 artifacts are committed and pushed
- **THEN** the manuscript source and specifications are accessible in the repository
