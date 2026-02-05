#made a function that reads binary number
def binary_to_number(b_number):
    binary = 0
    length = len(b_number)
    for x in range(length):
        exponent = 2**(length-x-1)
        if b_number[x] != "0" and b_number[x] != "1":
            print("please only type 1 and 0")
            break
        elif b_number[x] == "1":
            binary += exponent
    return binary

binary = input("Please provide a binary number number so we can return a number")
number = binary_to_number(binary)
print("your number is " + str(number))
