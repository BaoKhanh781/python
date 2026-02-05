def main():
  print("Starting The Code Challenge")
  # Declare Any main() Variables - (Not Global)

  print("Starting <Specific Part> Of Code Challenge")
  # Enter Your Code Here:
  print('Enter Your Code Here:')
  user_input = input("please enter a specific number \* We'll check if it's divisible by 1-9")
  n = 10
  array = []
  while n > 0:
      if (int(user_input) % n == 0):
          array.append(str(n))
      n -= 1
  print(user_input + " can be divided by ")
  print(array)
    
  print("Ending while-loop Of Code Challenge")
  print("Ending The Code Challenge")

main()
