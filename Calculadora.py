import time as t

#Funcion Suma
def Suma(): 
    numero1 = int(input("Ingrese el numero que va operar: "))
    numero2 = int(input("Ingrese el numero con el que va a sumar: "))
    respuesta = numero1 + numero2
    return respuesta

#Funcion resta
def Resta():
    numero1 = int(input("Ingrese el numero que va operar: "))
    numero2 = int(input("Ingrese el numero con el que va a restar: "))
    respuesta = numero1 - numero2
    return respuesta

#Funcion divicion
def Divicion():
    numero1 = float(input("Ingrese el numero que va operar: "))
    numero2 = float(input("Ingrese el numero con el que va a dividir: "))
    respuesta = numero1/numero2
    return respuesta 

#Funcion Multiplicacion
def Multiplicacion():
    numero1 = int(input("Ingrese el numero que va operar: "))
    numero2 = int(input("Ingrese el numero con el que va a multiplicar: "))
    respuesta = numero1*numero2
    return respuesta 


#MAIN
while True:
    print("Hola y bienvenido a tu calculadora online!")
    print("1) Suma \n 2) Resta \n 3) Divicion \n 4) Multiplicacion")
    try:    
        opcion = int(input("Ingresa el tipo de operacion que quieras realizar: "))

    #Opcion de suma
        if opcion == 1:
            respuesta = Suma()
            print(respuesta)
            t.sleep(0.5)
            
#Opcion de resta
        elif opcion == 2:
            respuesta = Resta()
            print(respuesta)
            t.sleep(0.5)
            
#Opcion de divicion
        elif opcion == 3:
            respuesta = Divicion()
            print(respuesta)
            t.sleep(0.5)
    
            
#Opcion de multiplicacion
        elif opcion == 4:
            respuesta = Multiplicacion()
            print(respuesta)
            t.sleep(0.5)
            
        #Else por si se elijen numero fuera de las opciones
        else:
            print("Opcion no valida")
            t.sleep(0.5)
    except ZeroDivisionError:    
        print("You cannot divide by zero!")
    except Exception as e:
        print(e, "No es una opcion no valida")
        #Catch por si se selecciona cualquier otro digito que no sea un int    

    



    