
class item:
    def __init__(self, price: int, quantity: int):
        self.price = price
        self.quantity = quantity
        
    def getTotalPrice(self) -> int:
        return self.price * self.quantity


item_list = []

while True:

    price = input(f"Enter the price of item {len(item_list) + 1}: ")
    quantity = input(f"Enter the quantity of tiem {len(item_list) + 1}: ")
    
    if price.isdigit() and quantity.isdigit():
        price, quantity = int(price), int(quantity)
        if price > 0 and quantity > 0:
            item_list.append(item(price, quantity))
    else:
        "Wrong input. Try Again."
        continue
    
    type = input("Finish? (y/n)")
    if type == "y":
        break
    
subTotal = sum([x.getTotalPrice() for x in item_list])
tax = subTotal * 0.055
totalPrice = round(subTotal + tax, 2)
print(f"Subtotal : ${round(subTotal,2)}\n", 
      f"Tax: ${round(tax, 2)}\n",
      f"Total: ${totalPrice}")