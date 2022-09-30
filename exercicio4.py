lista=[]
listaquad=[]
for i in range(8):
  numero=int(input('Digite um numero:'))
  lista.append(numero)
  
x=int(input('Digite um numero1:'))
y=int(input('Digite um numero2:'))
posicaox=lista.index(x)
posicaoy=lista.index(y)

print("Soma das posições",posicaox+posicaoy)
