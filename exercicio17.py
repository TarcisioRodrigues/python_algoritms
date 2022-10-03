lista=[]

for i in range(10):
  valor=int(input('Digite um valor:'))
  lista.append(valor)
  
  if lista[i]<0:
    lista[i]=0
  
print(lista)

