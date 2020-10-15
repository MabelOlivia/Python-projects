from datetime import *


class Project:
    def __init__(self, name, startDate,endDate):
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(task)


class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.resources = []

    def addResource(self, resource):
        self.resources.append(resource)


class Resource:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill


project = Project("AI", date(2020, 1, 1), date(2021, 1, 1))
task = Task("creating a bot", 90)
resource = Resource("Livy", "python")
project.addTask(task)
task.addResource(resource)


for eachTask in project.tasks:
    print(eachTask.name)
    print(eachTask.duration)
    for eachResource in eachTask.resources:
        print(eachResource.name)
        print(eachResource.skill)
