import datetime 
"""
Constraints
Don’t hard-code the current year into your program.
Get it from the system time via your programming language.
"""

age = int(input("What is your current age? "))
retire_age = int(input("At what age would you like to retire? "))
yearsLeft = retire_age - age
if yearsLeft > 0:
    print(f"You have {yearsLeft} years left until you can retire.\n",
      f"It's {datetime.date.today().year}, so you can retire in {int(datetime.date.today().year) + yearsLeft}.")
# Challenge : Handle situations where the program returns a negative number by stating that the user can already retire.
else:
    print("You can already retire!")
    