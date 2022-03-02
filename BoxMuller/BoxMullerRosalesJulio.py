#requerido 
#pip install matplotlib
import random 
import matplotlib.pyplot as plt
import math
import numpy


def main():
    arraySize=10000
    datos =[random.random() for i in range(arraySize)]
    segunda=[]
    for i in range(len(datos)-1):
        #sqrt(-2Ln*U1)*cos(2*pi*U2)
        segunda.append(math.sqrt(-2*numpy.log(datos[i]))*math.cos(2*math.pi*datos[i+1]))
        #sqrt(-2Ln*U1)*sin(2*pi*U2)
        segunda.append(math.sqrt(-2*numpy.log(datos[i]))*math.sin(2*math.pi*datos[i+1]))

    histograma(segunda,11)    

def histograma(arreglo,b:int):
    #llenar los datos en el histograma
    plt.hist(arreglo,bins=b)
    #imprimir 
    plt.show()

main()