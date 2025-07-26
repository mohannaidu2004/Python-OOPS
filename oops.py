#Class Creation , access class through odject
class dog:
  def features(self):
    print("German shepard")
    print("Austria")

animal = dog()
animal.features()

#passing parameters to a class
class person:
  def set_name(self,name):
    self.name = name
  def get_name(self):
    return self.name
p = person()
p.set_name("krishna")
print(p.get_name())

#mathematical operations
class calc:
  def add(self,a,b):
    return a+b
  def sub(self,a,b):
    return a-b
c = calc()
print(c.add(5,6))
print(c.sub(10,5))

#Using same parameters for all the def's using self
class calc:
  def set_values(self,a,b):
    self.a = a
    self.b = b
  def add(self):
    return self.a+self.b
  def sub(self):
    return self.a-self.b
  def mul(self):
    return self.a*self.b
c = calc()
c.set_values(5,6)
print(c.add())
print(c.sub())
print(c.mul())

#cal area and circumference of a circle
class circle:
  def set_values(self,r):
    self.r=r
  def area(self):
    return 3.14*self.r**2
  def circumference(self):
    return 2*3.14*self.r
c= circle()
r=int(input("Enter the radius : "))
c.set_values(r)
print("Area :",c.area())
print("Circumference:",c.circumference())

#cal pythogorum problem
import math
class pyt:
  def set_values(self,a,b):
    self.a=a
    self.b=b
  def cal(self):
    return math.sqrt(self.a**2+self.b**2)
p=pyt()
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
p.set_values(a,b)
print(p.cal())

#usage of __init__:
class person:
  def __init__(self,name,height,weight):
    self.name=name
    self.height=height
    self.weight=weight
p=person("krishna",5.11,70)
print(p.name,p.height,p.weight)

#Default parameters
class book:
  def __init__(self,title,author="Unknown",year= 2000):
    self.title=title
    self.author=author
    self.year=year
b1 = book("CNS")
b2 = book("CC","Sai",2025)
print(b1.title,b1.author,b1.year)
print(b2.title,b2.author,b2.year)

# List or collections through the class
class shopping:
  def __init__(self):
    self.items= []
  def add_items(self,item):
    self.items.append(item)
  def remove_items(self,item):
    self.items.remove(item)
  def show_items(self):
    for item in self.items:
      print(item)
cart = shopping()
print("1. Add items , 2. remove items , 3. show items")
res=int(input("Enter your choice : "))
while res!=0:
  if res==1:
    res1=int(input("Enter the number of items : "))
    for i in range(res1):
      item=input("Enter the item : ")
      ecart.add_items(item)
  elif res==2:
    print("added items")
    print(cart.show_items())
    item=input("Enter the item : ")
    cart.remove_items(item)
  elif res==3:
    print(cart.show_items())

#class with direct
class student:
  def __init__(self,name):
    self.name=name
    self.grades={}
  def add_grades(self,subject,grade):
    self.grades[subject]=grade
s=student("krishna")
s.add_grades("math",90)
s.add_grades("science",95)
print(s.name)
print(s.grades)

#code for the del method --- __del__()
class abc():
  classvar =0
  def __init__(self,var):
    abc.classvar+=1
    self.var=var
    print("the object value is:",self.var)
    print("the value of class variable is :",abc.classvar)
  def __del__(self):
    abc.classvar-=1
    print("object with value %d is going out of scope" %self.var)
obj1=abc(10)
obj2=abc(20)
obj3=abc(30)
del obj1
del obj2
del obj3

# number operations to perform simple arthemetic operations by class and delete the call
class numpos:
  def __init__(self,a,b):
    self.a=a
    self.b=b
    print(f"initialized with a={a} and b={b}")
  def add(self):
    return self.a+self.b
  def sub(self):
    return self.a-self.b
  def mul(self):
    return self.a*self.b
  def div(self):
    if self.a!=0:
      return self.a/self.b
    else:
      print("Divide by zerq error!!!")
  def __del__(self):
    print(f"deleting obj with a={self.a} and b={self.b}")
n1= int(input("Enter the value of a : "))
n2= int(input("Enter the value of b : "))
op=numpos(n1,n2)
print("Addition :",op.add())
print("Subtraction :",op.sub())
print("Multiplication :",op.mul())
print("Division :",op.div())
del op

# get item and set item using a list
class nums:
  def __init__(self,mylist):
    self.mylist = mylist
  def __getitem__(self, index):
    return self.mylist[index]
  def __setitem__(self, index , value):
    self.mylist[index]= value
numlist= nums([10,20,30,40,50])
print(numlist[2])
numlist[2]=60
print(numlist.mylist)

# public and private variables
class abc():
  def __init__(self,v1,v2):
    self.v1 = v1
    self.__v2 = v2
  def display (self):
    print("from class method , var1=",self.v1)
    print("from class method , var2=",self.__v2)
obj = abc(1,2)
obj.display()
print("from class method , var1=",obj.v1)
print("from class method , var2=",obj.__v2)

'''code that uses a class to store the name and marks of a student use a list to store the marks of 3 bubjects.
1. create a class student
2. create a function in the class with in the range of three subjects
3. take manual inputs of the marks to be apprehended in the list
4. display the name of the student along with marks in a list'''

class student:
  def __init__(self,name):
    self.name=name
    self.marks=[]
  def entermarks(self):
    for i in range(3):
      m=int(input("enter the marks of %s in the subject %d"%(self.name , i+1)))
      self.marks.append(m)
  def showmarks(self):
    print(f"{self.name} got following marks{self.marks}")
n=input('enter 1st name:')
s1=student(n)
s1.entermarks()
n2=input('enter 2st name:')
s2=student(n2)
s2.entermarks()
s1.showmarks()
s2.showmarks()

# inheritance multiple
# create a super class from a constructor and call the base class
class base1(object):
  def __init__(self):
    super(base1, self).__init__()
    print("Base class-1")
class base2(object):
  def __init__(self):
    super(base2, self).__init__()
    print("Base class-2")
class base3(object):
  def __init__(self):
    super(base3, self).__init__()
    print("Base class-3")
class derived(base1,base3,base2):
  def __init__(self):
    super(derived, self).__init__()
    print("Derived class")
d= derived()

''' code to inherit add() from addition base and sub() from subtract base and create a own multiply in the derived
class of calc pass the values for the obj to the class of inheritence multiply
num1 = 10
num2 =5


'''

class addition:
  def add(self,a,b):
    return a+b
class subtract:
  def sub(self,a,b):
    return a-b
class calc(addition,subtract):
  def mul(self,a,b):
    return a*b
c = calc()
n1= int(input("Enter the value of a : "))
n2= int(input("Enter the value of b : "))
print("Addition:",c.add(n1,n2))
print("Difference:",c.sub(n1,n2))
print("Product:",c.mul(n1,n2))

''' import math for claculating sq.cube by multiple inheritence and summate the both'''

import math
class square:
  def sqt(self,a):
    return math.pow(a,2)
class cube:
  def cb(self,b):
    return math.pow(b,3)
class calc(square,cube):
  def summate(self,a,b):
    return self.sqt(a)+self.cb(b)
c = calc()
n1= int(input("Enter the value of a : "))
n2= int(input("Enter the value of b : "))
print("Summation:",c.summate(n1,n2))

class levels:      #base class
  def name(self):
    print("one")
class step(levels): #class derived from levels
  def help(slef):
    print("two")
class run(step):
  def take(self):
    print("three")
a = run()
a.name()
a.help()
a.take()

class square:
  def square (self, num):
    return num**2
class cube(square):
  def cube (self , num):
    return num**3
class Total(cube):
  def total(self, num):
    sq = self.square(num)
    cu = self.cube(num)
    return sq+cu
calc = Total()
n = int ( input("enter the value of n:"))
print("Number:",n)
print("Square:",calc.square(n))
print("Cube:",calc.cube(n))
print("Total:",calc.total(n))

# abstract methodology
from abc import ABC, abstractmethod
import abc
class vehicle(ABC): #abstract method
  def move(self): #subclasses implementation by abstarct method
    pass
  def stop(self): #method shared my all subclasses
    return "stopped !!!"
class car(vehicle):
  def move(self):
    return "Drives on the road!!!!"
class boat(vehicle):
  def move(self):
    return "sail on water!!!!"
car = car()
boat = boat()
print(car.move())
print(boat.move())
print(car.stop())
print(boat.stop())

from abc import ABC, abstractmethod
class animal(ABC):
  def sound(self):
    pass
  def sleep(self):
    return "Zzzzzz......"
class dog(animal):
  def sound(self):
    return "Bark..."
class cat(animal):
  def sound(self):
    return "meow..."
dog = dog()
cat = cat()
print("Dog",dog.sound())
print("Dog",dog.sleep())
print("Cat",cat.sound())
print("Cat",cat.sleep())

''' create a abstaract method for deifferent shapes to calculte the area of the respective shapes through concrete subclasses . return the values by passing different args
circle: pass 5 as radius
square: pass 4 as side '''
from abc import ABC, abstractmethod
class area (ABC):
  def square(self,side):
    return side**2
  def circle(self,radius):
    return 3.14*radius**2
class square(area):
  def area(self,side):
    return self.square(side)
class circle(area):
  def area(self,radius):
    return self.circle(radius)
s = int(input("Enter squre Side length:"))
r = int(input("Enter Radius of circle:"))
sq = square()
cr = circle()
print("Square area:",sq.area(s))
print("Circle area:",cr.area(r))

''' create a abstaract method for deifferent shapes to calculte the area of the respective shapes through concrete subclasses . return the values by passing different args
circle: pass 5 as radius
square: pass 4 as side '''
from abc import ABC, abstractmethod
class shape (ABC):
  def area(self):
    pass
class square(shape):
  def __init__(self,side):
    self.side = side
  def area(self):
    return self.side**2
class circle(shape):
  def __init__(self,radius):
    self.radius = radius
  def area(self):
    return 3.14*self.radius**2
s = int(input("Enter squre Side length:"))
r = int(input("Enter Radius of circle:"))
sq = square(s)
cr = circle(r)
print("Square area:",sq.area())
print("Circle area:",cr.area())

#math operations using abstract method with subclasses of arthemetic ops
from abc import ABC, abstractmethod
class op(ABC):
  def cal(a,b):
    pass
  def gen(self):
    return " This is a sample math operarions, when ever you call it will work "
class addition(op):
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def cal(self):
    return self.a+self.b
class subtraction(op):
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def cal(self):
    return self.a-self.b
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
add=addition(a,b)
sub=subtraction(a,b)
print(add.gen())
print(add.cal())
print(sub.gen())
print(sub.cal())

#simple overloading
def name(str= 'ajay'):
  print('hello',str)
name()
name('vijay')

# *args with numbers
def abc(*args):
  return sum(args)
print(abc(1,2,3,4,5))

#operators overloading
class val:
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def __add__(self,other):
    return self.a+other.a,self.b+other.b
v1=val(1,2)
v2=val(3,4)
print(v1+v2)

'''program to add two complex numbers using method overload and print the total the imaginary and real number
a=1+2i
b=3+4i
output=4+6i
'''
class complex:
  def __init__(self,r=0,i=0):
    self.r=r
    self.i=i
  def __add__

#over-riding method in a sub class
class vehicle:
  def start(self):
    print("vehicle is starting !")
class car(vehicle):
  def start(self):
    print("car is starting !")
class bike(vehicle):
  def start(self):
    print("Bike is strating !")
v = vehicle()
c = car()
b = bike()
v.start()
c.start()
b.start()

''' over-riding , calling superclass attributes program to caliculate the area of circle by method overriding by calling the superclass function. '''
class shape:
  def area(self):
    print("Deploy area of circle")
class circle(shape):
  def area(self):
    print("Calculating")
    super().area()
c = circle()
c.area()

#passing the args and return values
'''program to pass args of salaries of different esignated employees from a super class to sub classes ake super
class as employee and derived class as manager and developper accordingly and pass the amount with 10% and 20% bonus '''
class employee:
  def salary(self,cash):
    print(f" Employee salary is {cash}")
class manager(employee):
  def salary(self,cash):
    print(f" Manager salary is", round(cash*1.1))
class developer(employee):
  def salary(self,cash):
    print(f" Developer salary is", round(cash*1.2))
e = employee()
m = manager()
d = developer()
e.salary(50000)
m.salary(50000)
d.salary(50000)

class person():
  def hi(self):
    return "Hello, How are ya !!!"
class friend(person):
  def hi(self):
    return "Hello, How are ya frnd !!!"
class stranger(person):
  def hi(self):
    return "Hello, How are ya str !!!"

p = person()
f = friend()
s = stranger()
print(p.hi())
print(f.hi())
print(s.hi())

# map function split function-

#write a program to cal the factorial and poower of given numbers by creating the nested loop with in loop where a= 5 and b= 3 cal factorial for a and cal power for 5**3

def task():
  a = 5
  b = 3
  fact = 1
  for i in range(1, a + 1):
    fact *= i
  power = 1
  for i in range(b):
    temp = 0
    for j in range(a):
      temp += power
    power = temp
  print(f"Factorial of {a} is: {fact}")
  print(f"{a} to the power of {b} is: {power}")
task()

'''Recursion:function calling without condition'''

#linear / head
def hrec(n):
  if n==0:
    return
  print(n)
  hrec(n-1)
n=int(input("Enter the value of n:"))
hrec(n)

#linear / head
def hrec(n):
  if n==0:
    return
  hrec(n-1)
  print(n)
n=int(input("Enter the value of n:"))
hrec(n)

#linear recursion factorial
def fact(n):
  if n==0:
    return 1
  return n*fact(n-1)
num=int(input("enter a num:"))
print('factorial:',fact(num))

#linear recursion sum of n numbers
def summ(n):
  if n==1:
    return 1
  return n+summ(n-1)
num=int(input("enter a num:"))
print('sum:',summ(num))

num=1
summ= num//2
print(summ)

#indirect function
def func1(n):
  if n <= 0:
    return
  print("Inside func1:", n)
  func2(n - 1)

def func2(n):
  if n <= 0:
    return
  print("Inside func2:", n)
  func1(n//2)

func1(5)

#write a code to check the given num is even or odd using indirect recursive function with boolean output
#input:5
#output:

def first(n):
  if n==0:
    return True
  return second(n-1)
def second(n):
  if n==0:
    return False
  return first(n-1)

num= int(input("Enter Num:"))
first(num)

def fibonacci_tree(n):
  if n <= 1:
    return n
  else:
    return fibonacci_tree(n - 1) + fibonacci_tree(n - 2)

num = 6
print(f"Fibonacci sequence up to {num} using tree recursion:")
for i in range(num):
  print(fibonacci_tree(i))

def nest(n):
  if n>=10:
    return n-1
  return nest(nest(n+2))
print(nest(2))

'''I/O Operations functions:

r -
rb -
r+ -
rb+ -
w -
wb -
w+ -
wb+ -
a -'''

#Reading data
with open('notes.txt','r') as file:
    data=file.read()
    print("Accessed from outsource:",data)

#Writing  data
with open('data.txt','a') as file:
  file.write("Helloo! \n")
  file.write("Helloo! \n")
  file.write("mohan \n")

with open('data.txt','r+') as file:
  data= file.read()
  file.seek(0)
  print(file.read())

with open ('data.txt','r')as file:
  lines=file.readlines()
  print("Lines list: ", lines)
  print(file.readline(200))
  file.close()
  print(file.closed)

num = int(input("Enter Numerator:"))
deno = int(input("Enter Denominator:"))
try:
  print(num/deno)
except ZeroDivisionError:
  print("Denominator cannot be zero")

print("="*50)

try:
  file = open('file.txt')
  str= file.readline()
  print(str)
except IOError:
  print("Error occured due to input!")
except ValueError:
  print("coudnt ")

#assertion
c=int(input("enter the temp in c :"))
f = (c*9/5)+32
assert(f<=32), "Its frezzing"
print("Temperature in fahrentheit:",f)

#write a program that prompts the user to enter a number and print its square perform exceptional handling for keyboard interrupt
n=0
while True:
  try:
    n=n+1
    if n==31:
      raise StopIteration
  except StopIteration:
    break
  else:
    print(n, end=" ")

try:
  size= int(input("enter size:"))
  user_list=[]
  for i in range(size):
    val= int(input(f"Enter element:"))
    user_list.append(val)
  index= int(input("Enter Index to access elements: "))
  print("Element at index",index,"is",user_list[index])
except ValueError:
  print("Error: please enter a valid integer")
except IndexError:
  print("Error: Index....")

print([num**2 for num in range(1,11)])
print([x for x in range(1,11) if x%2==0])

rows = int(input("Enter the number of rows: "))
patterns= [([chr(97+j) for j in range(i)]) for i in range(1, rows+1)]
for line in patterns:
  print(' '.join(line).upper())

rows = int(input("Enter the number of rows: "))
patterns= [([chr(97+j) for j in range(i)]) for i in range(1, rows+1)]
for line in patterns:
  print(' '.join(line).upper())

rows= int(input("Enter rows:"))
pattern= [(' ' * (rows-i)+'*'*(2*i-1)) for i in range(1, rows+1)]
for line in pattern:
          print(line)

rows= int(input("Enter rows:"))
pattern= [''.join([str(num) for num in range(1, rows-i+1)]) for i in range(rows)]
for line in pattern:
  print(line)

n= int(input("Enter rows:"))
pattern= [['*' if i==0 or i==n-1 or j==0 or j==n-1 or i==j or j==i else ' ' for i in range(n)] for j in range(n)]
for i in pattern:
          print(" ".join(i))

n= int(input("Enter rows:"))
upper=[' '*(n-i)+''.join('*' if j==0 or j==2*i else ' ' for j in range(2*i+1)) for i in range(n)]
lower=[' '* (i+2)+''.join('*' if j==0 or j==2*(n-i-2) else ' ' for j in range(2*(n-i)*1)) for i in range(n-1)]
for line in upper+lower:
  print(line)

def add(a,b):
  return a+b
def sub(a,b):
  return a-b
add(1,2)
sub(4,8)

class abc:
  value=9
  def display(self):
    print("This is a CLASS method")
obj1= abc()
print(obj1.value)
obj1.display()

class abc:
  def __init__(self, value):
    print("this is a class method")
    self.value=value
    print("Accessed value in class is", self.value)
num= int(input("Enter a value: "))
obj= abc(num)

class student:
  def __init__(self, name, age):
    self.name=name
    self.age=age
  def hi(self):
    print(f"Hello, I am {self.name} and i am {self.age} years-old.")
s=student('Mohan', 21)
s.hi()

''' code to calculate the area of a circle by importing pi from math and create a
 class with a constructor,
where radius is considerd as an arg
clauclte and return the value to the object.'''

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    def cir(self):
      return 2*math.pi*self.radius
circle_obj = Circle(int(input("Enter radius:")))
area = circle_obj.calculate_area()
print(f"The area of the circle with radius {circle_obj.radius} is: {area}")
print("Circumference of circle", circle_obj.cir())

class Math:
  def __init__(self, num):
    self.num =num
  def fact(self):
    f = 1
    for i in range(1, self.num+1):
      f*=i
    return f
number=int(input("Enter the number:"))
m= Math(number)
print("Factorial: ", m.fact())

import math
class SquareRoot:
    def find_root(self, number):
        if number < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        return math.sqrt(number)
if __name__ == "__main__":
    calculator = SquareRoot()
num = float(input("Enter a number to find its square root: "))
result = calculator.find_root(num)
print(f"The square root of {num} is: {result}")

class number:
  even=[]
  odd=[]
  def __init__(self,n):
    self.n=n
    if n%2==0:
      number.even.append(n)
    else:
      number.odd.append(n)

n1= number(21)
n2= number(25)
n3= number(541)
n4= number(24)
n5= number(66)
print("Even:",number.even)
print("Odd:",number.odd)



#__del__():

'''del method / class variable with const access'''

class monkey():
  class_var= 0
  print("initial Class_var:",class_var)
  class_var+=1
  print("initial Class_var:",class_var)
  def __init__(ac,var):
    monkey.class_var += 10
    ac.var=var
    print("Oject_var:", ac.var)
    print("Class_var:", monkey.class_var)
    #cal(var)
  '''def cal(self,a):

    print(self.var)
    print("initial Class_var:",monkey.class_var)'''
obj1= monkey(20)
#monkey.cal("abc")
#print("initial Class_var:",monkey.class_var)
obj2= monkey(21)
obj1= monkey(50)

class calc:
  def __init__(self, a,b):
    self.a=a
    self.b=b
    print("Calc obj created......")
  def add(self):
    return self.a+self.b
  def sub(self):
    return self.a-self.b
  def __del__(self):
    print("Created Calc obj was deleted.........")
a= int(input("Enter the value of a:"))
b= int(input("Enter the value of b:"))
c= calc(a,b)
print("Addition:", c.add())
print("Subtract:", c.sub())
del calc

'''code to calc area and circumference of a circle by using a class
rectangle, create a constructor and seprate functions for area circ and delete the
constructor import math pi value.'''

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def __del__(self):
        print(f"Circle object with radius {self.radius} is being deleted.")


radius_input = float(input("Enter the radius of the circle: "))

my_circle = Circle(radius_input)
area = my_circle.calculate_area()
circumference = my_circle.calculate_circumference()

print(f"The area of the circle is: {area:.2f}")
print(f"The circumference of the circle is: {circumference:.2f}")

del my_circle

'''special methods:
__cmp__()-> objects comparision
__len__()->len(objects)
__repr__()-> str representation
__call__()-> n args
comparative -
__lt__(), __le__(),
__eq__(), __ne__(),
__gt__(), __ge__()
__hash__()-used for an obj / it will decide the place of any object data structure
__iter__() iteration over objects
__getitem__()--> indexing key ->(self,key)
__setitem__()-->(self,key,value)

'''

class Numbers:
  def __init__(self, myList):
    self.myList=myList
  def __getitem__ (self, index):
    return self.myList[index]
  def __setitem__(self, index, val):
    self.myList[index]= val
NumList= Numbers ([1,2,3,4,5,6,7,8,9,10])
print(NumList[5])
NumList[3]=100
print(NumList.myList)

# math evaluation on get item setitem code to add the sum of rows in a 2-d list '''

class RowSum:
  def __init__(self, matrix):
    self.matrix= matrix
  def __getitem__ (self, row):
    return sum(self.matrix[row])
  def __setitem__(self, row, val):
    self.matrix[row]= val
m= RowSum([[1,2], [3,4], [5,6]])
# sum of index row values = 3
# sum of 1 index row values 11

print("Sum of row 0 : ",m[0])
print("Sum of row 1 : ",m[1])
print("Sum of row 2: ", m[2])
m[1]=[10,20]

print("New sum of row 1 :",m[1])

'''Mutable type attributes
code to illustrate multiple attributes by calling a class fpr its
specifications
for example n = 21, 32, 43, 54, 65
even list: [32,54]
odd list: [21,43,65]'''

"""'''Mutable type attributes
code to illustrate multiple attributes by calling a class fpr its
specifications
for example n = 21, 32, 43, 54, 65
even list: [32,54]
odd list: [21,43,65]'''
"""

class numc:
  even_numbers = []
  odd_numbers = []

  def __init__(self, number):
    if number % 2 == 0:
      numc.even_numbers.append(number)
    else:
      numc.odd_numbers.append(number)

Numbers = [21, 32, 43, 54, 65]
for num in Numbers:
  numc(num)

print("Even list:", numc.even_numbers)
print("Odd list:", numc.odd_numbers)

class numc:
  even_numbers = []
  odd_numbers = []

  def __init__(abc,number):
    if number % 2 == 0:
      numc.even_numbers.append(number)
    else:
      numc.odd_numbers.append(number)
n1=numc(22)
n2=numc(32)
n3=numc(54)
n4=numc(65)
n5=numc(20)
print("Even list:", numc.even_numbers)
print("Odd list:", numc.odd_numbers)

def op(x):
  return x**3

class abc():
  def __init__(self, val):
    self.val=val

  def display(self):
    print("Given value:", self.val)

  def modify(self):
    self.val=op(self.val)

n=int(input("Enter the value of n:"))

o=abc(n)
o.display()
o.modify()
o.display()

class abc():  #deg(abc)
  def __init__(self,var1,var2):
    self.var1=var1
    self.var2=var2
  def display(self):
    print("var1:",self.var1)
    print("var2:",self.var2)

n1=int(input("Enter the value of n1:"))
n2=int(input("Enter the value of n2:"))

c=abc(n1,n2)
print("object.__dict__-",c.__dict__)
print("object.__doc__-",c.__doc__)
print("object.__module__-",c.__module__)
print("class.__name__-",abc.__name__)
print("class.__base__-",abc.__base__)

def add():
  c = a+b
  #return a+b
print(add)

'''code to view the memory info in a class, which gives the type of the class,
 size of the class object, and size of instance
 const: use package- sys for size of given value of num = 10
 class name is A'''

import sys
class A:
  def __init__(self, value):
    self.value = value
num = 10

print("Type of the class:", type(A))
print("Size of the class object:", sys.getsizeof(A))

instance = A(num)
print("Size of the instance:", sys.getsizeof(instance))

'''create a class atm and check the pin user1234
define a function to with draw 2000/-, balace amount from account 5999,
 if the amount is over the balance exit and check the pin
 for accessing the account ......'''

import datetime

class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def check_pin(self, entered_pin):
        if entered_pin == self.pin:
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            return False
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")
            with open('data.txt','a') as file:
              file.write(f"Amount withdrawn: {amount}\n")
              file.write(f"Remaining balance: {self.balance}\n")
            return True

    def get_balance(self):
        return self.balance
    def deposit(self, amount):
      self.balance+=amount
      with open('data.txt','a') as file:
        file.write(f"Amount deposited: {amount}\n")
        file.write(f"Remaining balance: {self.balance}\n")
      return self.balance

atm = ATM("user1234", 0)

entere_pin = input("Enter your PIN: ")

if atm.check_pin(entere_pin):
    print("PIN accepted.")
    deposit_amount = int(input("Enter the amount to deposit: "))
    atm.deposit(deposit_amount)
    withdraw_amount = int(input("Enter the amount to withdraw: "))
    atm.withdraw(withdraw_amount)
else:
    print("Incorrect PIN. Exiting.")

"pip install psycopg2-binary"

'''CREATE TABLE atm_transactions (
    id SERIAL PRIMARY KEY,
    transaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transaction_type TEXT,
    amount REAL,
    balance REAL
);
'''

import datetime
import psycopg2

class ATM:
    def __init__(self, pin, balance, db_conn):
        self.pin = pin
        self.balance = balance
        self.conn = db_conn

    def log_transaction(self, transaction_type, amount):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO atm_transactions (transaction_type, amount, balance) VALUES (%s, %s, %s)",
                (transaction_type, amount, self.balance)
            )
            self.conn.commit()

    def check_pin(self, entered_pin):
        return entered_pin == self.pin

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            return False
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")
            self.log_transaction("Withdraw", amount)
            return True

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. Current balance: {self.balance}")
        self.log_transaction("Deposit", amount)
        return self.balance

    def get_balance(self):
        return self.balance


# PostgreSQL DB connection setup
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)

# ATM session
atm = ATM("user1234", 0, conn)
entered_pin = input("Enter your PIN: ")

if atm.check_pin(entered_pin):
    print("PIN accepted.")
    deposit_amount = int(input("Enter the amount to deposit: "))
    atm.deposit(deposit_amount)
    withdraw_amount = int(input("Enter the amount to withdraw: "))
    atm.withdraw(withdraw_amount)
else:
    print("Incorrect PIN. Exiting.")

conn.close()

import psycopg2
import datetime

class ATM:
    def __init__(self, conn):
        self.conn = conn
        self.user_id = None
        self.username = None
        self.balance = 0

    def authenticate_user(self, username, pin):
        with self.conn.cursor() as cur:
            cur.execute("SELECT user_id, balance FROM users WHERE username=%s AND pin=%s", (username, pin))
            result = cur.fetchone()
            if result:
                self.user_id, self.balance = result
                self.username = username
                return True
            else:
                return False

    def log_transaction(self, transaction_type, amount):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO atm_transactions (user_id, transaction_type, amount, balance) VALUES (%s, %s, %s, %s)",
                (self.user_id, transaction_type, amount, self.balance)
            )
            self.conn.commit()

    def update_balance(self):
        with self.conn.cursor() as cur:
            cur.execute("UPDATE users SET balance = %s WHERE user_id = %s", (self.balance, self.user_id))
            self.conn.commit()

    def deposit(self, amount):
        self.balance += amount
        self.update_balance()
        self.log_transaction("Deposit", amount)
        print(f"Deposit successful. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        self.update_balance()
        self.log_transaction("Withdraw", amount)
        print(f"Withdrawal successful. Remaining balance: {self.balance}")


# PostgreSQL DB connection
conn = psycopg2.connect(
    dbname="testdb",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

# Start ATM
atm = ATM(conn)
username = input("Enter your username: ")
pin = input("Enter your PIN: ")

if atm.authenticate_user(username, pin):
    print(f"Welcome, {username}!")
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == "3":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid option. Try again.")
else:
    print("Invalid username or PIN.")

conn.close()
