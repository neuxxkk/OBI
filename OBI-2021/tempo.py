geral=0
ans = {}

v=[]

n = int(input())

for i in range(n):
    c, x = [f for f in input().split()]

    for j in ans:
        if ans[j][1]<0 and c!='T': ans[j][0]+=1

    if c == 'T':
        for o in ans:
            if ans[o][1]<0:
                ans[o][0]+=int(x)-1
    elif c == 'R':
        if x in v:
            ans[x][1]=-1
        else:
            v.append(x)
            ans.update({x:[0, -1]})
    elif c == 'E':
        ans[x][1]=1

g = sorted(ans)
for i in g:
    if ans[i][1]>0:print(i,'',ans[i][0])
    else: print(i,'',ans[i][1])