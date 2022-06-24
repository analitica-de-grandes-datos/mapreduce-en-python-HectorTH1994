#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#! /usr/bin/python3

import sys
elements=[]

if __name__ == '__main__':

    def take_element(element):
        return int(element.split()[2])
        
    for line in sys.stdin:
        elements.append(line)
    else:
        elements = sorted(elements, key = take_element)
        for element in elements:
            sys.stdout.write(element)
