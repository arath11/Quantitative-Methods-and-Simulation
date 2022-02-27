def main():
    #asignar valores 
    a=5
    #c=7
    m=30
    #metodo de congruencia lineal
    formula(a,m,5)

def formula(a:float, m:float, s:int):
    semilla=s
    resultado=0
    for i in range(16):
        resultado=(a*semilla)%m
        print(f"n:{i} resultado: {resultado}")
        semilla=resultado
main()