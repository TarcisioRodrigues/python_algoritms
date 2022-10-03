lista=[]

for i in range(5):
  valor=int(input("Digite um valor inteiro:"))
  lista.append(valor)
print(lista)

soma_valores=sum(lista)
maior=max(lista)
menor=min(lista)
print("Maior valor",maior)
print("Menor valor",menor)
print('Media',soma_valores/5)
print("Posição do menor valor",lista.index(menor))
print("Posição do maior valor",lista.index(maior))