def fibonacci(numero:int):
  n1 = 0
  n2 = 1
  n3 = 0
  print(str(n1) + ", " + str(n2) + ",", end=" ")
  while True:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(str(n3) + ",", end=" ")
    if(n3 == numero):
      return "{0} pertence a sequência.".format(numero)
    elif(numero < n3):
      return "{0} não pertence a sequência.".format(numero)

fibonacci(100)