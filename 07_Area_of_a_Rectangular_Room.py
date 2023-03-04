while True:
    length = input("What is the length of the room in feet? ")
    width = input("What is the width of the room in feet? ")
    
    if length.isdigit() and width.isdigit():
        length, width = int(length), int(width)
        if length > 0 and width > 0:
            break
    else:
        print("Wrong input. Try again.")

def conversion_feet_to_meter(feet_square: int) -> int:
    return feet_square * 0.09290304

print(f"You entered dimensions of {length} feet by {width} feet.\n", 
      f"The area is\n",
      f"{length * width} square feet\n",
      f"{conversion_feet_to_meter(length * width)} square meters")