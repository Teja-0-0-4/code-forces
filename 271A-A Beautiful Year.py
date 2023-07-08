n=int(input())
n+=1
n=str(n)
while True:
    flag=True
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if n[i]==n[j]:
                flag=False
                break
    if flag:
        print(int(n))
        break
    else:
       n=str(int(n)+1)
