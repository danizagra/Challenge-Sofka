from tabulate import tabulate
import random
avance1=0
avance2=0
avance3=0
avance4=0
cantidad =4
pista =1
jugador1= 'Daniel'
jugador2= 'Clarivel'
jugador3= 'Lucas'
jugador4= 'Conrado'
while cantidad == 4 and pista == 1:
        
           
        tabla = [[jugador1, avance1],
                [jugador2, avance2],
                [jugador3, avance3],
                [jugador4, avance4]]
        print (tabulate(tabla))
        lanzar = input('¿Desea lanzar los dados? S/N\r\n')
        
        if avance1 >= 20000 or avance2 >= 20000 or avance3 >= 20000 or avance4 >= 20000:
            break
        else:
            None

        if (lanzar == 'S'):
            dado = random.randint(1,6)
            print('El dado para el jugador 1 cayó en: ', dado)
            dado = int(dado)
            avance1 += dado * 100
            print (avance1)

            

        else:
            print ('Lamentamos que no quieras jugar. Hasta la próxima !!!')
            break