n=int(input())
l=list(map(int,input().split()))
for i in range(1,n+1):
    for j in range(n):
        if l[j]==i:
            print(j+1)