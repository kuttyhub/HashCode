import sys


class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = level


class Project:
    def __init__(self, name, duration, score, best_before, skills):
        self.name = name
        self.duration = duration
        self.score = score
        self.best_before = best_before
        self.skills = skills
        self.contributors = []


file1 = open(
    r"E:\Coding Competition\Hash Code\qualifyRound\input_data\a_an_example.in.txt")
lines = file1.read().splitlines()
# print(lines)
contributersNo, projectsNo = map(int, lines[0].split())
skill = {}
projects = {}
idx = 1
for i in range(contributersNo):
    name, no = lines[idx].split()
    idx += 1
    for j in range(int(no)):
        sk, level = lines[idx].split()
        # skill[name]=lines[idx]
        skill[sk] = skill.get(sk, [])+[name+" "+level]
        idx += 1
for k, v in skill.items():
    skill[k] = sorted(v, key=lambda x: int(x.split()[-1]))

for i in range(projectsNo):
    r = lines[idx].split()
    idx += 1
    for j in range(int(r[-1])):
        # projects[r[0]]=projects.get(r[0],[])+[lines[idx]]
        print(r, j)
        # projects[r[0]] = Project()
        idx += 1

projects.sort(lambda x: x.score-x.duration)
print(skill)
print(projects)

result = []

# def canDo(project:Project):
#     _list = []
#     for projReq in project.skills:
#         ls = skill[projReq.name]
#         if int(ls[-1].split()[-1]) < projReq.level:
#             return False
#         for j in ls:
#             name, _ = j.split()[-1]
#             _list.append(name)
#     project.contributors = _list
#     return True

# while len(projects)>1:
#     for project in projects:
#         if canDo(project):
#             result.append(project)
#             projects.remove(project)
#             break
