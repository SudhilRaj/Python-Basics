# There can be many exceptions. We can catch those and show users a nice message

# Eg: 
x = int(input("x: "))
y = int(input("y: "))

result = x / y

print(f"{x} / {y} = {result}")

# Eg 2:
# Exception Handling
import sys

try:
   x = int(input("x: "))
   y = int(input("y: "))
except ValueError:
   print("Error: Invalid inpuit.")
   sys.exit(1)

try:
   result = x / y
except ZeroDivisionError:
   print("Error: Cannot divide by 0.")
   sys.exit(1) # Something went wrong

print(f"{x} / {y} = {result}")
