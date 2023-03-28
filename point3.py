num:int
num = int(input("Enter a number: ")) # The user is asked to enter an integer
while num >= 2: # The code will run until the stablished limit
    if num%2 == 0: # If the condition is met, num is printed and 1 is subtracted from num
        print(num) # The number is printed
        num -= 1
    else: # If not, 1 is subtracted from num
        num -= 1

print("End of the loop")