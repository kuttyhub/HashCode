file1 = open(r"E:\Coding Competition\Hash Code\Practice\input_data\a_an_example.in.txt")
lines = file1.read().splitlines()
# print(lines)

t= int(lines[0])
likes=set()
disLikes=set()
idx =1
for _ in range(t):
    l=lines[idx].split()
    for i in range(1,len(l)):
        likes.add(l[i])
    dl=lines[idx+1].split()
    for i in range(1,len(dl)):
        disLikes.add(dl[i])
    idx+=2
# print(disLikes)
for i in disLikes:
    if i in likes:
        likes.remove(i)
l=list(likes)
l.sort()
print(str(len(likes))+" "+" ".join(l))