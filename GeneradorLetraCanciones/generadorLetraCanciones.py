import markovify

def main(palabras:int):
    #leer archivo
    #texto = leerTxt('badbunny_letras.txt')
    texto = leerTxt('karolg_letras.txt')
    #quitar saltos de linea

    #texto=leerTxt('canciones.txt')
    #print(texto)
    text_model=textModel(texto)
    print(f'Imprimiendo___')
    for i in range(palabras):
        print(text_model.make_short_sentence(280))

def leerTxt(path):
    with open(path) as f:
        text = f.read()
    #print(text)
    return text

def textModel(texto):
    # Build the model.
    # text_model = markovify.Text(text)
    return markovify.NewlineText(texto)

main(10)