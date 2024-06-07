answer=0

estoque=[]

l = [int(i) for i in input().split()][0]

for m in range(l):
    estoque.extend(int(n) for n in input().split())

c = int(input())

for i in range(c):
    a,b = (int(o) for o in input().split())
    if estoque[a*b-1]>0: 
        estoque[a*b-1]-=1
        answer+=1

print(answer)
