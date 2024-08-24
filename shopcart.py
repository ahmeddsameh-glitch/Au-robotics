class ShoppingCart:
    count = 0
    def __init__(self,items):
        self.items=[]
    def add_item(self,item,price,quantity):
        item = {
            "item":item,
            "price":price,
            "quantity":quantity,
            "total":price*quantity,
        }
        self.count+=1
        self.items.append(item)
    def remove_item(self,item_name):
         if not self.count:
             print("error removing nonexistent")
             return
         for item in self.items:
            if item["item"] == item_name:
                self.items.remove(item)
                self.count -= 1
                break
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["total"]
        return total
    def display(self):
        for item in self.items:
            print(item)
carrefour = ShoppingCart([])
carrefour.add_item("apple",1,2)
carrefour.add_item("banana",2,3)
carrefour.remove_item('banana')
carrefour.remove_item('apple')
carrefour.display()
carrefour.remove_item('apple')
print(carrefour.calculate_total())