a=[[1,2],[3,4]]
b=[[0,4],[0,0]]
c=[[0,0],[0,0]]

for i in range(len(a)):
    for j in range(len(b[i])):
        for k in range(len(b)):
            
            c[i][j]+=a[i][k]*b[k][j]
for value in c:
    print(value)
    
