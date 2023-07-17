# def keyword to define a function

#1 - Example
def square(x):
    return x*x

for i in range(11):
   print(f"The square of {i} is {square(i)}")

#2 - Importing a function
from functions2 import cube
# or import functions2 -> Then functions2.cube
for i in range(11):
   print(f"The cube of {i} is {cube(i)}")

# This way we can import different built in modules such as csv or math, etc