pagas=0
contas=[]

v=int(input())

contas.append(int(input()))
contas.append(int(input()))
contas.append(int(input()))

contas.sort()

for i in contas:
    if i<=v:
        v-=i
        pagas+=1
    else: break

print(pagas)

