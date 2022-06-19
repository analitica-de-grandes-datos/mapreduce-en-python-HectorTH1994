#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#! /usr/bin python3

import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    total = 0
    contador=1

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, val = line.split("\t")
        val=float(val)

        if key == curkey:
            
            total += val
            contador+=1
            
        else:
            #
            # Se cambio de clave. Se reinicia el acumulador.
            #
            if curkey is not None:
                #
                # una vez se han reducido todos los elementos
                # con la misma clave se imprime el resultado en
                # el flujo de salida
                #

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, total,total/contador))
            curkey = key
            total = val
            contador=1
            
        
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, total,total/contador))
