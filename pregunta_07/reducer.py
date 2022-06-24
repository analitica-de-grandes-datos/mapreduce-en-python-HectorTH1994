#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#! /usr/bin/python3

import sys
from operator import itemgetter, attrgetter
elements=[]

if __name__ == '__main__':

    def take_element(element):
        return int(element.split()[2])

    def take_word(element):
        return element.split()[0]
        
    for line in sys.stdin:
        elements.append(line)
    else:
        elements = sorted(elements, key = itemgetter(0,2))

        for element in elements:
            sys.stdout.write(element)
