def calculateSimpleInterest(principal: int, interest: float, year: int) -> int:
    return round(principal * pow(1.0 + interest, year))

while True:
    principal = input(f"Enter the principal: ")
    interest = input(f"Enter the rate of interest: ")
    year = input(f"Enter the number of years: ")

    if principal.isdigit() and year.isdigit():
        principal, year = int(principal), int(year)
        
        idx = interest.find('.')
        if idx == -1 and interest.isdigit():
            interest = float(interest)
        elif idx != -1 and interest[0:idx].isdigit() and interest[idx + 1:].isdigit():
            interest = float(interest)
        else:
            print("Wrong interest input. Try Again.")
            continue
            
        if principal <= 0 or year <= 0 or interest <= 0:
            print("Wrong principal or year input. Try Again.")
            continue
        else:
            break

for i in range(1, year + 1):
    rtn = calculateSimpleInterest(principal, interest * 0.01, i)
    print(f"After {i} years at {interest}%, the investment will be worth ${rtn}.")    
