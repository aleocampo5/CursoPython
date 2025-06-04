def imprimir(altura):


    for i in range(altura):
        print(' '*(altura-i)+'*')
        print('*'*(altura+i+1)+' '*)



imprimir(int(input("ingresar tamaño:")))