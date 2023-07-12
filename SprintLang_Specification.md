# SprintLang Language Definition

## Overview

SprintLang is a lightweight markup language (LML) designed for project management. The language provides a structured yet human-readable way to define and manage projects, including project metadata, modules, sprints, and tasks.

## Syntax

### Project File

A SprintLang project is defined in a `.slproj` file. The project file contains the project metadata, module definitions, sprint definitions, and includes task files.

#### Metadata

Metadata is defined at the start of the project file. The following metadata fields are supported:

- `Created:`: The date the project was created.
- `Updated:`: The date the project was last updated.
- `Owner:`: The owner or main contact for the project.
- `Version:`: The version of the project.

#### Modules

Modules are defined using the `Module:` keyword followed by the name of the module. 

#### Sprints

Sprints are defined using the `Sprint:` keyword followed by the name of the sprint. Each sprint has a `Start:` and `End:` date.

#### Task Files

Task files are included using the `Include:` directive followed by the name of the `.tasks` file. 

### Task File

A SprintLang task is defined in a `.tasks` file. The task file contains one or more task definitions.

#### Tasks

Tasks are defined using the `Task:` keyword followed by the name of the task. Each task has the following fields:

- `BelongsTo:`: The module and sprint that the task belongs to.
- `Description:`: A description of the task.
- `Status:`: The status of the task. This must be one of the following values: "Not Started", "In Progress", "Completed".
- `Progress:`: The percentage of the task that is complete.
- `Start:`: The date the task is set to start.
- `Due:`: The date the task is due.
- `Other Date:`: Any other significant dates for the task.
- `Priority:`: The priority of the task. This must be one of the following values: "High", "Medium", "Low".
- `Assigned to:`: The person or team assigned to the task.

## Semantics

The semantics of SprintLang are straightforward. The project file defines the overall structure of the project, including the modules and sprints. Tasks are associated with modules and sprints to organize the work and track progress.

The metadata provides context about the project, such as who is responsible for it and when it was last updated. The status and progress of tasks provide a way to track the progression of the project. The start and due dates of tasks and sprints provide a way to manage the schedule of the project.

