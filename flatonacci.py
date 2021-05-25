from functools import reduce

def flatonacci(signature: list, n: int) -> list:
    # happy coding
  resultado = []
 
  try: 
    if type(n) != int:
      print('El dato ingresado '+str(n)+ 'es diferente a un numero entero')

    elif n < 0:
      print('El numero '+str(n)+' es negativo solo se premiten numeros enteros')
  
    else:
      for valores in signature:
        if type(valores) != int:
          print('El listado contiene un str o un numero que no es entero')
          return(resultado)
        else:
          resultado.append(valores)
          print(resultado)

      for i in range(n-3):
        resultado.append(reduce(lambda x,y: x+y, resultado[:-4:-1]))

      print(resultado)
      return resultado
    
  except ValueError as err:
    print(err)
    return[]
    

  
  
    