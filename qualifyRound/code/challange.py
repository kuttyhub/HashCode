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

