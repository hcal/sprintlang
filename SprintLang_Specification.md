# SprintLang Language Definition

## Index
- [Overview](#overview)
- [Syntax](#syntax)
  - [Project File](#project-file)
    - [Title](#title)
    - [Metadata](#metadata)
    - [Modules](#modules)
    - [Cycles](#cycles)
    - [Task Files](#task-files)
    - [Additional Sections](#additional-sections)
  - [Task File](#task-file)
    - [Tasks](#tasks)
- [Semantics](#semantics)
- [Examples](#examples)
  - [Project File Example](#project-file-example)
  - [Task File Example](#task-file-example)

## Overview

SprintLang is a lightweight markup language (LML) designed for project management. The language provides a structured yet human-readable way to define and manage projects, including project title, metadata, modules, cycles, and tasks.

## Syntax

### Project File

A SprintLang project is defined in a `.slproj` file. The project file contains the project title, metadata, module definitions, cycle definitions, and includes task files.

#### Title

The title of the project is defined at the start of the project file, enclosed in `#` for clarity.

#### Metadata

Metadata is defined after the title, enclosed between two lines of three dashes. The following metadata fields are supported:

- `Created:`: The date the project was created.
- `Updated:`: The date the project was last updated.
- `Owner:`: The owner or main contact for the project.
- `Version:`: The version of the project.

Users may add additional metadata fields as needed.

#### Modules

Modules are defined using the `Module:` keyword followed by the name of the module. 

#### Cycles

Cycles are defined using the `Cycle:` keyword followed by the name of the cycle. Each cycle has a `Start:` and `End:` date.

#### Tasks and Task Files

Task files are included using the `Include:` directive followed by the name of the `.tasks` file. Optionally, Tasks can be added directly to the Project (.slprof) file using the same task format defined below in the task file section.

#### Additional Sections

The following additional sections can be added after the task files:

- **Project Description:** A brief description of the project.
- **Team Members and Contacts:** List of team members and their contact information.
- **Notes:** Any additional notes about the project.
- **Deliverables:** Expected outputs or products of the project.
- **Status Updates:** Periodic updates about the project's status.
- **Scope:** The project's boundaries or extent.
- **Stakeholders and Contacts:** List of key stakeholders, their roles, and their level of involvement or interest in the project.
- **Goals and Objectives:** The main goals and objectives of the project.
- **Risks and Mitigations:** Potential risks to the project and plans to mitigate them.
- **Resources:** Key resources for the project, such as documents, tools, or websites.
- **Dependencies:** Dependencies between this project and other projects or tasks.
- **Constraints and Assumptions:** Any constraints (such as budget or time) and assumptions that are being made in the planning of the project.
- **Change Log:** Significant changes to the project, such as scope adjustments, timeline shifts, or resource changes.
- **Lessons Learned:** Lessons learned throughout the project for future reference and improvement.

### Task File

A SprintLang task is defined in a `.tasks` file. The task file contains one or more task definitions.

#### Tasks

Tasks are defined using the `Task:` keyword followed by the name of the task. Each task must have a unique name. Each task has the following fields:

- `Module:`: The module that the task belongs to.
- `Cycle:`: The cycle that the task belongs to.
- `Description:`: A description of the task.
- `Status:`: The status of the task. This must be one of the following values: "Not Started", "In Progress", "Completed".
- `Progress:`: The percentage of the task that is complete. This can be a number from 0 to 100. The percent sign (%) is optional and serves no function.
- `Start:`: The date the task is set to start.
- `Due:`: The date the task is due.
- `Other Date:`: Any other significant dates for the task.
- `Priority:`: The priority of the task. This must be one of the following values: "High", "Medium", "Low".
- `Assigned to:`: The person or team assigned to the task.
- `Notes:`: Any additional notes about the task. This field is enclosed in `<Notes>` and `</Notes>` tags.

## Semantics

The semantics of SprintLang are straightforward. The project file defines the overall structure of the project, including the title, metadata, modules, and cycles. Tasks are associated with modules and cycles to organize the work and track progress.

If the module is left blank, we will assume the task belongs to the backlog, which is also essitially treated as a default special case cycle.

## Examples

### Project File Example

```markdown
# Tech Conference 2023

---
Created: 2023-07-01
Updated: 2023-07-01
Owner: Event Team
Version: 1.0
---

Module: Venue Booking
Module: Speaker Arrangement
Module: Sponsorship Management
Module: Event Management

Cycle: Cycle 1
Start: 2023-07-01
End: 2023-07-15

Cycle: Cycle 2
Start: 2023-07-16
End: 2023-07-31

Include: venue_booking.tasks
Include: speaker_arrangement.tasks
Include: sponsorship_management.tasks
Include: event_management.tasks


#### Task Files

Task files are included using the `Include:` directive followed by the name of the `.tasks` file. 

### Task File

A SprintLang task is defined in a `.tasks` file. The task file contains one or more task definitions.

#### Tasks

Tasks are defined using the `Task:` keyword followed by the name of the task. Each task must have a unique name. Each task has the following fields:

- `Module:`: The module that the task belongs to.
- `Cycle:`: The cycle that the task belongs to.
- `Description:`: A description of the task.
- `Status:`: The status of the task. This must be one of the following values: "Not Started", "In Progress", "Completed".
- `Progress:`: The percentage of the task that is complete. This can be a number from 0 to 100. The percent sign (%) is optional and serves no function.
- `Start:`: The date the task is set to start.
- `Due:`: The date the task is due.
- `Other Date:`: Any other significant dates for the task.
- `Priority:`: The priority of the task. This must be one of the following values: "High", "Medium", "Low".
- `Assigned to:`: The person or team assigned to the task.
- `Notes:`: Any additional notes about the task. This field is enclosed in `<Notes>` and `</Notes>` tags.

## Semantics

The semantics of SprintLang are straightforward. The project file defines the overall structure of the project, including the title, metadata, modules, and cycles. Tasks are associated with modules and cycles to organize the work and track progress.

The metadata provides context about the project, such as who is responsible for it and when it was last updated. The status and progress of tasks provide a way to track the progression of the project. The start and due dates of tasks and cycles provide a way to manage the schedule of the project.

## Examples

### Project File Example

```markdown
# Tech Conference 2023

---
Created: 2023-07-01
Updated: 2023-07-01
Owner: Event Team
Version: 1.0
---

Module: Venue Booking
Module: Speaker Arrangement
Module: Sponsorship Management
Module: Event Management

Cycle: Cycle 1
Start: 2023-07-01
End: 2023-07-15

Cycle: Cycle 2
Start: 2023-07-16
End: 2023-07-31

Include: venue_booking.tasks
Include: speaker_arrangement.tasks
Include: sponsorship_management.tasks
Include: event_management.tasks

### Tasks File Example
```markdown
# venue_booking.tasks

Task: Venue Research
  Module: Venue Booking
  Cycle: Cycle 1
  Description: Research potential venues for the conference and gather information on pricing, capacity, and availability. 
  Status: Completed
  Progress: 100
  Start: 2023-07-01
  Due: 2023-07-05
  Priority: High
  Assigned to: Alice
  <Notes>
  This task was completed ahead of schedule.
  </Notes>

Task: Venue Booking
  Module: Venue Booking
  Cycle: Cycle 2
  Description: Book the chosen venue for the conference.
  Status: In Progress
  Progress: 50
  Start: 2023-07-06
  Due: 2023-07-10
  Priority: High
  Assigned to: Alice
  <Notes>
  We are waiting for the venue to confirm our booking.
  </Notes>
```


