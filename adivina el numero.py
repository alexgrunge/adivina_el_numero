import random
import time
from os import system


while True: 

#funcion modo facil
    def modo_facil():
       
        numero = random.randrange(10) #numero aleatorio
        
        contador = 5
        while contador >= 0:
           
            print("adivina el numero")
            valor_pensado = int(input(" "))

            # si acierta
            if valor_pensado ==  numero:
                time.sleep(1.1)
                system("cls")
                print(" GENIAL ACERTASTE!!")
                time.sleep(1.8)
                system("cls")

                break
            # si es mayor el valor pensado
            if valor_pensado > numero:
                time.sleep(1.2)
                system("cls")
                print("ERROR!! el numero es menor")
                contador -= 1
                time.sleep(1.5)
                system("cls")
                print("oportunidades")
                print(contador)
                time.sleep(1.5)
                system("cls")
               
              
            #si es menor el valor pensado
            if valor_pensado < numero:
                time.sleep(1.2)
                system("cls")
                print("ERROR!!  el numero es mayor")
                contador -= 1
                time.sleep(1.5)
                print("oportunidades")
                print(contador)
                time.sleep(1.5)
                system("cls")
               
            # si pierde
            if contador == 0:
                print("UPS PERDIST")
                time.sleep(1.5)
                system("cls")
                break

#funcion modo medio
    def modo_medio():
       
        numero = random.randrange(15) #numero aleatorio
        
        contador = 5 
        while contador >= 0:
           
            print("adivina el numero")
            valor_pensado = int(input(" "))
            # si acierta
            if valor_pensado ==  numero:
                time.sleep(1.1)
                system("cls")
                print(" GENIAL ACERTASTE!!")
                time.sleep(1.8)
                system("cls")

                break
            
            # si es mayor el valor pensado
            if valor_pensado > numero:
                time.sleep(1.2)
                system("cls")
                print("ERROR!! el numero es menor")
                contador -= 1
                time.sleep(1.5)
                system("cls")
                print("oportunidades")
                print(contador)
                time.sleep(1.5)
                system("cls")
               
              
            # si es menor el valor pensado
            if valor_pensado < numero:
                time.sleep(1.2)
                system("cls")
                print("ERROR!!  el numero es mayor")
                contador -= 1
                time.sleep(1.5)
                print("oportunidades")
                print(contador)
                time.sleep(1.5)
                system("cls")
               
            # si pierde
            if contador == 0:
                print("UPS PERDISTE!!")
                time.sleep(1.5)
                system("cls")
                break


#funcion modo dificil
    def modo_dificil():
       
        numero = random.randrange(20) # numero aleatorio
        contador = 5
        while contador >= 0:

            
            print("adivina el numero")
            valor_pensado = int(input(" "))
            # si acierta
            if valor_pensado ==  numero:
                time.sleep(1.1)
                system("cls")
                print(" GENIAL ACERTASTE!!")
                time.sleep(1.8)
                system("cls")

                break
            # si es mayor el valor pensado
            if valor_pensado > numero:
                time.sleep(1.2)
                system("cls")
                print("ERROR!! el numero es menor")
                contador -= 1
                time.sleep(1.5)
                system("cls")
                print("oportunidades")
                print(contador)
                time.sleep(1.5)
                system("cls")
               
              
            # si es menor el valor pensado
            if valor_pensado < numero:
                time.sleep(1.2)
                system("cls")
                print("ERROR!!  el numero es mayor")
                contador -= 1
                time.sleep(1.5)
                print("oportunidades")
                print(contador)
                time.sleep(1.5)
                system("cls")
               
            # si pierde
            if contador == 0:
                print("UPS PERDISTE!!")
                time.sleep(1.5)
                system("cls")
                break


# modos de dificultad
    print(" \n Selecciona la dificultad \n 1.facil \n 2.medio \n 3.dificil ")
    dificultad = int(input(" "))
    system("cls")
    time.sleep(1.8)
  
  

#condiciones
    if dificultad == 1:
        print("\n estoy pensando en un número del uno al 10 \n tienes 5 intentos para adivinar cual es ")
        time.sleep(3.0)
        system("cls")
        modo_facil()

    if dificultad == 2:
        print("\n estoy pensando en un número del uno al 15 \n tienes 5 intentos para adivinar cual es ")
        time.sleep(3.0)
        system("cls")
        modo_medio()
    
    if dificultad == 3:
        print("\n estoy pensando en un número del uno al 20 \n tienes 5 intentos para adivinar cual es ")
        time.sleep(3.0)
        system("cls")
        modo_dificil()



      