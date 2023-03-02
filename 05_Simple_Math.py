def make_answer(num1: int, num2: int) -> str:
    equation = str(num1) + "-" + str(num2)
    ans1 = f"{num1} + {num2} = {num1 + num2}\n"
    ans2 = f"{num1} - {num2} = {eval(equation)}\n"
    ans3 = f"{num1} * {num2} = {num1 * num2}\n"
    ans4 = f"{num1} / {num2} = {num1 / num2}\n"
    return ans1 + ans2 + ans3 + ans4

while True:
    firstNum = input("What is the first number? ")
    secondNum = input("What is the second number? ")
    
    if firstNum.isdigit() and secondNum.isdigit():
        firstNum, secondNum = int(firstNum), int(secondNum)
        if firstNum > 0 and secondNum > 0:
            break
    else:
        print("Wrong input. Try again.")
    
    
answer = make_answer(firstNum, secondNum)
print(answer)

"""
Challenges
clear (1) Revise the program to ensure that inputs are entered as
numeric values. Don’t allow the user to proceed if the value entered is not numeric.
clear (2) Don’t allow the user to enter a negative number.
clear (3) Break the program into functions that do the computations.
You’ll explore functions in Chapter 5, Functions, on page 45.
(4) Implement this program as a GUI program 
that automatically updates the values when any value changes.
"""