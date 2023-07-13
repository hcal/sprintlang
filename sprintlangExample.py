from sprintlanglib.sprintlangproject import SprintLangProject

project_file_path = 'path/to/your/project.slproj'
project = SprintLangProject(project_file_path)
project.import_project_file()
project.import_task_files()

print(project.title)
print(project.metadata)
# ...
