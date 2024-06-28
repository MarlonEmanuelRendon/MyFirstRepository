from random import randint
bn = 10
we = 0
lista = []
while we != bn:
    we = we + 1
    var = randint(0, bn)
    lista.append(var)
    var1 = randint(0, bn)
    lista.append(var1)
    if var1 == lista[0]:
        lista.remove(var1)





    # for i in lista:
    #     if i == var:
    #         lista.remove(var)
    #         print(lista)
print(lista)
