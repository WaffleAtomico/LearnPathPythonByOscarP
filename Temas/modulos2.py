import platform
#Este lo vamos a usar luego para manejo de archivos
import datetime

import math

import json 

import re


x = platform.system()
print(x)    
# x = dir(platform)
# print(x) 

x = datetime.datetime.now()
print(x) 
print(x.year)
print(x.strftime("%A"))


x = datetime.datetime(2020, 5, 17)
print(x)

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B")) 

#Revisar https://www.w3schools.com/python/python_datetime.asp
#Para mejores referencias de metodos o valores que puede tomar strftime


'''
MATEMATICAS
'''

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y) 

x = abs(-7.25)
print(x) 

x = pow(4, 2) #4^3
print(x) 

x = math.sqrt(64)
print(x) 

'''json to python (Make a dicctionary)'''
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print(y["age"]) 

'''python to json'''

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y) 



x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print(json.dumps(x, indent=4, sort_keys=True))


txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) 
print(x)
'''
findall 	Returns a list containing all matches
search 	Returns a Match object if there is a match anywhere in the string
split 	Returns a list where the string has been split at each match 
sub 	Replaces one or many matches with a string

Metacharacters & Special Sequences & Sets
https://www.w3schools.com/python/python_regex.asp
For more info about
'''

#The split() function returns a list where the string has been split at each match:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) 
#You can control the number of occurrences by specifying the maxsplit parameter:
x = re.split("\s", txt, 1)
print(x)

#The sub() function replaces the matches with the text of your choice:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x) 
nuevo_txt = re.sub(r"[aeiouAEIOU]", "i", txt)
print(nuevo_txt)

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
  
  