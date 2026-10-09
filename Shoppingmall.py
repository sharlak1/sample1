class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show_details(self):
        print("name: ",self.name)
        print("price: ",self.price)
        print("stock: ",self.stock)

    def buy(self,quantity):
        if quantity <= self.stock:
            self.stock-= quantity
            total_price = self.price * quantity
            print("total cost:", total_price)
            print("Remaining stock:", self.stock)
        else:
            print("Not enough stock")          
    
class Electronics(Product):
        def __init__(self,name,price,stock,warranty):
            super().__init__(name, price, stock)
            self.warranty = warranty

        def show_warranty(self):
             print("Warranty is for:", self.warranty)

name = input("Name of product:")
price = int(input("Enter price:"))
stock = int(input("Enter stock"))
warranty = int(input("Enter warranty:"))
store1 = Electronics(name,price,stock,warranty)
store1.show_details()
quantity = int(input("Enter the quantity"))
store1.buy(quantity)
store1.show_warranty()
