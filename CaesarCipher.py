#By StaryDark    Telegram: Dark_Zly
"""
Version:1.0
Requisitos:
    Python3
    Libreria de Colorama
"""
from colorama import Fore, init
init()

#Funciones

def cifrar_caesar(input_user):
    """Toma un texto y lo devuelve un texto cifraco con el cifrado caesar"""

    abecedario = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']
    texto_cifrado = ""

    for element in input_user:

        if element in abecedario:
            index = abecedario.index(element)
            texto_cifrado = texto_cifrado + (abecedario[index + 3])
        else:
            texto_cifrado = texto_cifrado + element
    
    return texto_cifrado

def output_formatter(output):
    """ Impirmir en pantalla los resultados de forma bonita"""
    textfinal = (Fore.LIGHTYELLOW_EX + f"\nTexto Cifrado: " +Fore.LIGHTCYAN_EX + output) + "\n\n"
    print (textfinal)

def menu():
    """ Menu Principal"""
    menu = (Fore.LIGHTYELLOW_EX + """
   ____                             _____         _      ____ _       _               
  / ___|__ _  ___  ___  __ _ _ __  |_   _|____  _| |_   / ___(_)_ __ | |__   ___ _ __ 
 | |   / _` |/ _ \/ __|/ _` | '__|   | |/ _ \ \/ / __| | |   | | '_ \| '_ \ / _ \ '__|
 | |__| (_| |  __/\__ \ (_| | |      | |  __/>  <| |_  | |___| | |_) | | | |  __/ |   
  \____\__,_|\___||___/\__,_|_|      |_|\___/_/\_\\__|  \____|_| .__/|_| |_|\___|_|   
                                                               |_|                     
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                                    """ + Fore.RED + """\By: StaryDark\\""" + Fore.LIGHTYELLOW_EX + """
    
    Escribe el texto a cifrar:\n\n--->"""+ Fore.LIGHTCYAN_EX)
    return (menu)

def main ():
    """ Ejecucion Principal"""
    input_user = input(menu())
    output = cifrar_caesar(input_user)
    output_formatter(output)

main()