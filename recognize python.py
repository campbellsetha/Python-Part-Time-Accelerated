num1 = 42
# int variable delcaration
num2 = 2.3
# float variable declaration
boolean = True
# declaration for variable boolean to true
string = 'Hello World'
# declaration for variable string to 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# Initialize a list named pizza_toppings and establishes string variables within array.
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# Initialize a Dictionary named person and establishes parameters and variables.
fruit = ('blueberry', 'strawberry', 'banana')
# Initialize a Tuples named fruit and establishes variables
print(type(fruit))
# Displays variable type in the Tuples 'fruit' in the console
print(pizza_toppings[1])
# Displays the variable in the index position '1' from the pizza_toppings list in the console.
pizza_toppings.append('Mushrooms')
# Adds the variable 'Mushrooms' to the pizza_toppings list. 
print(person['name'])
# Displays the variable in the 'name' parameter of the person dictionary in the console.
person['name'] = 'George'
# Changese the variable of the 'name' parameter of the person dictionary to 'George'.
person['eye_color'] = 'blue'
# Adds the parameter 'eye_color' with the variable 'blue' to the person dictionary.
print(fruit[2])
# prints the variable in the index position '2' from the fruit Tuples in the console.

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
""" If/else conditional statements that will print out difference strings to the console
if num1 variable is higher or lower than 45.
"""
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
""" If/elif/else conditional statements that will print out difference strings to the console
depending on the length of the 'string' variable.
"""
for x in range(5):
    print(x)
    # prints x 5 times (1, 2 ,3, 4, 5)
for x in range(2,5):
    print(x)
    # prints x 3 times (3, 4, 5)
for x in range(2,10,3):
    print(x)
    # prints x 3 times (2, 5, 8)
x = 0
# sets x to zero
while(x < 5):
    print(x)
    x += 1
    #prints x  5 times (1, 2, 3, 4, 5)

pizza_toppings.pop()
# Removes the last variable in the pizza_toppings list
pizza_toppings.pop(1)
# Removes the variable in index position '1' of the pizza_toppings list

print(person)
# Prints the person dictionary parameters and variables
person.pop('eye_color')
# Removes the parameter 'eye_color' and associated variable
print(person)
# Prints the person dictionary parameters and variables
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')
    # fucntion to print 'Hello' ten times
print_hello_ten_times()
# executes function
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
    # function to print 'Hello' x number of times
print_hello_x_times(4)
# executes function and sets x to 4. Will print 'Hello' 4 times
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
# function to print 'Hello' x or 10 times
print_hello_x_or_ten_times()
# executes function to print 'Hello' 10 times
print_hello_x_or_ten_times(4)
# executes function to print 'Hello' 4 times

"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)