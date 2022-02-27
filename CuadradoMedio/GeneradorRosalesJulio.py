import math

def main():
    #entradas
    semilla1=(int)(input("Inserte la semilla\n"))

    #checar 0
    if(semilla1!=0):
        multiplicacion=multiplicar(semilla1,semilla1)
#        print(multiplicacion)

        #encontrar el medio 
        valorMedio=medio(multiplicacion)
        if(valorMedio!=0):
            #valor izquierdo 
            print(valorIzquierdo(valorMedio,len(str(semilla1))))
        else:
            print(0)
        
    else:
        print(0)


def multiplicar(sem1,sem2):
    return sem1*sem2

def medio(num):
    #revisar el lenght
    tamaño=len((str)(num))
    primerPunto=math.ceil(tamaño/4)
    segundoPunto=math.ceil(3*tamaño/4)
    numero=str(num)
    #print(primerPunto)    
    #print(segundoPunto)   
    regreso=""
    for i in range(primerPunto-1,segundoPunto,1):
        regreso=regreso+numero[i]        
    return (int)(regreso)

def valorIzquierdo(num,tamaño):
    if len(str(num))==tamaño:
        return num
    else:
        numero=str(num)
        regreso=""
        for i in range(0,tamaño,1):
            regreso=regreso+numero[i]
        return (int)(regreso)
main()