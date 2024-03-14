def inverte_caractere(palavra:str):
  palavra_invertida = ""
  print(len(palavra))
  for indice in range(len(palavra)-1, -1, -1):
    palavra_invertida += palavra[indice]
  return palavra_invertida

inverte_caractere("roma")