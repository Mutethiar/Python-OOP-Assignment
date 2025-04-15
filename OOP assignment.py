# Define a class to represent a Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        """
        Initialize the Smartphone object with brand, model, and price.
        """
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        """
        Simulate making a call to the given number.
        """
        return f"Calling {number} from {self.model}..."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"


class Smartwatch(Smartphone):  # Inheritance
    def __init__(self, brand, model, price, battery_life):
        super().__init__(brand, model, price)
        self.battery_life = battery_life

    def track_steps(self, steps):
        return f"{self.model} tracked {steps} steps."

    def __str__(self):
        return f"{self.brand} {self.model} (Smartwatch) - ${self.price}, Battery Life: {self.battery_life} hours"


# Example usage
phone = Smartphone("Apple", "iPhone 14", 999)
print(phone)
print(phone.make_call("123-456-7890"))
print(phone.send_message("123-456-7890", "Hello!"))

watch = Smartwatch("Samsung", "Galaxy Watch 5", 299, 48)
print(watch)
print(watch.track_steps(5000))