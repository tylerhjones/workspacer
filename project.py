__author__ = 'tyler'
import subprocess

class Project(object):
    def __init__(self, path):
        self.path = path
        self.branches = self.get_branches(path)
        self.starting_branch = self.get_branch(path)

    def get_branches(self, path):
        pr = subprocess.Popen("git branch",
                          cwd=path,
                          shell=True,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
        (out, error) = pr.communicate()
        if(error):
            raise Exception(error)
        return [x.strip().strip('* ') for x in out.split('\n')]

    def get_branch(self, path):
        pr = subprocess.Popen("/usr/bin/git rev-parse --abbrev-ref HEAD",
                          cwd=path,
                          shell=True,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
        (out, error) = pr.communicate()
        if(error):
            raise Exception(error)
        return out