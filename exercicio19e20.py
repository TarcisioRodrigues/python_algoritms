lista=[]

for i in range(10):
  valor=int(input('Digite o valor :'))
  lista.append(valor)
  
print(lista)

n=int(input('Digite o numero'))
for x in lista :
  if x %n ==0:
    print('Multiplos de x:')

#20
lista=[]

for i in range(50):
  lista.append((i+5*i)%(i+1))
  
print(lista)