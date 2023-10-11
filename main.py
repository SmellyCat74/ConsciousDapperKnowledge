name = input("Please, enter your name:")
print("Welcome,", name)
print("------------------------------------------------------------")
x=int(input("Please, enter an integer:"))
y=int(input("Please, enter a second integer:"))
print("Your first integer is",x)
print("Your second integer is",y)
print("Here are some matematical equations based on your integers")
print("------------------------------------------------------------")
print("Addition")
z = x + y
print("x=",x,"y=",y,x,"+",y,"=",z)
print("------------------------------------------------------------")
print("Subtraction")
z = x - y
print("x=",x,"y=",y,x,"-",y,"=",z)
print("------------------------------------------------------------")
print("Multiplication")
z = x * y
print("x=",x,"y=",y,x,"*",y,"=",z)
print("------------------------------------------------------------")
print("Division")
z =(float(x/y))
print("x=",x,"y=",y,x,"/",y,"=",z)
print("------------------------------------------------------------")
x=float(input("Please, enter a value for x:"))
y=float(input("Please, enter a value for y:"))
print(float(x/y))

a=int(input("Please, enter a value for a:"))
b=int(input("Please, enter a value for b:"))
if b > a:
  print("b is greater than a")
  print(b,">",a)
if b < a:
  print("b is less than a")
  print(b,"<",a)
if b == a:
  print("b is equal to a")
  print(b,"=",a)
print("------------------------------------------------------------")
print("Choices: Addition, Subtraction, Multiplication, Division") 
operator = input("Choose an operation:")

if operator == "Addition":
  x=int(input("Please, enter a number:"))
  y=int(input("Please, enter another number:"))
  z = x + y
  print("The sum of",x,"and",y,"is",z)
  print(x,"+",y,"=",z)
if operator == "Subtraction":
  x=int(input("Please, enter a number:"))
  y=int(input("Please, enter another number:"))
  z = x - y
  print("The difference between",x,"and",y,"is",z)
  print(x,"-",y,"=",z)
if operator == "Multiplication":
  x=int(input("Please, enter a number:"))
  y=int(input("Please, enter another number:"))
  z = x * y
  print("The product of",x,"and",y,"is",z)
  print(x,"*",y,"=",z)
if operator == "Division":
  x=float(input("Please, enter a number:"))
  y=float(input("Please, enter another number: "))
  z = x / y
  print("The quotient of",x,"and",y,"is",z)
  print(x,"/",y,"=",z)
print("------------------------------------------------------------")
print("Modulus")
x=int(input("Please, enter an integer:"))
y=int(input("Please, enter a second integer:"))
print("integer 1 is",x)
print("integer 2 is",y)
z = x % y
print(x,"%",y,"=",z)
print("------------------------------------------------------------")
print("Exponentiation")
x=int(input("Please, enter an integer:"))
y=int(input("Please, enter a  second integer:"))
print("integer 1 is",x)
print("integer 2 is",y)
z = x ** y
print(x,"**",y,"=",z) #same as 2*2*2*2
print("------------------------------------------------------------")
print("Floor Division")
x=int(input("Please, enter an integer:"))
y=int(input("Please, enter a  second integer:"))
print("integer 1 is",x)
print("integer 2 is",y)
z = x // y
print(x,"//",y,"=",z) #the floor division // rounds the result down to the nearest whole number
print("------------------------------------------------------------")
print("Choices: Modulus, Exponentiation, Floor Division") 
operator = input("Choose an operation:")

if operator == "Modulus":
  x=int(input("Please, enter a number:"))
  y=int(input("Please, enter another number:"))
  z = x % y
  print("The modulo of",x,"and",y,"is",z)
  print(x,"%",y,"=",z)

if operator == "Exponentiation":
  x=int(input("Please, enter a number:"))
  y=int(input("Please, enter another number:"))
  z = x ** y
  print(x,"to the power of",y,"is",z)
  print(x,"**",y,"=",z) #same as 2*2*2*2

if operator == "Floor Division":
  x=int(input("Please, enter a number:"))
  y=int(input("Please, enter another number:"))
  z = x // y
  print("The whole number",x,"and",y,"rounded to was",z)
  print(x,"//",y,"=",z)
print("------------------------------------------------------------")
x=int(input("Please, enter an integer:"))
y=int(input("Please, enter a second integer:"))
print("Your first integer is",x)
print("Your second integer is",y)
print("Here is another set matematical equations based on your integers")
print("------------------------------------------------------------")
print("Addition")
z = x + y
print("x=",x,"y=",y,x,"+",y,"=",z)
print("------------------------------------------------------------")
print("Subtraction")
z = x - y
print("x=",x,"y=",y,x,"-",y,"=",z)
print("------------------------------------------------------------")
print("Multiplication")
z = x * y
print("x=",x,"y=",y,x,"*",y,"=",z)
print("------------------------------------------------------------")
print("Division")
z=(float(x/y))
print("x=",x,"y=",y,x,"/",y,"=",z)
print("------------------------------------------------------------")
print("Modulus")
z = x % y
print(x,"%",y,"=",z)
print("------------------------------------------------------------")
print("Exponentiation")
z = x ** y
print(x,"**",y,"=",z) #same as 2*2*2*2
print("------------------------------------------------------------")
print("Floor Division")
z = x // y
print(x,"//",y,"=",z) #the floor division // rounds the result down to the nearest whole number
print("------------------------------------------------------------")
print("Choices: Addition, Subtraction, Multiplication, Division, -- Modulus, Exponentiation, Floor Division") 
operator = input("Choose an operation:")

if operator == "Addition":
  x=int(input("Please, enter a number:"))
  y=int(input("Please, enter another number:"))
  z = x + y
  print("The sum of",x,"and",y,"is",z)
  print(x,"+",y,"=",z)
  
if operator == "Subtraction":
  x=int(input("Please, enter a number:"))
  y=int(input("Please, enter another number:"))
  z = x - y
  print("The difference between",x,"and",y,"is",z)
  print(x,"-",y,"=",z)
  
if operator == "Multiplication":
  x=int(input("Please, enter a number:"))
  y=int(input("Please, enter another number:"))
  z = x * y
  print("The product of",x,"and",y,"is",z)
  print(x,"*",y,"=",z)
  
if operator == "Division":
  x=float(input("Please, enter a number:"))
  y=float(input("Please, enter another number:"))
  z = x / y
  print("The quotient of",x,"and",y,"is",z)
  print(x,"/",y,"=",z)
  
if operator == "Modulus":
  x=int(input("Please, enter a number:"))
  y=int(input("Please, enter another number:"))
  z = x % y
  print("The modulo of",x,"and",y,"is",z)
  print(x,"%",y,"=",z)
  
if operator == "Exponentiation":
  x=int(input("Please, enter a number:"))
  y=int(input("Please, enter another number:"))
  z = x ** y
  print(x,"to the power of",y,"is",z)
  print(x,"**",y,"=",z) #same as 2*2*2*2

if operator == "Floor Division":
  x=int(input("Please, enter a number:"))
  y=int(input("Please, enter another number:"))
  z = x // y
  print("The whole number",x,"and",y,"rounded to was",z)
  print(x,"//",y,"=",z)
print("------------------------------------------------------------")
