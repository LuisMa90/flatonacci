from functools import reduce

def flatonacci(signature: list, n: int) -> list:
    # happy coding
  resultado = []
 
  try: 
    if type(n) != int or  n < 0 or len(signature) != 3:
      print('N no es un numero entero o signature no contiene 3 elementos')

    else:
      for valores in signature:
        if type(valores) != int:
          print('El valor de signature contiene un str o un numero que no es entero')
          return(resultado)
        else:
          resultado.append(valores)
      
      if n == 0:
        resultado = [] 
      else:
        for i in range(n-3):
          resultado.append(reduce(lambda x,y: x+y, resultado[:-4:-1]))

      print(resultado)
      return resultado
    
  except ValueError as err:
    print(err)
    return[]