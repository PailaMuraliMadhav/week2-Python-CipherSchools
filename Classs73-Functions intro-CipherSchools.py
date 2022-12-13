#functions
name="murali"
print(len(name))

def add_two(a,b):
    return a+b

total =add_two(10,4)
print(total)

a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
total=add_two(a,b)
print(total)

firstname=input("type first name: ")
lastname=input("type lastname: ")
print(add_two(firstname,lastname))