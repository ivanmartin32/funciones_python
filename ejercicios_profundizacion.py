#!/usr/bin/env python
'''
Funciones [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"

import random
from collections import Counter

def lista_de_tiro (valor_min, valor_max, cantidad_dados):
    lista = []
    for i in range(cantidad_dados):
        numero = random.randrange(valor_min, valor_max+1)
        lista.append(numero)
    return lista

def ordenar(valor_de_dados):
    valor_de_dados.sort()
    return valor_de_dados

def contar(valor_de_dados,valor_a_contar1,valor_a_contar2,
                        valor_a_contar3,valor_a_contar4,valor_a_contar5,
                        valor_a_contar6):
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0
    contador5 = 0
    contador6 = 0
    for i in range(len(valor_de_dados)):
        if valor_de_dados[i] == valor_a_contar1:
            contador1 += 1
        if valor_de_dados[i] == valor_a_contar2:
            contador2 += 1
        if valor_de_dados[i] == valor_a_contar3:
            contador3 += 1
        if valor_de_dados[i] == valor_a_contar4:
            contador4 += 1
        if valor_de_dados[i] == valor_a_contar5:
            contador5 += 1
        if valor_de_dados[i] == valor_a_contar6:
            contador6 += 1
    return contador1,contador2,contador3,contador4,contador5,contador6

def contar_dado(primer_tiro,elegir_numero_repetido):
    repetido = []
    for i in primer_tiro:
        if i == elegir_numero_repetido:
            repetido.append(elegir_numero_repetido)
    return repetido

def ej1():
    print('Comencemos a crear lo nuestro!')

    '''
    Cree un nuevo archivo el cual será su módulo que utilizará
    para resolver todos los ejercicios de está guía.
    En el módulo implemente todas las funciones que le fueron
    solicitadas en "ejercicios_clase":
    - promedio
    - lista_aleatoria
    - ordenar
    - contar

    Importe el módulo a este programa/documento para su uso
    en el resto de los ejercicios
    '''


def ej2():
    print("Jugando a los dados")

    '''
    Un dado común tiene 6 caras, 6 resultados posibles
    1 - 2 - 3 - 4 - 5 - 6

    Utilice la función "lista_aleatoria" para generar
    5 tiros de dados (una lista de 5 valores con resultados posibles
    de un dado)
    ejemplo, se tiraron 5 dados y los resultados de lista aleatoria
    se deben parecer a:
    [1, 2, 3, 2, 5]
    Cada valor representa el valor que sacó cada uno de los 5 dados

    
    1)
    Utilice la función "ordenar" para ordenar la lista
    de números generados.
    Imprimir en pantalla la lista ordenada
    '''
    numero_min = 1
    numero_max = 6
    cantidad_dados = 5

    valor_de_dados = lista_de_tiro(numero_min, numero_max, cantidad_dados)

    valor_ordenado = ordenar(valor_de_dados)

    print('El valor de los 5 dados arrojados y ordenados es', valor_ordenado)


def ej3():
    print("Jugando a los dados")

    '''
    Un dado común tiene 6 caras, 6 resultados posibles
    1 - 2 - 3 - 4 - 5 - 6

    Utilice la función "lista_aleatoria" para generar
    5 tiros de dados (una lista de 5 valores con resultados posibles
    de un dado)
    ejemplo, se tiraron 5 dados y los resultados de lista aleatoria
    se deben parecer a:
    [1, 2, 3, 2, 5]
    Cada valor representa el valor que sacó cada uno de los 5 dados

    1)
    Utilice la función "contar" para contar cuantas veces aparece:
    a - Cuantsa veces aparece el número 1 en su lista de dados tirados
    b - Cuantsa veces aparece el número 2 en su lista de dados tirados
    c - Cuantsa veces aparece el número 3 en su lista de dados tirados
    d - Cuantsa veces aparece el número 4 en su lista de dados tirados
    e - Cuantsa veces aparece el número 5 en su lista de dados tirados
    f - Cuantsa veces aparece el número 6 en su lista de dados tirados


    2)
    Utilice la función de Python max con la key de list.count para
    determinar cual fue el número que más se repitió. Consultar los ejemplos
    vistos en clase para ver como se implementa max con esa key

    '''
    numero_min = 1
    numero_max = 6
    cantidad_dados = 5
    valor_a_contar1 = 1
    valor_a_contar2 = 2
    valor_a_contar3 = 3
    valor_a_contar4 = 4
    valor_a_contar5 = 5
    valor_a_contar6 = 6

    valor_de_dados = lista_de_tiro(numero_min, numero_max, cantidad_dados)
    
    (contar_numero1,contar_numero2,
    contar_numero3,contar_numero4,
    contar_numero5,contar_numero6) = contar(valor_de_dados,valor_a_contar1,valor_a_contar2,
                                            valor_a_contar3,valor_a_contar4,valor_a_contar5,
                                            valor_a_contar6)

    print('La cantidad de veces que aparece el numero 1 es:', contar_numero1)
    print('La cantidad de veces que aparece el numero 2 es:', contar_numero2)
    print('La cantidad de veces que aparece el numero 3 es:', contar_numero3)
    print('La cantidad de veces que aparece el numero 4 es:', contar_numero4)
    print('La cantidad de veces que aparece el numero 5 es:', contar_numero5)
    print('La cantidad de veces que aparece el numero 6 es:', contar_numero6)

    print('El valor mas repetido es el:', max(set(valor_de_dados), key=valor_de_dados.count))

def ej4():
    print("Ahora sí! buena suerte :)")

    '''
    Este ejercicio representa ya un problema que forma parte de un juego
    Lo que se desea realizar es una parte del juego "la generala".
    El enunciado está armado a modo de guía, pueden resolver el problemla
    de otra forma.
    Si tienen dudas sobre el enunciado o alguno de los puntos por favor
    comuníquelo por el campus y lo discutiremos entre todos, ya que siempre
    puede haber varias interpretaciones de un mismo enunciado.

    Deberá realizar una lista para guardar 5 dados, guardar los números
    sacados en esa tirada de de dados (son 5 números del 1 al 6)

    1) El jugador tira la dados y sacar 5 números aleatorios, puede usar
    la función de "lista_aleatoria" para generar dichos números.'''

    numero_min = 1
    numero_max = 6
    cantidad_dados = 5

    primer_tiro = lista_de_tiro(numero_min,numero_max,cantidad_dados)
    print('Los numeros del primer tiro son:', primer_tiro)

    '''
    2) Luego debe analizar los 5 números y ver cual es el número que
    más se repitio entre los 5 dados.
    Debe usar la función de Python max con la key de list.count paara
    determinar cual fue el número que más se repitió. Consultar los ejemplos
    vistos en clase o el ejercicio anterior de esta guia.
    '''
    
    elegir_numero_repetido = max(set(primer_tiro), key=primer_tiro.count)
    print('El numero elegido es el', elegir_numero_repetido)
    
    '''
    3) Una vez reconocido el número más repetido entre los 5, debe
    guardar en una lista esos números.
    Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4"
    Debe extrarlos de la lista, quedándole una lista separada
    dados_guardados = [4,4,4]
    Debe realizar un bucle para recorrer la lista de dados_tirados
    y guardar los "4" en nuestra nueva lista dados_guardados
    Utilie append para ir sumando a dados_guardados los valores
    '''
    dados_guardados = contar_dado(primer_tiro,elegir_numero_repetido)
    
    print('Dado/s guardado/s', dados_guardados)
    
    '''
    4) Debe volver a tira los dados, generar nuevos
    números aleatorios.
    Si en la lista "dados_guardados" tengo 3 dados guardados
    significa que ahora deberé tirar dos dados. Puede usar la función
    "len" para ver cuantos elementos hay en "dados_guardados"
    Es decir que en este caso debería generar dos números
    aleatorios nuevos con "lista_generica"
    Ahora tendré una nueva lista de "dados_tirados" en este caso
    de dos nuevos números aleatorios entre 1 y 6 representando a los dados
    tirados.
    '''
    
    cantidad_dados = cantidad_dados - len(dados_guardados)

    conteo_tiros = 1
    
    while len(dados_guardados) < 5:

        otro_tiro = lista_de_tiro(numero_min,numero_max,cantidad_dados)

        conteo_tiros += 1 # Agregue un contador de tiros
        
        print('Dado/s arrojado/s', otro_tiro)

        for i in otro_tiro:
            if i == elegir_numero_repetido:
                dados_guardados.append(elegir_numero_repetido)
                cantidad_dados -= 1
                print('Dado/s guardado/s', dados_guardados)
    
    print('La cantidad de veces que se tiraron los dados es de:', conteo_tiros)   

    '''
    5) Luego de tirar nuevamente los datos, por ejemplo digamos
    que salieron los números: 4-1
    Debo volver a quedarme con el "4" ya que es el número que estoy
    buscando.
    Sino salió el "4" vuelvo a tirar todos los dados.
    Si salió un "4" me lo quedo y lo guardo en "dados_guardados".
    '''
        
    '''
   5) Debe repetir este proceso hasta que en su lista de "dados
   guardados" tenga "generala", es decir, 5 números iguales.

   ''' 

if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
