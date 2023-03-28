n:int 
n = int(input("Enter a number between 2 and 50: ")) # The user is asked to enter an integer
x = 1 # x is set to 1 as a counter
while x <= n//2: # The loop takes place until the half of n
    if n%x == 0: # If the module of n divided into x is zero, x is a divisor of n and it's printed
        print(x)
        x += 1 # After printing x, 1 is added to x
    else: 
        x += 1 # If the condition is not met, 1 is also added to x
print(n) # n is printed at the end becuase a number is divisor of itself