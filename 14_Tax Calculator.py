amount = int(input("What is the order amount? "))
state = input("What is the state? ").upper()


s = dict(zip(["WISCONSIN"], ["WI"]))
d = dict(zip(["WI"], [0.055]))
if len(state) > 2:
    state = s[state]

tax = amount * d[state]
total = amount * (1 + d[state])

print(f"The subtotal is ${amount}.\n",
      f"The tax is ${round(tax, 1)}.\n",
      f"The total is ${round(total, 2)}.")