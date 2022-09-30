lista=[]
vezespar=0
for i in range(10):
  numero=int(input('Digite um numero:'))
  lista.append(numero)
  if numero%2==0:
    vezespar=vezespar+1
  
  
print('Quantidades de numeros pares',vezespar)