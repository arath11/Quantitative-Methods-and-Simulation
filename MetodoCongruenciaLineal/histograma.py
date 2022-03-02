#requerido 
#pip install matplotlib
import random 
import matplotlib.pyplot as plt

def main():
    arraySize=10000
    #hacer arreglo
    datos =[random.random() for i in range(arraySize)]

    histograma(datos)

def histograma(data):
    print("enrto")
    plt.hist(data,bins=11)
    plt.show()

main()