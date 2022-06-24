#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#! /usr/bin/python3

import sys

elements=[]
letras=[]
elements2=[]

if __name__ == '__main__':

    def take_element(element):
        return int(element.split()[2])

    def take_word(element):
        return element.split()[0]

    for line in sys.stdin:
        elements.append(line)
    else:
        elements = sorted(elements, key = take_element)
    
        for linea in elements:
            letra = take_word(linea)
            
            if letra not in letras:
                letras.extend(letra+"\n")

        for letra in letras:
            for linea in elements:
                if letra == take_word(linea):
                    elements2.append(linea)

        for element in elements2:
            sys.stdout.write(element)
