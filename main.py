from pip._vendor.distlib.compat import raw_input
from funcoes import inverte, concatena

print("Informe um texto")

texto = raw_input()

texto = inverte.inversao(texto)

texto = concatena.concat(texto)

print(texto)