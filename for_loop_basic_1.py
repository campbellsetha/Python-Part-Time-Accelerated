for i in range(151): #Basic: prints all integers from 1-150.
    print(i)

for x in range(5, 1000, 5): # Multiples of 5: Prints all multiples of 5 from 5-1000.
    print(x)

i = 1
x = 0

for i in range(1, 101): #Counting, the Dojo Way: Divisible by 5 prints 'Coding', Divisible by 10 prints 'Coding Dojo'.
    if i % 10 == 0:
        print("Coding Dojo")

    elif i % 5 == 0: 
        print("Coding")

    else:
        print(i)

total = 0

for x in range(500000): #Whoa. That Sucker's Huge: Adds all odd integers from 0-500000.
    if x % 2 == 0:
        continue
    else: 
        total = total + x


i = 0
x = 0

print(total)

for i in range(2018, 0, -4): #Countdown by Fours: Prints positive numbers decreasing by 4.
    print(i)

lowNum = 5
highNum = 120
mult = 3

for i in range(lowNum, highNum, mult): #Flexible Counter: prints multiples of a 3 between 5-120.
    if i % 5 == 0:
        print (i)