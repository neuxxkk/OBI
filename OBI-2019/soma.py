n, k = [int(i) for i in input().split()]

ans=0

seq = [int(o) for o in input().split()]

for i in range(n):
    for j in range(i, n):
        if sum(seq[i:j+1]) == k: ans+=1

print(ans)