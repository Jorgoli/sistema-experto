import json
import os

#Sección para definir las funciones de imprimir colores.
def prRed(text): print("\033[91m{}\033[00m" .format(text))
def prGreen(text): print("\033[92m{}\033[00m" .format(text))
def prYellow(text): print("\033[93m{}\033[00m" .format(text))
def prLightPurple(text): print("\033[94m{}\033[00m" .format(text))
def prPurple(text): print("\033[95m{}\033[00m" .format(text))
def prCyan(text): print("\033[96m{}\033[00m" .format(text))
def prLightGray(text): print("\033[97m{}\033[00m" .format(text))
def prBlack(text): print("\033[98m{}\033[00m" .format(text))

#Definir la función clear nos ayuda a limpiar la consola
clear = lambda: os.system('cls')
clear()

#Se abren y guardan los 3 archivos relevantes para la base de conocimientos como utf-8 para respetar acentos
colorsFile = open('colors.json', 'r', encoding='utf-8')
questionsFile = open('questions.json', 'r', encoding='utf-8')
birdsFile = open('birds.json', 'r', encoding='utf-8')

#Se convierten los archivos de la base de conocimientos a JSON o diccionarios
birds = json.load(birdsFile)
answers = json.load(colorsFile)
questions = json.load(questionsFile)

#Bienvenida
def greeting():
    prCyan("¡Bienvenido al clasificador de aves!")
    prPurple("Para elegir una respuesta a una pregunta, solo escribe el número de la opción deseada y presiona enter")

#Funcion principal
def __main__():
    clear()
    greeting()
    
    #Ave inicial vacía
    matchBird = {
        "ojos": "",
        "pico": "",
        "tarsos": "",
        "patas": "",
        "corona": "",
        "garganta": "",
        "vientre": "",
        "alas": "",
        "cola": "",
        "pecho": "",
        "cuerpo": "",
        "cabeza": "",
        "plumas": "",
        "frente": ""
    }
    
    #Se imprimen todas las preguntas y todas las respuestas posibles. Se obtiene una respuesta y se guarda en el ave vacía
    #Esta es la interfaz de usuario
    for question in questions:
        prLightGray(question['question'])

        for i in range(0, len(answers)):
            print("\033[93m {}\033[00m".format(str(i + 1)), '-' ,answers[i]['name'])

        res = int(input("\033[97m{}\033[00m" .format('Elige tu respuesta: '))) - 1
        matchBird[question['char']] = answers[res]['name']
        clear()
        
    foundFlag = True
    foundBird = None

    #Aquí se busca si algún ave de la base de conocimientos cumple con todas las características entradas arriba en un modelo SI-ENTONCES
    #Este es el motor de inferencia
    for bird in birds:
        foundFlag = True
        for attr, value in matchBird.items():
            if bird[attr] != value:
                foundFlag = False
                break
        if foundFlag == True:
            foundBird = bird
            break

    clear()

    #Si no se encuentra un ave ya guardada, se pide indicar si se desea agregar a la base de conocimientos
    #Este es el módulo de aprendizaje
    if foundFlag == False:
        prRed("Desafortunadamente el ave descrita no fue encontrada :(")

        for attr, value in matchBird.items():
            print("\033[95m{}\033[00m".format(attr.capitalize()) + ": " + "\033[97m{}\033[00m".format(value))
            
        res = input("\033[97m{}\033[00m" .format('Deseas agregar una nueva ave con estas características? (y/n): '))

        #Si se quiso agregar, se le da un nombre y descripción, despues se guarda en el arreglo de aves existentes y se escribe en el archivo existente
        if res == 'y':
            nombre = input("\033[95m{}\033[00m".format('Cuál es el nombre de la ave a agregar?: '))
            matchBird['nombre'] = nombre

            desc = input("\033[95m{}\033[00m".format('Escribe una corta descripción del ave: '))
            matchBird['descripcion'] = desc

            matchBird['id'] = len(birds) + 1

            birds.append(matchBird)
            birdsToWrite = json.dumps(birds, indent=4)

            with open("birds.json", "w", encoding='utf-8') as outfile:
                outfile.write(birdsToWrite)
            
            prGreen("¡Ave agregada!")
            prCyan("¡Hasta luego!")
        #Si no se desea agregar, se termina el programa
        else:
            prCyan("¡Hasta luego!")

    #Si se encontró un ave ya guardada, se muestra el nombre y su descripción
    #Este es el módulo de explicaciones
    else:    
        prGreen("¡Ave encontrada con las siguientes características!")

        for attr, value in matchBird.items():
            print("\033[95m{}\033[00m".format(attr.capitalize()) + ": " + "\033[97m{}\033[00m".format(value))

        print('\nNombre: ' + foundBird['nombre'])
        print('Descripción: ' + foundBird['descripcion'])
        prCyan("¡Hasta luego!")

if True:
    __main__()
