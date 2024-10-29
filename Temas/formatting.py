#Para revisar mejor el formateo : https://www.w3schools.com/python/python_string_formatting.asp 

price = 59
txt = f"The price is {price} dollars"
print(txt)
txt = f"The price is {price:.2f} dollars" 
print(txt)
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)


def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

price = 1159000
txt = f"The price is {price:,.2f} dollars"
print(txt)

#Se pueden pasar como argumentos en una funcion
price = 49
txt = "The price is {} dollars"

#Asi se aplican los estilos
#txt = "The price is {:.2f} dollars"


print(txt.format(price))



quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


#Darle orden a las variables
quantity = 3
itemno = 567
price = 49
myorder = "I want {1} pieces of item number {2} for {2:.2f} dollars."
print(myorder.format(itemno, quantity, price))    

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))