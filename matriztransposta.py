lista=[[1,2,3],[4,5,6],[7,8,9]]
vazia=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
  for j in range(3):
    vazia[j][i]=lista[i][j]

print(vazia)