def countdown(a):
    return_list = []
    for i in range(a, -1, -1):
        return_list.append(i)
    print(return_list)

countdown(10)

def print_and_return(a, b):
    print(a)
    return b

print_and_return(4, 15)

def first_plus_length(a):
    b = len(a)
    c = a[0]
    b = c+b
    print(b)

list_1 = [6, 12, 15, 4, 9, 37, 44, 21]
list_2 = [9]
first_plus_length(list_1)

def values_greater_than_second(a):
    return_list = []

    if len(a) < 2:
        return_list.append(False)
    else:
        b = a[1]
        for i in a:
            if i > b:
                return_list.append(i)
            else: 
                continue
    print(return_list)

values_greater_than_second(list_1)
values_greater_than_second(list_2)

def this_length_that_value(a, b):
    list_1 = []
    for i in range(a):
        list_1.append(b)
    print (list_1)

this_length_that_value(4, 15)
