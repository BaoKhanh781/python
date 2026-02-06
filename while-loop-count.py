
# <Add Any Header Comments, Versioning & License>
# <Add a Comment Here to describe/explain what you are doing>

# Your Code Starts Here:

# Include any Libraries
# Declare Any Global Variables

def main():
    print("Starting Code Challenge")
    # Declare Any main() Variables - (Not Global)
    
    user = input("Enter an integer number 20 or greater >")
    try:
        if (int(user) > 20):
            print("your number",user,"is a valid Integer 20 or greater. Thanks")
            
    except:
        print("your number is invalid")
    print("Starting While Loop - Print Count Variable")
    print("The user input started as", user)
    number = int(user)
    n = 0
    while (n < 5):
        number = number / 2
        n += 1
        print("The current value of the user input after some math is", number)
        print("The while loop has looped", n,"time")
    print("Ending While Loop")
    print("Ending Code Challenge")

main()
