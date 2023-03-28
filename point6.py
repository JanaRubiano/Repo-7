import random # Module random is imported to generate the number that is going to be guessed
number:int
answer = random.randint(1, 100) # A random number between 1 and 100 is asigned to the variable answer
number = int(input("Enter a number: ")) # The user is asked to enter an integer
while number != answer: # While number dosn't equal answer the following block of code is ran
    if number > answer: # If the entered number is greater than the answer the code asks to enter smaller values
        print("The number is smaller than the answer")
        number = int(input("Enter a number: "))

    else: # If the entered number is smaller than the answer the code asks to enter larger values
        print("The number is greater than the answer")
        number = int(input("Enter a number: "))

print(f"number found: {answer}") # When the while condition isn't met, the loop ends and prints


