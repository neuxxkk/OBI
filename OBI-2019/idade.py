f =[]

m = int(input())
f.append(int(input()))
f.append(int(input()))

f.append(m - (f[0]+f[1]))

f.sort()

print(f[-1])