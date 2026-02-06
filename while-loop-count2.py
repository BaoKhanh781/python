
# <Add Any Header Comments, Versioning & License>
# <Add a Comment Here to describe/explain what you are doing>

# Your Code Starts Here:
# Enter Your Code Here:

def main():
    print("Starting Code Challenge")
    # Print The User Input
    number = input("Enter an integer from 1-9")
    try:
        if (int(number) < 10):
            pass
    except:
        print("Please enter an integer from 1-9")
    integer = int(number)
    n = 0
    print("Starting While Loop - Print Count Variable")
    while (n < 10):
        if (n == integer):
            print("The User variable is equal to the count variable.")
            print("User =", integer)
            print("Count =", n)
        else:
            print(n)
        n += 1
    
    print("Ending While Loop")
    print("Ending Code Challenge")

main()
