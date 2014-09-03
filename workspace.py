__author__ = 'tyler'
import os
import project

class Workspace(object):
    def __init__(self, path):
        self.path = path
        self.projects = self.set_projects(path)

    def find_projects(self, path):
        projects = []
        folders = [os.path.join(path, o) for o in os.listdir(path) if
                 (os.path.isdir(os.path.join(path, o)) and os.path.basename(os.path.join(path, o))[0] != '.')]

        for folder in folders:
            if (os.path.isdir(folder + '/.git')):
                projects.append(folder)
        return projects

    def set_projects(self, path):
        project_paths = self.find_projects(path)
        projects = []
        for project_path in project_paths:
            projects.append(project.Project(project_path))
        return projects

    def find_workspaces(self):
        workspaces = {}
        for project in self.projects:
            for branch in project.branches:
                if('workspace/' in branch):
                    workspaces[branch] = True
        return list(workspaces.keys())