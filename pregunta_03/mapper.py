#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#


# reference https://docs.python.org/3/howto/sorting.html
import sys

elements = []

def take_element(element):
    return element.split(",")[0]

for row in sys.stdin:
    elements.append(row)
else:
    elements = sorted(elements, key = take_element)
    
    for element in elements:
        sys.stdout.write(element)
