# arbol = 1
try:
  print(arbol)
except NameError:
  print("X not declared")
except:
  print("An exception ocurred")
#Como arbol no esta definido, da error
else:
  print("Nel no paso un error")
finally:
  print("The 'try except' is finished") 
  
  
  
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file") 


'''EXCEPTIONS'''

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero") 

try:
  
  x = "hello"

  if not type(x) is int:
    raise TypeError("Only integers are allowed") 
except:
  print("Cache el error generado por mi")
  
  