def primos(num:int=1): 
    ''' This functions return the prime values from 1 to 100 '''
    while num <= 100: # The loop will run until num is not larger than 100
        divs = 0 # Zero is asigned to the variable divs
        x = 2 # x is set to 2
        while x <= int(num**0.5): # This loop runs until x is not larger than the square root of num
            if num % x == 0: # If the module of num divided by x is zero, then 1 is added to divs and to x
                divs += 1
                x += 1
            else: # If the condition is not met, 1 is added to divs and to x
                x += 1
        if divs == 0: # If the variable divs equals 0, a prime number is found and it's printed
            print(num)
            num += 1
        else:
            num += 1 # If the condition isn't met, 1 is added to num

    return "End of the loop"

if __name__ == "__main__":
    p = primos()
    print(p)