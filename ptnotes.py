# IF CONDITION
a = 10
b =15
if b > a:
 print("b is greater")

#IF,ELSE CONDITION
c = 15
d = 20
if c > d:
    print("c is greater")
else:
    print("d is greater")

#IF ,ELIF, ELSE CONDITION
e = 10
f = 20
if e > f :
 print("e is greater")
elif e == f:
  print("e and f is equal")
else:
  print("f is greater")
#shorthand if in one line
a= 10
b= 20
if b>a : print("b is greater")
#shorthand if,else
c=30
d=30
print("c is greater") if c > d  else print("equal")
#mutiple in one line
e = 20
f = 10
print("F") if f > e else print("equal") if e == f else print("E")

#AND
a = 10
b = 20
c = 10
if a<b and a==c:
    print("Two conditions are true")
#OR
a = 10
b = 20
c = 10
if a>b or a==c:
    print("any one cond is true")
#nested
x =30
if x>10:
     print("greter than 10")
     if x >20:
         print("also greater than 20")
     else:
         print("nothing")

#pass statement
a= 10
b= 20
if a >b:
    pass

###### WHILE LOOP
x = 0
while x < 6:
  print(x)
  x = x + 1
#break
x = 0
while x < 6:
    print(x)
    if x == 3:
        break
    x = x + 1
#CONTINUE
x = 0
while x < 6:
    x += 1
    if x == 3:
        continue
    print(x)
#ELSE
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is  no longer less than 6")
#FOR LOOP
a = ["anbu", "athiran", "som"]
for x in a:
  print(x)
#break
a = ["anbu", "athiran", "som"]
for x in a:
    print(x)
    if x == "athiran" : #Exit the loop when x is "athiran"
        break
#break2
a = ["anbu", "athiran", "som"]
for x in a:
    if x == "athiran" : #Exit the loop when x is "athiran", but this time the break comes before the print
        break
    print(x)
#CONTINUE
a = ["anbu", "athiran", "som"]
for x in a:
    if x == "athiran" :
        continue
    print(x)
#RANGE
for x in range(1, 6):
    print(x)
#RANGE USE INCREMENT BY USER
for x in range(1, 50, 4):
    print(x)
#else loop
for x in range(1, 6):
    print(x)
else:
    print('printed successfully')
#ELSE LOOP
for x in range(1, 6):
    print(x)
    if x == 3:
        break
        ### else block will  not executed in break statement
else:
    print('printed successfully')
#PASS--use pass avoiding get error
for i in range(1,5):
    pass
#PYTHON FUNCTIONS
def my_function():
  print("Hello function")
my_function()

#Arguments used function
def my_function(fn1, fn2):
    print("Hello " + fn1 +" and " + fn2)
my_function("akash", "anbu")

#ARBITARY ARGUMENTS
def my_function(*name):
  print("The child is " + name[2])

my_function("Emilia", "shark", "jack")

#ARBITARY KEYWORD AND ARGUMENTS
def my_function(**name):
  print("The child is " + name["lname"])
my_function(fname = "jack", lname = "rose")
#DEFAULT PARAMETER
def my_function(city ="chennai"):
    print("The city name is " + city)
my_function("salem")
my_function("coimbatore")
my_function()
#LAMBDA EXPRESSION
a = lambda x: x+10
print(a(10))
#CREATE OBJECT AND CLASS
class myclass:
    x =5
    y="str"
p1 = myclass()
print(p1.x)
print(p1.y)
#_INIT_function
class new:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = new("Akash", 25)
print(p1.name)
print(p1.age)
#object methods
class man:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def my_func(self):
        print("The person is " + self.name + " And age is " + self.age)
p1 = man("Akash", "25")
p1.my_func()
#inheritance
class man:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def my_func(self):
        print(self.fname, self.lname)
class student(man):  ##using PASS statement
    pass
x = student("pavi","kali")
x.my_func()
#ADD CHILD CLASS USING _INT _
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
#
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("john", "sen")
x.printname()
#SUPER METHOD
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
#
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
x = Student("john", "sen")
x.printname()
#add function
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
#
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
#
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, self.graduationyear)

x = Student("john", "sen", 2019)
x.welcome()
#
#ITERATORS
my = ("apple", "banana", "cherry")
my1 = iter(my)

print(next(my1))
print(next(my1))
print(next(my1))
#use iter and next
class akash:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

my = akash()
my1 = iter(my)

print(next(my1))
print(next(my1))
print(next(my1))
print(next(my1))
print(next(my1))
#SCOPE
#local
def myfunc():
  x = 100
  print(x)

myfunc()
#global
x=200
def myfunc():
  print(x)

myfunc()
#local and global
x = 200

def myfunc():
  x = 100
  print(x)

myfunc()
print(x)
#use GLOBAL key
def myfunc():
  global x
  x = 200

myfunc()
print(x)
#module
import platform

x = dir(platform)
print(x)
#DATETIME
import datetime

x = datetime.datetime.now()
print(x)
#day and year
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
#MATH func
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)
#positive value
x = abs(-101.25)

print(x)
#power
x = pow(9, 3)

print(x)
#sqrt
import math

x = math.sqrt(125)

print(x)
#ceil and floor
import math

x = math.ceil(5.5)
y = math.floor(6.2)

print(x)
print(y)
# covert json to python
import json
x = '{ "name":"Akash", "age":24, "city":"Chennai"}'
y = json.loads(x)
print(y)
#python to json
import json
x = { "name":"Akash", "age":24, "city":"Chennai"}
y = json.dumps(x)
print(y)
#use indent
x = { "name":"Akash", "age":24, "city":"Chennai"}
print(json.dumps(x, indent= 4))
#use separators
x = { "name":"Akash", "age":24, "city":"Chennai","car":"ford"}
print(json.dumps(x, indent= 4, separators=(",","=")))
#use sort _keys
x = { "name":"Akash", "age":24, "married":True, "city":"Chennai","car":"ford", "dogs":None}
print(json.dumps(x, indent= 4, sort_keys=True))
#REGEX search
import re
txt = "No pain no Gain"
x = re.search("^No.*Gain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
#find all
import re
txt = "No pain no Gain"
x = re.findall("ai", txt)
print(x)
#spilit
import re
txt = "No pain no Gain"
x = re.split("\s", txt)
print(x)
#split with whitespace
import re
txt = "No pain no Gain"
x = re.split("\s", txt, 2)
print(x)
#span
import re
txt = "No pain no Gain"
x = re.search(r"\bG\w+", txt)
print(x.span())
#string
import re

txt = "No pain no Gain"
x = re.search(r"\bG\w+", txt)
print(x.string)
#group
import re

txt = "No pain no Gain"
x = re.search(r"\bp\w+", txt)
print(x.group())
#try except
try:
  print("hello")
except:
  print("Something else went wrong")
#use final
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("final finished")
##user input
"""name = input("Enter name:")
print("The name is: " + name)"""
#sring format
qty = 3
item = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(qty, item, price))
##use index
qty = 3
item = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(qty, item, price))