#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#! /usr/bin/python3
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        for word in line.split()[0]:
            sys.stdout.write("{}\t1\n".format(word))
