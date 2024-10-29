'''
Clases
'''

class ogPerson:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self): # self puede cambiar por lo que sea
    return f"Name: {self.name}({self.age})"
  def myfunc(self): #Igualmente aqui, pero ps, es como el this
    print("Hello my name is " + self.name)

p1 = ogPerson("John", 36)

print(p1)

'''
Herencia
'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")

class Student(Person):
    pass # Use the pass keyword when you do not want to add any other properties or methods to the class.


y= Student("Mike", "Olsen")
y.printname() 

class UniqueStudent(Person):
    #When you add the __init__() function, 
    #the child class will no longer inherit the parent's __init__() function.
  def __init__(self, fname, lname):
    #Note: The child's __init__() function overrides the inheritance of the parent's 
    # __init__() function.
    
    
    #To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
    Person.__init__(self, fname, lname) 
    #OR super() function that will make the child class inherit all the methods and properties from its parent:
    super().__init__(fname, lname) 
    
    # self.firstname = fname
    # self.lastname = lname
    

class StudentFormed(Person):
   def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 
    
z = StudentFormed("Mike", "Olsen", 2019) 
z.printname() 



'''
ITERACIONES
'''

'''
No es lo mismo interator a iterable
Las listas, tuplas, diccionarios, etc, son ITERABLES

'''
mytuple = ("apple", "banana", "cherry")

print("Por uso de iter method")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print("Por Loop")

for x in mytuple:
  print(x) 
#The for loop actually creates an iterator object and executes the next() method for each loop.

#Se debe de impelementar los metodos __iter__



class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

mynumclass = MyNumbers()
myiter = iter(mynumclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# Esto no lo hagas si no tienen algo para pararlo, pq va a repetirlo sin fin
#Al parecer se evita con un vil IF y ya
for x in mynumclass:
    print(x)



