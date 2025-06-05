nombre=input("¿Cual es tu nombre?")
r = (input("¿Quieres saber los resultados de unas operaciones"))

if r == "Si":
    print("Todavia puedes seguir contestando %s" %(nombre))
    list = ["1.Resta","2.Multiplicacion","3.Division"]
    print(list)
    

    numero = int(input("Dame un numero entero"))
    numero1 = int(input("Dame otro numero entero"))

    print("Tus numeros son %d y %d" %(numero, numero1))
    print("La ssuma es: ", numero + numero1)
    print("La resta es:", numero - numero1)
    print("La multiplicacion es", numero * numero1)
    print("La divison es",numero / numero1)

else:
    print("Lo siento, Ya no puedes seguir contestando %s" %(nombre))

    list = ["Resta","Multiplicacion"]

