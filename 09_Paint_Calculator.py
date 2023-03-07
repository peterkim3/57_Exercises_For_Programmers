import math

gallonPerSquare = 360

def make_answer_square_room(width: int, height: int) -> str:
    result = (width * height) / gallonPerSquare
    ans1 = f"You will need to purchase {math.ceil(result)} gallons of paint to cover {width * height} square feet."
    return ans1

def make_answer_round_room(radius: int) -> str:
    result = (radius * radius * math.pi) / gallonPerSquare
    ans1 = f"You will need to purchase {math.ceil(result)} gallons of paint to cover {round(radius * radius * math.pi, 2)} square feet."
    return ans1

while True:
    type = input("Enter the number\n(1) Square room\n(2) Round room\n")
    if not type.isdigit():
        print("Wrong type. Try again.")    
        continue
    
    if int(type) == 1:
        width = input("What is the width of the room? ")
        height = input("What is the height of the room? ")
    
        if width.isdigit() and height.isdigit():
            width, height = int(width), int(height)
            if width > 0 and height > 0:
                print(make_answer_square_room(width, height))
                break
        else:
            print("Wrong input. Try again.")
    elif int(type) == 2:
        radius = input("What is the radius of the room?")
        if radius.isdigit():
            radius = int(radius)
            if radius > 0:
                print(make_answer_round_room(radius))
                break
        
    print("Wrong input. Try again.")


"""
Unsolved Challenge
- Implement a mobile version of this app 
so it can be used at the hardware store.    
"""