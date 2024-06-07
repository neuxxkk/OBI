l = []

for i in range(int(input())):l.append((input(),int(input())))

l.sort(key= lambda i: i[1], reverse=1)

print(l[0][0])
print(l[0][1])
