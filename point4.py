A:int = 25000000 # Popullation in country A
B:int = 18900000 # Popullation in country B (Note* in the repo it wasn't clear if it was 18 or 18,9 millions)
year:int = 2022 # Initial year

num_years = 1 # 1 is asigned to the variable num_years
year += 1 # 1 is added to year
while B < A: # The code will run until populltaion in country B is smaller than in country A
    if B*(1 + 0.03)**num_years > A*(1 + 0.02)**num_years: # If having aplyed the equations for exponential growth, the popullation in B is greater than in A,
        break # the loop is broken
    else: # if not, 1 is added to num_years and year
        num_years += 1
        year += 1

print(f"In year {str(year)} populltaion in country B is grater than in country A") # The message is printed when the loop is broken