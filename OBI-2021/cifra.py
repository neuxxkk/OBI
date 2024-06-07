vogais = 'aeiou'
alfabeto = 'abcdefghijklmnopqrstuvxz'
vogals_index = [0,4,8,14,20]

p = input()
l=[]
block=[]

for l in p:
    if l in alfabeto and l not in vogais:
        temp = []
        for vi in vogals_index:
            ai = alfabeto.index(l)
            temp.append([abs(vi-ai), vi-ai])

        temp.sort()

        if l =='z':
            c ='z'
        elif alfabeto[ai+1] not in vogais:
            c = alfabeto[ai+1]
        else:
            c=alfabeto[ai+2]
        block.append(''.join([l, alfabeto[ai+temp[0][1]], c]))

    else: block.append(l)

print(''.join(block))
    
