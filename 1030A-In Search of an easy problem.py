n=int(input())
l=list(map(int,input().split()))
count0=0
count1=0
for each in l:
    if each==0:
        count0+=1
    else:
        count1+=1
if(count1>0):
    print("HARD")
else:
    print("EASY")