while True:
    numPeople = input("How many people? ")
    numPizzas = input("How many pizzas do you have? ")
    
    if numPeople.isdigit() and numPizzas.isdigit():
        numPeople, numPizzas = int(numPeople), int(numPizzas)
        if numPeople > 0 and numPizzas > 0:
            break
    else:
        print("Wrong input. Try again.")

result = numPizzas // numPeople
left = numPizzas % numPeople

print(f"{numPeople} people with {numPizzas}.\n")
if result > 1:
    print(f"Each person gets {result} pieces of pizza.\n")
else:
    print(f"Each person gets {result} piece of pizza.\n",)
    
if left > 1:
    print(f"There are {left} leftover pieces")
else:
    print(f"There is {left} leftover piece")

