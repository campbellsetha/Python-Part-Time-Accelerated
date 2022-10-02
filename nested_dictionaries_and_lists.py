x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["y"]=30

print(x)
print(students)
print(sports_directory)
print(z)


print("------------")


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(input):
    for i in input:
        for key, val in i.items():
            print(key, "-", val)

iterateDictionary(students)


print("------------")


def iterateDictionary2(key_name, some_list):

    x = 0
    for i in some_list:
        print(some_list[x][key_name])
        x = x + 1

iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)

print("------------")


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):

    num_local = len(some_dict["locations"])
    num_instruct = len(some_dict["instructors"])

    print(num_local, " LOCATIONS")

    for i in range(num_local):
        print(some_dict["locations"][i])

    print("------------")

    print(num_instruct, " INSTRUCTORS")

    for i in range(num_instruct):
        print(some_dict["instructors"][i])


printInfo(dojo)
# output:
"""
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""