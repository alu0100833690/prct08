if (__name__=="__main__"):
  import sys
  if((len(sys.argv) == 1) or (len(sys.argv) == 2)):
    print("No ha introducido todos los argumentos")
    n = 200
    v = 12
  else:
    n = int(sys.argv[1])
    v = int(sys.argv[2])
    
  lista=[]
  for j in range (1, v+1):
   pi = f(j*n)
   lista = lista+[pi]
  print lista
