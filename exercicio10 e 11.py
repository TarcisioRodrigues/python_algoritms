lista=[-1,-2,-3,-4,0,1,2,3,4,5,6,7,8]
pares=[]
numeros_negativos=0
for i in range(13):
  if lista[i]<0:
    numeros_negativos=numeros_negativos+1
    print(lista[i])
  elif lista[i]>0:
    print(lista[i])
    pares.append(lista[i])


totalpar=sum(pares)

print('Quantidade de numeros negativos',numeros_negativos)
print("Soma dos numeros pares",totalpar)
