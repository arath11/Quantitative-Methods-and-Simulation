import math

def main():
    #entradas
    semilla1=(int)(input("Inserte la semilla1\n"))
    semilla2=(int)(input("Inserte la semilla2\n"))
    
    
    if(semilla1==0 or semilla2==0):
        return 0
    
    multiplicacion=multiplicar(semilla1,semilla2)
    #print(multiplicacion)
    #valor medio 
    valorMedio=medio(multiplicacion)
    if(valorMedio!=0):
        print(valorIzquierdo(valorMedio,len(str(semilla1))))
    #valor izquierdo

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


def multiplicar(sem1,sem2):
    return sem1*sem2

main()