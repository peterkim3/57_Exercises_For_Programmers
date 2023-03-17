while True:
    age = input("What is your age? ")

    if age.isdigit() and int(age) > 0:
        age = int(age)
        break
    else:
        print("Wrong input. Try again.")
    
print("You are not old enough to legally drive.") if age < 20 else print("You are old enough to legally drive.")

d = dict(zip(["Korea", "Japan", "USA"], [19, 20, 21]))
legal = []
for i in d:
    if d[i] < age:
        legal.append(i)

print(f"You are old enough to legally drive in {legal}")