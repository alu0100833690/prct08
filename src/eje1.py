#! /usr/bin/python
import modulo2

def error(n, v, u):
  err = 0.0
  for i in range(v):
    aprox1 = modulo2.f(n)
    aprox2 = modulo2.f(v)
    resultado = aprox1 - aprox2 
    if(abs(resultado)>=u):
      err += 1
  return(err/v)*100
  
if (__name__=="__main__"):
  import sys
  if((len(sys.argv) == 1) or (len(sys.argv) == 2) or (len(sys.argv) == 3)):
    print("No ha introducido todos los argumentos")
    n = 200
    v = 12
    u = 0.0000001
  else:
    n = int(sys.argv[1])
    v = int(sys.argv[2])
    u = float(sys.argv[3])
  print error(n, v, u)
