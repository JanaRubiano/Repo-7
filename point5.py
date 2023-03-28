n:int 
n = int(input("Enter an integer: ")) # The user is asked to enter an integer
fact = 1 # fact is set to one
res = 1 # res is set to one
while fact <= n: # The code will run until fact is not larger than n
    res *= fact # fact times res is asigned to the variable res
    fact += 1 # 1 is added do fact

print(f"The factorial of {str(n)} is {str(res)}")
    
    