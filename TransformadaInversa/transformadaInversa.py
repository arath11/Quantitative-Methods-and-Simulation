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
    lambd=1
    for i in range(len(datos)-1):
        #queremos exponencial asi que usamos la cdf que es la inversa de la exponencial 
        #sacamos la inversa de (1-e^-lambda*x) y da
        #x=-1/lambda*ln(1-y)
        datos[i]=-1/lambd*numpy.log(1-datos[i])
    
    histograma(datos,100)    

def histograma(arreglo,b:int):
    #llenar los datos en el histograma
    plt.hist(arreglo,bins=b)
    #imprimir 
    plt.show()

main()