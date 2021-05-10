import os
import random
from tabulate import tabulate
import pandas as pd
from os import system
CARPETA = 'Jugadores/'   # Carpeta de contactos
EXTENSION = '.txt'     #Extensión de archivos
def car():
    crear_registro()
    agregar_jugador = True
    while agregar_jugador:

        cantidad = input('¿Cuántos jugadores quieres agregar? Máximo 4, mínimo 3.\r\n')
        cantidad = int(cantidad)
        
        if cantidad ==3:
            jugador1 = input(f'Escribe el nombre del primer jugador\r\n')
            jugador2 = input(f'Escribe el nombre del segundo jugador\r\n')
            jugador3 = input(f'Escribe el nombre del tercer jugador\r\n')
            system ('clear')
            agregar_jugador = False
        elif cantidad ==4:
            jugador1 = input(f'Escribe el nombre del primer jugador\r\n')
            jugador2 = input(f'Escribe el nombre del segundo jugador\r\n')
            jugador3 = input(f'Escribe el nombre del tercer jugador\r\n')
            jugador4 = input(f'Escribe el nombre del cuarto jugador\r\n')
            system ('clear')
            agregar_jugador = False 
        else:
            print('Escribir un número válido')

    #Pistas del juego
    print('Se tienen las siguientes pistas disponibles')
    print('1) Hawaii - 10 km')
    print('2) Sydney - 12 km')
    print('3) New York - 8 km')
    pista = input ('¿Cuál pista escoges?\r\n')
    pista = int (pista)

    #Presentación
    print (f'El juego está a punto de comenzar\r\n')
    print (f'Correrán en la pista: {pista}')
    print ('El avance de los vehículos depende de un dado\r\nEl número que salga será cambiado a metros,\r\n sería el avance que tiene el respectivo carro en la pista\r\n\r\n')
        

    avance1=0
    avance2=0
    avance3=0
    avance4=0
    # Cuatro Jugadores - Pista 1 Hawaii con 10000 metros
    while cantidad == 4 and pista == 1:
        
           
        tabla = [[jugador1, avance1],
                [jugador2, avance2],
                [jugador3, avance3],
                [jugador4, avance4]]
        indice = [1 , 2 ,3 ,4]
        print (tabulate(tabla,
                        headers=['Nombre Jugador','Recorrido'],
                        tablefmt='fancy_grid',
                        showindex=indice,
                        stralign='center',
                        numalign='center'))
        
        if avance1 >= 10000 or avance2 >= 10000 or avance3 >= 10000 or avance4 >= 10000:
            break
        else:
            None
        lanzar = input('¿Desea lanzar los dados? S/N\r\n')

        if (lanzar == 'S'):
            dado1 = random.randint(1,6)
            print('El dado para el jugador 1 cayó en: ', dado1)
            dado1 = int(dado1)
            avance1 += dado1 * 100
    
            dado2 = random.randint(1,6)
            print('El dado para el jugador 2 cayó en: ', dado2)
            dado2 = int(dado2)
            avance2 += dado2 * 100

            dado3 = random.randint(1,6)
            print('El dado para el jugador 3 cayó en: ', dado3)
            dado3 = int(dado3)
            avance3 += dado3 * 100

            dado4 = random.randint(1,6)
            print('El dado para el jugador 4 cayó en: ', dado4)
            dado4 = int(dado4)
            avance4 += dado4 * 100
            system('clear')

        else:
            print ('Lamentamos que no quieras jugar. Hasta la próxima !!!')
            break
    
    # Cuatro Jugadores - Pista 2 Sydney con 12000 metros       
    while cantidad == 4 and pista == 2:
        
           
        tabla = [[jugador1, avance1],
                [jugador2, avance2],
                [jugador3, avance3],
                [jugador4, avance4]]
        indice = [1 , 2 ,3 ,4]
        print (tabulate(tabla,
                        headers=['Nombre Jugador','Recorrido'],
                        tablefmt='fancy_grid',
                        showindex=indice,
                        stralign='center',
                        numalign='center'))

        
        
        if avance1 >= 12000 or avance2 >= 12000 or avance3 >= 12000 or avance4 >= 12000:
            break
        else:
            None
        lanzar = input('¿Desea lanzar los dados? S/N\r\n')

        if (lanzar == 'S'):
            dado1 = random.randint(1,6)
            print('El dado para el jugador 1 cayó en: ', dado1)
            dado1 = int(dado1)
            avance1 += dado1 * 100
    
            dado2 = random.randint(1,6)
            print('El dado para el jugador 2 cayó en: ', dado2)
            dado2 = int(dado2)
            avance2 += dado2 * 100

            dado3 = random.randint(1,6)
            print('El dado para el jugador 3 cayó en: ', dado3)
            dado3 = int(dado3)
            avance3 += dado3 * 100

            dado4 = random.randint(1,6)
            print('El dado para el jugador 4 cayó en: ', dado4)
            dado4 = int(dado4)
            avance4 += dado4 * 100
            system ('clear')

        else:
            print ('Lamentamos que no quieras jugar. Hasta la próxima !!!')
            break     

    # Cuatro Jugadores - Pista 3 New York con 8000 metros       
    while cantidad == 4 and pista == 3:
        
           
        tabla = [[jugador1, avance1],
                [jugador2, avance2],
                [jugador3, avance3],
                [jugador4, avance4]]
        indice = [1 , 2 ,3 ,4]
        print (tabulate(tabla,
                        headers=['Nombre Jugador','Recorrido'],
                        tablefmt='fancy_grid',
                        showindex=indice,
                        stralign='center',
                        numalign='center'))

        lanzar = input('¿Desea lanzar los dados? S/N\r\n')
        
        if avance1 >= 8000 or avance2 >= 8000 or avance3 >= 8000 or avance4 >= 8000:
            break
        else:
            None

        if (lanzar == 'S'):
            dado1 = random.randint(1,6)
            print('El dado para el jugador 1 cayó en: ', dado1)
            dado1 = int(dado1)
            avance1 += dado1 * 100
    
            dado2 = random.randint(1,6)
            print('El dado para el jugador 2 cayó en: ', dado2)
            dado2 = int(dado2)
            avance2 += dado2 * 100

            dado3 = random.randint(1,6)
            print('El dado para el jugador 3 cayó en: ', dado3)
            dado3 = int(dado3)
            avance3 += dado3 * 100

            dado4 = random.randint(1,6)
            print('El dado para el jugador 4 cayó en: ', dado4)
            dado4 = int(dado4)
            avance4 += dado4 * 100
            system ('clear')

        else:
            print ('Lamentamos que no quieras jugar. Hasta la próxima !!!')
            break             
    
    while cantidad == 3 and pista == 1:
        tabla = [[jugador1, avance1],
                [jugador2, avance2],
                [jugador3, avance3]]
        indice = [1 , 2 ,3]
        print (tabulate(tabla,
                        headers=['Nombre Jugador','Recorrido'],
                        tablefmt='fancy_grid',
                        showindex=indice,
                        stralign='center',
                        numalign='center'))

        lanzar = input('¿Desea lanzar los dados? S/N\r\n')
        
        if avance1 >= 10000 or avance2 >= 10000 or avance3 >= 10000:
            break
        else:
            None

        if (lanzar == 'S'):
            dado1 = random.randint(1,6)
            print('El dado para el jugador 1 cayó en: ', dado1)
            dado1 = int(dado1)
            avance1 += dado1 * 100
    
            dado2 = random.randint(1,6)
            print('El dado para el jugador 2 cayó en: ', dado2)
            dado2 = int(dado2)
            avance2 += dado2 * 100

            dado3 = random.randint(1,6)
            print('El dado para el jugador 3 cayó en: ', dado3)
            dado3 = int(dado3)
            avance3 += dado3 * 100
            system ('clear')


        else:
            print ('Lamentamos que no quieras jugar. Hasta la próxima !!!')
            break

    while cantidad == 3 and pista == 2:
        tabla = [[jugador1, avance1],
                [jugador2, avance2],
                [jugador3, avance3]]
        indice = [1 , 2 ,3]
        print (tabulate(tabla,
                        headers=['Nombre Jugador','Recorrido'],
                        tablefmt='fancy_grid',
                        showindex=indice,
                        stralign='center',
                        numalign='center'))

        lanzar = input('¿Desea lanzar los dados? S/N\r\n')
        
        if avance1 >= 12000 or avance2 >= 12000 or avance3 >= 12000:
            break
        else:
            None

        if (lanzar == 'S'):
            dado1 = random.randint(1,6)
            print('El dado para el jugador 1 cayó en: ', dado1)
            dado1 = int(dado1)
            avance1 += dado1 * 100
    
            dado2 = random.randint(1,6)
            print('El dado para el jugador 2 cayó en: ', dado2)
            dado2 = int(dado2)
            avance2 += dado2 * 100

            dado3 = random.randint(1,6)
            print('El dado para el jugador 3 cayó en: ', dado3)
            dado3 = int(dado3)
            avance3 += dado3 * 100
            system ('clear')

    while cantidad == 3 and pista == 3:
        tabla = [[jugador1, avance1],
                [jugador2, avance2],
                [jugador3, avance3]]
        indice = [1 , 2 ,3]
        print (tabulate(tabla,
                        headers=['Nombre Jugador','Recorrido'],
                        tablefmt='fancy_grid',
                        showindex=indice,
                        stralign='center',
                        numalign='center'))

        lanzar = input('¿Desea lanzar los dados? S/N\r\n')
        
        if avance1 >= 8000 or avance2 >= 8000 or avance3 >= 8000:
            break
        else:
            None

        if (lanzar == 'S'):
            dado1 = random.randint(1,6)
            print('El dado para el jugador 1 cayó en: ', dado1)
            dado1 = int(dado1)
            avance1 += dado1 * 100
    
            dado2 = random.randint(1,6)
            print('El dado para el jugador 2 cayó en: ', dado2)
            dado2 = int(dado2)
            avance2 += dado2 * 100

            dado3 = random.randint(1,6)
            print('El dado para el jugador 3 cayó en: ', dado3)
            dado3 = int(dado3)
            avance3 += dado3 * 100
            system ('clear')

    df=pd.DataFrame(tabla)
    tabla_ordenada= df.sort_values(1, ascending=False)
    #print (tabla_ordenada)
    print ('El podium quedó de la siguiente manera:\r\n')
    print (f'1er puesto: ',tabulate(tabla_ordenada.iloc[[0]],showindex=False, tablefmt='plain'))
    print ('2do puesto: ',tabulate(tabla_ordenada.iloc[[1]],showindex=False, tablefmt='plain'))
    print ('3er puesto: ',tabulate(tabla_ordenada.iloc[[2]],showindex=False, tablefmt='plain'))       

    

        




  #  while agregar_jugador:
   #     print('Máximo puedes agregar tres (3) jugadores\r\n')

def crear_registro:
    if not os.path.exists(CARPETA):     #Verifica si la carpeta está creada, si no, se crea con os.makedir



car()