people = [
   {"name": "Sudhil", "age": "21"},
   {"name": "Raj", "age": "29"},
   {"name": "Anu", "age": "25"},
]


# people.sort() - Error
# Need to tell the sort function how to sort
def f(person):
   return person["name"]

# people.sort(key=f)
# print(people)

# There is another easier built in way called lambda
people.sort(key=lambda person: person["name"])
print(people)
