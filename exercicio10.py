lista=[-1,-2,-3,-4,0,1,2,3,4,5,6,7,8]
pares=[]
for i in range(13):
  if lista[i]<0:
    print(lista[i])
  elif lista[i]>0:
    print(lista[i])
    pares.append(lista[i])


totalpar=sum(pares)

print(totalpar)