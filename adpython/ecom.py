class Product:
    def __init__(self,items,prices):
        self.ite = items
        self.p = prices
        
    def cal(self):
        total_cost = 0
        
        for c in self.p:
            total_cost = total_cost + c
        return total_cost 
class Physical_Product(Product):
    def __init__(self,items,prices):
        super().__init__(items,prices)

    def cal(self):
        total_cost = 0
        
        for c in self.p:
            total_cost = total_cost + c
        final = total_cost + 50
        return final

class Digital_Product(Product):
    def __init__(self,items,prices):
        super().__init__(items,prices)
    
    def cal(self):
        total_cost = 0
    
        for c in self.p:
            total_cost = total_cost + c
        tax = total_cost*0.12 
        final = total_cost + tax
        return final

products = ["1.pen","2.eraser","3.scale"]
print(f"select items from store:{products}")
items = []
for i in range(1,4):
    item = input(f"enter item number:{i} and type stop to exit and go billing: ")
    if item == "stop":
        break
    items.append(item)
print(items)
print(f"your items are listed below enter there prices:")
   
prices = []
for x in items:
    print(f"enter price of {x}")
    price = int(input(":"))
    prices.append(price)

print("below are base prices for checking proceed for type of product and select")
print("items | cost")
for item, cs in zip(items, prices):
    print(f"{item} : {cs}")
base = Product(items,prices)
print(f"total base price without tax is {base.cal()}")



ty = int(input("enter 1 for digital product and 2 for physical product:"))
if ty == 1:
    digi = Digital_Product(items,prices)
    print(f"total amount with tax is {digi.cal()}")
elif ty == 2:
    pys = Physical_Product(items,prices)
    print(f"total amount with tax is {pys.cal()}")


     
     


