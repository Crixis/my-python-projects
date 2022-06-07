"""
realizar el juego de adivina un numero
"""
import random

nMax=int(input("Ingresa el rango Maximo para el programa: "))
try:
    while True:
        if 0<nMax:
            break
        else:
            nMax=int(input("Por favor ingresa un numero valido: "))
except:
    print("Error lo que has ingresado no es un digito")

elNumero=random.randint(1,nMax)
numPrueba=0
intentos=0

try:
    numPrueba=int(input("Adivina el numero: "))

    while True:
        intentos+=1
        if numPrueba<elNumero:
            numPrueba = int(input("El numero a adivinar es mayor\n Intenta de nuevo: "))
        elif numPrueba>elNumero:
            numPrueba= int(input("El numero a adivinar es menor\n Intenta de nuevo: "))
        else:
            print(f"Genial!!!  Adivinaste, el numero a adivinar era: {elNumero}\n Cantidad de intentos: {intentos}")
            break
except:
    print("Error lo que has ingresado no es un digito")
