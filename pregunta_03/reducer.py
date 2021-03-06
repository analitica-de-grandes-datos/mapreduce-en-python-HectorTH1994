#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
# reference https://docs.python.org/3/howto/sorting.html
#! /usr/bin/python3
import sys
elements = []
if __name__ == '__main__':

    def take_element(element):
        return element.split(",")[1]
    for line in sys.stdin:
        elements.append(line)
    else:
        elements = sorted(elements, key = take_element)
        for element in elements:
            sys.stdout.write(element)
