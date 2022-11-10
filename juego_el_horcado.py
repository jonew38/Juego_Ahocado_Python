
from calendar import c
import numbers
import os
import random
from re import I


def aleatorio(word_select):
    with open("./archivos/data.txt", "r", encoding= "utf-8") as f:
        word_aleatorio = [ word for word in f ]
        word_aleatorio = list(map(str.rstrip, word_aleatorio))
        word_select = random.choices(word_aleatorio)
        return word_select


def run():
    word = aleatorio(word_select=())
    for i, l in enumerate(word):
        lista_pat = list(l)
        pista = ["_"]*len(l)
        pista2 = dict(zip(l,lista_pat))
    while word != pista:
        print ("JUEGO DEL HORCADO","\n""!ADIVINA LA PALABRA!", "\n",f" ".join(pista),"\n")
        if lista_pat == pista:
            print("Ganastes")
            break
        try:
            lec = str(input("Escribe una letra: "))
            if lec == numbers:
                raise ValueError("No debe ser un numero")
        except ValueError as error:
                print(error)
        letras = pista2.get(lec)
        if letras == lec:
            letter = [i for i, lec in enumerate(lista_pat) if lec==letras ]
            for i in letter:
                if i >= 0:
                    pista[i]=lec
                
        else:
            print("Sigue Intentando")
        os.system("cls")
    return letras




if __name__=="__main__":
    run()