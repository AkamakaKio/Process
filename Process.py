class Checkout:
    def __init__(self, cart):
        self.cart = cart

    def calculate_total(self):
        total = sum(item['product'].price * item['quantity'] for item in self.cart.items)
        return total

# Example usage:
checkout = Checkout(cart)
total_amount = checkout.calculate_total()
print("Total Amount:", total_amount)
