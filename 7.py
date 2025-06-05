def imprimir(altura):
       for i in range(altura):
        print(' '*(altura-i+1)+'*'*(2+i-1))


imprimir(int(input("ingresar tamaño:")))

def estrella(tamano=7):
    for i in range(tamano):
        for j in range(tamano):
            if i == tamano//2 or j == tamano//2 or i == j or i + j == tamano - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()
estrella(9)