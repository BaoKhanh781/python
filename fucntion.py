# Python Lists
x = 42
print(x)
print(type(x))
# re-assign the variable 'x' to be a list with the following elements:
# 1,3,5,23,9,14
x = [1,3,5,23,9,14]
print(x)
print(type(x))
print('Creating a list of mixted Type objects')
x = ['fName', 'lName', 25, True, 4.2]
print('x is now a list of mixed objects')
print(x)
print(type(x))
print('Add more hard-coded challenge to the list')
x.append(67)
x.append(42)
x.append('hi')
print(x)
print(type(x))
    
print('let\'s index the list')
for item in x:
    print(item)
    print(type(item))
