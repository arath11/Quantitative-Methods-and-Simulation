import random 
import winsound 
import time

#cadena valida 
cadenaMarkov=[[0.0,0.4,0.05,0.15,0.1,0.2,0.1],
                 [0.05,0.3,0.15,0.4,0.0,0.05,0.05],
                 [0.4,0.1,0.2,0.0,0.1,0.1,0.1],
                 [0.0,0.1,0.15,0.3,0.2,0.2,0.05],
                 [0.1,0.1,0.1,0.0,0.4,0.2,0.1],
                 [0.1,0.1,0.0,0.1,0.4,0.0,0.3],
                 [0.5,0.1,0.0,0.3,0.0,0.0,0.1]]

estrellita=[[0.5,0.0,0.0,0.0,0.5,0,0.0],
            [0.5,0.5,0.0,0.0,0.0,0.00,0.00],
            [0.4,0.1,0.2,0.0,0.1,0.1,0.1],
            [0.0,0.0,0.5,0.5,0.0,0.,0.00],
            [0.0,0.0,0.0,0.0,0.5,0.5,0.0],
            [0.1,0.1,0.0,0.1,0.4,0.0,0.3],
            [0.5,0.1,0.0,0.3,0.0,0.0,0.1]]

#130,138,146,155,164,174,184,195,207,220,233,246,
#261,277,283,311,329,349,369,391,415,440,466,493

cadenaSonido=[265,297,334,354,397,446,501]
def main(iteraciones):
    numeroIteraciones=iteraciones
    duracion=500
    siguiente=0#do
    for i in range(0,numeroIteraciones,1):
        #print(cadenaMarkov[siguiente])
        procesar(siguiente,cadenaSonido,duracion)
        #siguiente=do(siguiente,estrellita)
        siguiente=do(siguiente,cadenaMarkov)
        
        
def procesar(numero, tabla,duracion):
    print(numero)
    winsound.Beep(tabla[numero], duracion)
        

def do(q:int,tabla):
    azar=random.randint(0,1000)/1000
    #print(f"azar:\n{azar}\n")
    #print(f"q:{q}")
    inicial=0
    for i in range(len(tabla[q])):
        if azar >= inicial and azar<= inicial+tabla[q][i]:
            return i
        else:
            inicial=inicial+tabla[q][i]
    
def validarCadenas(tabla):
    valida=True
    for i in tabla:
        suma=0
        for j in i:
            suma+=j
        if 1.00000000000000005>suma>.9999999999999999999999999:
            print(f'Posicion:{i} da {suma}')
            valida=False
            
    return valida

main(100)
#print(validarCadenas(cadenaMarkov))
#print(validarCadenas(estrellita))

#cadenaMarkov=[[.4,.1,.5],[.8,.1,.1],[.2,.3,.5]]
#"Do","Re","Mi","Fa","Sol","La","Si"
#0044543322110
#do do sol sol la la sol fa fa mi mi re re do
#do do re re mi fa fa sol sol la la si do do re re mi fa fa sol sol la la si do 
    #winsound.PlaySound('bongo1.wav',winsound.SND_FILENAME)