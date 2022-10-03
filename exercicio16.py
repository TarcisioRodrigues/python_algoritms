from ast import While


listaint = []
# listafloat=[]
# for j in range(5):
#     valorfloat=float(input("Digite um valor decimal"))
#     listafloat.append(valorfloat)
while True:
    for i in range(5):
        valorint = int(input("Digite um valor inteiro:"))
        listaint.append(valorint)

    menu = int(input("Digite 0 - para finalizar o programar 1-vetor ordem direita 2-vetor na inversa")
               )
    if menu == 0:
        break
    elif menu == 1:
        print(listaint)
    elif menu == 2:
        reverso=reversed(listaint)
        for x in reverso:
          print(x)
    elif menu != 1 or menu != 2:
        print('Codigo invalido')
