#requerido 
#pip install matplotlib
import random 
import matplotlib.pyplot as plt

def main():
    arraySize=10000
    #hacer arreglo
    arreglo =[random.randint(0,10) for i in range(arraySize)]

    plt.hist(arreglo,bins=11)
    plt.show()

main()