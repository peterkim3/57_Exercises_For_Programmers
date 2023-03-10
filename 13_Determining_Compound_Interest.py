def calculateCompoundedInterest(principal: int, interest: float, compounded: int, year: int) -> int:
    return round(principal * pow(1.0 + interest / compounded, year * compounded))

def calculateFromCompoundedInterest(principal: int, interest: float, compounded: int, year: int) -> int:
    return round(principal / pow(1.0 + interest / compounded, year * compounded))

while True:
    principal = input(f"What is the principal amount?: ")
    interest = input(f"What is the rate?: ")
    compounded = input(f"What is the number of years?: ")
    year = input(f"What is the number of times the interest is compounded per year?: ")

    if principal.isdigit() and year.isdigit() and compounded.isdigit():
        principal, year, compounded = int(principal), int(year), int(compounded)
        
        idx = interest.find('.')
        if idx == -1 and interest.isdigit():
            interest = float(interest)
        elif idx != -1 and interest[0:idx].isdigit() and interest[idx + 1:].isdigit():
            interest = float(interest)
        else:
            print("Wrong interest input. Try Again.")
            continue
            
        if principal <= 0 or year <= 0 or interest <= 0 or compounded <= 0:
            print("Wrong principal or year or compounded input. Try Again.")
            continue
        else:
            break

for i in range(1, year + 1):
    rtn = calculateCompoundedInterest(principal, interest * 0.01, compounded, i)
    print(f"After {i} years at {interest}%, the investment will be worth ${rtn}.")    


"""
Challenges 2
Create a version of the program that works in reverse, 
so you can determine the initial amount you’d need to invest to reach a specific goal.
"""
initialAmount = calculateFromCompoundedInterest(principal, interest * 0.01, compounded, year)
print(f"It takes ${initialAmount} of initial amount to reach goal(${principal}) at {interest}% within {year} years.") 


"""
Challenges 3
Implement this program as a GUI app that automatically updates the values 
when any value changes.
"""
from tkinter import *

window = Tk()
window.title("My GUI Window")

def button_pressed():
    # 이자율 입력값 후처리 방법은 GUI 구현 챌린지에서는 미구현
    i_principal, i_interest, i_compounded, i_years = int(entry1.get()), int(entry2.get()) * 0.01, int(entry3.get()), int(entry4.get())
    rtn = calculateCompoundedInterest(i_principal, i_interest, i_compounded, i_years)
    label_inputStr["text"] = f"After {i_years} years at {i_interest * 100}%, the investment will be worth ${rtn}."
    label_inputStr["bg"] = "burlywood1"
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    
entry1 = Entry(
    master=window, fg="black", bg="yellow", width=30, justify=CENTER, font=("Arial", 25)
)
entry2 = Entry(
    master=window, fg="black", bg="yellow", width=30, justify=CENTER, font=("Arial", 25)
)
entry3 = Entry(
    master=window, fg="black", bg="yellow", width=30, justify=CENTER, font=("Arial", 25)
)
entry4 = Entry(
    master=window, fg="black", bg="yellow", width=30, justify=CENTER, font=("Arial", 25)
)
entry1.insert(index=0, string="Principal")
entry2.insert(index=0, string="Interest Rate")
entry3.insert(index=0, string="Compounded Numbers")
entry4.insert(index=0, string="Years")

label_inputStr = Label(window, text="Results will be displayed", font=("Arial", 25))

button = Button(
    master=window,
    text="Enter",
    bg="white",
    fg="blue",
    width=80,
    height=2,
    command=button_pressed,
)

label_inputStr.pack()
button.pack()
entry1.pack()
entry2.pack()
entry3.pack()
entry4.pack()
    
window.mainloop()