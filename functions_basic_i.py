#1
def number_of_food_groups(): # Returns the number 5, prints 5
    return 5
print(number_of_food_groups())


#2
def number_of_military_branches(): #Returns the number 5, print 19
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#3
def number_of_books_on_hold(): # Returns the number 5, print 5
    return 5
    return 10
print(number_of_books_on_hold())


#4
def number_of_fingers(): # Returns the number 5, print 5
    return 5
    print(10)
print(number_of_fingers())


#5
def number_of_great_lakes(): # Prints the number 5 twice
    print(5)
x = number_of_great_lakes()
print(x)


#6
def add(b,c): # Prints 3, prints 5, prints 8
    print(b+c)
print(add(1,2) + add(2,3))


#7
def concatenate(b,c): # Prints the String 25
    return str(b)+str(c)
print(concatenate(2,5))


#8
def number_of_oceans_or_fingers_or_continents(): # Prints 100 returns 10
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c): # Returns value based on input
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # Returns 7, Prints 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # Returns 14, Prints 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Returns 7 on first function call, Returns 14 on second function call. Prints 21

#10
def addition(b,c): # Returns the addition of two numbers
    return b+c
    return 10
print(addition(3,5)) # Returns 8 on function call


#11 # Prints 500, function call prints 300, prints 500, fucntion call prints 300, prints 500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12 # Prints 500, function call prints 300 and returns 300, prints 300, fucntion call prints 300 and returns 300, prints 300
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13 # Prints 500, function call prints 300 and returns 300, prints 300, fucntion call prints 300 and returns 300, prints 300
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14 # print 1, print 3, print 2, print 3, print 1, print 3, print 2
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15 # print: 1, 3, 5, 3, 10
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)