def main():
    #asignar valores 
    #a=1
    #c=7
    #m=13
    #metodo de congruencia lineal
    #formula(a,c,m,7)

    a=1
    c=1000
    m=10000
    #metodo de congruencia lineal
    formula(a,c,m,5)

def formula(a:float, c:float, m:float, s:int):
    semilla=s
    resultado=0
    for i in range(16):
        resultado=(a*semilla+c)%m
        print(f"n:{i} resultado: {resultado}")
        semilla=resultado
main()