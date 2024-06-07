n, k = [int(i) for i in input().split()]

x= []
seq=[]

seq = [int(o) for o in input().split()]

for qtd in range(n): #agrupa de 1 ate 9
    for i in range(n): # passa de elemnto em elemneto
        if qtd:
            for idx in range(i+1, n-(qtd-1)): # roda em cada eelemtnto
                x.append(seq[i]+sum(seq[idx:idx+qtd])) # idx posiçao 
        else: x.append(seq[i])

print(x.count(k))