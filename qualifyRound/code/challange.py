from msilib.schema import Class


file1 = open(r"E:\Coding Competition\Hash Code\qualifyRound\input_data\a_an_example.in.txt")
lines = file1.read().splitlines()
# print(lines)
contributersNo ,projectsNo=map(int,lines[0].split())
skill={}
projects={}
idx = 1
for i in range(contributersNo):
    name,no = lines[idx].split()
    idx+=1
    for j in range(int(no)):
        sk,level = lines[idx].split()
        # skill[name]=lines[idx]
        skill[sk]=skill.get(sk,[])+[name+" "+level]
        idx+=1
for k,v in skill.items():
    skill[k] = sorted(v,key=lambda x: int(x.split()[-1]))

for i in range(projectsNo):
    r = lines[idx].split()
    idx+=1
    for j in range(int(r[-1])):
        projects[r[0]]=projects.get(r[0],[])+[lines[idx]]
        idx+=1
print(skill)
print(projects)

from typing import List

class Skill:
    def __init__(self,name:str,level:int) -> None:
        self.name=name
        self.level=level

class Role:
    def __init__(self,roll_number:int,skill:Skill) -> None:
        self.roll_number=roll_number
        self.skill=skill

class Contributor:
    def __init__(self,name :str,skills :List(Skill)) -> None:
        self.name=name
        self.skills=skills
        self.isAssigned=False

class Project:
    def __init__(self,name:str,duration:int,score:int,best_before:int,roles:List(Role)) -> None:
        self.name=name
        self.duration=duration
        self.score=score
        self.best_before=best_before
        self.roles=roles
        self.contributors=[]


#Solution

projects : List(Project)=[]
contributors : List(Contributor)=[]

projects.sort(lambda x:x.score-x.duration) #sorting projects based on priority
#priority is determined using score-duration -- score should be high, duration should be low

result=[]

def canDo(project:Project):
    project.contributors=[]
    pass

while len(projects)>1:  # TODO: should include the case when no project can be done
    for project in projects:
        if canDo(project): #canDo() will populate the "project.contributors" list
            result.append(project)
            projects.remove(project)
            break
    
