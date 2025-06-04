list1 =["Alejandra","Gonzalez","Ocampo"]
list2 =[1,2,3,4,5,6,]
list3 =["Jalisco", "Morelos", "Chihuahua"]
print(list1)
print(list2)
print(list3)

def imprimir(altura):
    for i in range(altura):
        print(' '*(altura-i-1)+'*'*(2*i+1))

    for _ in range(max(1,altura//3)):
        print(' '*(altura-1)+ '|')

imprimir(int(input("ingresar tamaño:")))
