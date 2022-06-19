#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

#! /usr/bin python3

# Esta es la funcion que mapea la entrada a parejas (clave, valor)
#
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    for line in sys.stdin:

        #
        # genera las tuplas palabra \tabulador 1
        # ya que es un conteo de palabras
        #
        word=line.split()[0]+"\t"+line.split()[2]
            #
            # escribe al flujo estandar de salida
            #
        sys.stdout.write("{}\n".format(word))
