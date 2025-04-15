# Base class representing a generic Animal
class Animal:
    def move(self):
        """
        Define a generic move method to be overridden by subclasses.
        """
        pass

# Subclass representing a Dog
class Dog(Animal):
    def move(self):
        """
        Override the move method to simulate a dog running.
        """
        print("Running 🐕")

# Subclass representing a Bird
class Bird(Animal):
    def move(self):
        """
        Override the move method to simulate a bird flying.
        """
        print("Flying 🐦")

# Subclass representing a Fish
class Fish(Animal):
    def move(self):
        """
        Override the move method to simulate a fish swimming.
        """
        print("Swimming 🐟")

# Example usage of polymorphism
animals = [Dog(), Bird(), Fish()]  # Create a list of different Animal objects

# Iterate through the list and call the move method for each animal
for animal in animals:
    animal.move()