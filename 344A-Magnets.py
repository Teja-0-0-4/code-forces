l = []
count = 0
n = int(input())
for i in range(n):
    l.append(input())
for i in range(n - 1):
    if l[i] == "01" and l[i + 1] == "10" or l[i] == "10" and l[i + 1] == "01":
        count += 1
print(count + 1)