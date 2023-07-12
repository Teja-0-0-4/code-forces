n=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(n):
    if l[i]==0:
        continue
    sum=sum+l[i]
final=sum/n
print("{0:.12f}".format(final))