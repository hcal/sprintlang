import os
import re

class SprintLangProject:
    def __init__(self, project_file_path):
        self.project_file_path = project_file_path
        self.title = None
        self.metadata = {}
        self.modules = []
        self.cycles = []
        self.task_files = []
        self.description = None
        self.team_members = []
        self.notes = None
        self.deliverables = None
        self.status_updates = None
        self.scope = None
        self.stakeholders = None
        self.goals = None
        self.risks = None
        self.resources = None
        self.dependencies = None
        self.constraints = None
        self.change_log = None
        self.lessons_learned = None

    def import_project_file(self):
        with open(self.project_file_path, 'r') as file:
            content = file.read()
            self.title = re.search(r'#\s*(.*)', content).group(1).strip()

            metadata_match = re.search(r'---\n(.*?)\n---', content, re.DOTALL)
            if metadata_match:
                metadata_content = metadata_match.group(1)
                metadata_lines = metadata_content.strip().split('\n')
                for line in metadata_lines:
                    key, value = line.split(':', 1)
                    self.metadata[key.strip()] = value.strip()

            self.modules = re.findall(r'Module:\s*(\w+)', content)
            self.cycles = re.findall(r'Cycle:\s*(.*)\nStart:\s*(.*)\nEnd:\s*(.*)', content)
            self.task_files = re.findall(r'Include:\s*(.*)', content)

            additional_sections_match = re.findall(r'###\s*(.*?)\n(.*?)\n\n', content, re.DOTALL)
            for section in additional_sections_match:
                section_title = section[0]
                section_content = section[1].strip()
                if section_title == 'Project Description':
                    self.description = section_content
                elif section_title == 'Team Members and Contacts':
                    self.team_members = re.findall(r'-\s*(.*)', section_content)
                elif section_title == 'Notes':
                    self.notes = section_content
                elif section_title == 'Deliverables':
                    self.deliverables = section_content
                elif section_title == 'Status Updates':
                    self.status_updates = section_content
                elif section_title == 'Scope':
                    self.scope = section_content
                elif section_title == 'Stakeholders and Contacts':
                    self.stakeholders = section_content
                elif section_title == 'Goals and Objectives':
                    self.goals = section_content
                elif section_title == 'Risks and Mitigations':
                    self.risks = section_content
                elif section_title == 'Resources':
                    self.resources = section_content
                elif section_title == 'Dependencies':
                    self.dependencies = section_content
                elif section_title == 'Constraints and Assumptions':
                    self.constraints = section_content
                elif section_title == 'Change Log':
                    self.change_log = section_content
                elif section_title == 'Lessons Learned':
                    self.lessons_learned = section_content

    def import_task_files(self):
        for task_file in self.task_files:
            task_file_path = os.path.join(os.path.dirname(self.project_file_path), task_file)
            if not os.path.isfile(task_file_path):
                task_file_path = os.path.join(os.path.dirname(self.project_file_path), 'tasks', task_file)
            if os.path.isfile(task_file_path):
                with open(task_file_path, 'r') as file:
                    content = file.read()
                    tasks = re.findall(r'Task:\s*(.*?)\n(.*?)\n\n', content, re.DOTALL)
                    for task in tasks:
                        task_name = task[0]
                        task_content = task[1].strip()
                        task_fields = re.findall(r'-\s*(.*?):\s*(.*)', task_content)
                        task_dict = {field[0]: field[1] for field in task_fields}
                        task_dict['Description'] = task_dict.get('Description')
                        task_dict['Assigned to'] = task_dict.get('Assigned to')
                        setattr(self, task_name, task_dict)
            else:
                print(f"Task file '{task_file}' not found.")

# Example usage
project_file_path = 'path/to/your/project.slproj'
project = SprintLangProject(project_file_path)
project.import_project_file()
project.import_task_files()

# Access project data
print(project.title)
print(project.metadata)
print(project.modules)
print(project.cycles)
print(project.task_files)
print(project.Team_Member_1)
print(project.Team_Member_2)
