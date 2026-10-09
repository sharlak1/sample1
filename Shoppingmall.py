# This is just for trial.

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show_details(self):
        print("name:", self.name)
        print("price:", self.price)
        print("stock:", self.stock)

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.stock:
            raise ValueError("Not enough stock")
        self.stock -= quantity
        total_price = self.price * quantity
        print("total cost:", total_price)
        print("Remaining stock:", self.stock)
        return total_price


class Electronics(Product):
    def __init__(self, name, price, stock, warranty):
        super().__init__(name, price, stock)
        self.warranty = warranty

    def show_warranty(self):
        print("Warranty is for:", self.warranty)

    # Add extra years to the warranty. The number of years must be positive.
    def extend_warranty(self, years):
        if years <= 0:
            raise ValueError("Years must be greater than zero.")
        self.warranty += years
        return self.warranty


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")
        except EOFError:
            print("\nInput closed. Exiting program.")
            raise SystemExit


if __name__ == "__main__":
    name = input("Name of product: ")
    price = get_int("Enter price: ")
    stock = get_int("Enter stock: ")
    warranty = get_int("Enter warranty: ")

    store1 = Electronics(name, price, stock, warranty)
    store1.show_details()
    quantity = get_int("Enter the quantity: ")
    try:
        store1.buy(quantity)
    except ValueError as e:
        print(e)
    store1.show_warranty()
