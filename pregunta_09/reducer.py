#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#! /usr/bin/python3

import sys

elements=[]
letras=[]
elements2=[]
contador=0

if __name__ == '__main__':

    def take_element(element):
        return int(element.split()[2])

    def take_word(element):
        return element.split()[0]

    for line in sys.stdin:
        elements.append(line)

    else:
        elements = sorted(elements, key = take_element)

        for element in elements:
            if contador < 5:
                sys.stdout.write(element)
                contador+=1
