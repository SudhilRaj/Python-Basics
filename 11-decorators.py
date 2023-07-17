# Decorators are a way in python of taking a function and modifying it
# adding some additional functionality to a function
# Function which takes another function as input and returns the modified function
# It just like HOC in React
# In python functions are also considered as a value

# Eg:
def announce(f):
   def wrapper():
      print("About to run the function...")
      f()
      print("Done with the function")
   return wrapper

# Usage Eg
@announce
def hello():
   print("Hello world")


# Decorators are very useful