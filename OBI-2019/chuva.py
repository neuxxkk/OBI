n, m = [int(i) for i in input().split()]

c=[]

for i in range(n):
    c.append([o for o in input()])

r = [[0, m-1], [m, -1], [1,-1]]

for g in range(2):
    for o in range(2):
        for i in range(n):
            for j in range(r[0][o], r[1][o], r[2][o]):
                if c[i][j]=='.':
                    if (i and j) and (i!=n-1 and j!=m-1):
                        if (c[i-1][j] == 'o') or (c[i][j-1]=='o' and c[i+1][j-1]=='#') or (c[i][j+1]=='o' and c[i+1][j+1]=='#'):
                            c[i][j]='o'
                    elif i:
                        if (j and j!=m-1) and (c[i-1][j] == 'o'):c[i][j]='o'
                        elif j==0 and (c[i][j+1]=='o' and c[i+1][j+1]=='#'):c[i][j]='o'
                        elif j==m-1 and (c[i][j-1]=='o' and c[i+1][j-1]=='#'):c[i][j]='o'
                        elif (c[i-1][j] == 'o'):c[i][j]='o'

                    elif not i:
                        if not j and (c[i][j+1]=='o' and c[i+1][j+1]=='#'): c[i][j]='o'
                        elif j==m-1 and (c[i][j-1]=='o' and c[i+1][j-1]=='#'): c[i][j]='o'
                        elif j and j!=m-1:
                            if (c[i][j-1]=='o' and c[i+1][j-1]=='#') or (c[i][j+1]=='o' and c[i+1][j+1]=='#'):
                                c[i][j]='o'

ans=[]
for i in range(n): 
    ans.append(''.join(c[i]))

print(c)


""" 
c(i - 1, j)= “o”; ou
• c(i, j - 1)= “o” e c(i + 1, j - 1)= “#”; ou
• c(i, j + 1)= “o” e c(i + 1, j + 1)= “#”. """