from funcoes import encripta

def concat(texto):
    tam = len(texto)
    controle = 0
    controle2 = 2
    junta = ""

    for i in range(0, tam):
        cifra = encripta.encripta()
        texto2 = texto[controle, controle2]
        junta = junta + texto2 + cifra

        controle = controle + 2
        controle2 = controle2 + 2


        return junta