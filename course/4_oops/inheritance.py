# Python supports 5 types of inheritance:

# 1)Single Inheritance


# 2)Multilevel Inheritance
# Multilevel inheritance means a class is derived from another derived class.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


# Intermediate class
class Mammal(Animal):
    def has_fur(self):
        return True


# Derived class inheriting from Mammal
class Dog(Mammal):
    def speak(self):
        return f"{self.name} barks"


# Creating an object
dog = Dog("Charlie")
print(dog.speak())  # Output: Charlie barks
print(dog.has_fur())  # Output: True


# 3)Multiple Inheritance
# Multiple inheritance allows a child class to inherit from more than one parent class.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Runner:
    def run(self):
        return "Runs fast"


# Child class inheriting from multiple parent classes
class Dog(Animal, Runner):
    def speak(self):
        return f"{self.name} barks"


# Creating an object
dog = Dog("Rocky")
print(dog.speak())  # Output: Rocky barks
print(dog.run())  # Output: Runs fast

# Method Resolution Order (MRO)
# When multiple classes have the same method, Python follows MRO (Depth-First, Left-to-Right) to decide which method to call first.


# 4)Hierarchical Inheritance
# Hierarchical inheritance occurs when multiple child classes inherit from the same parent class.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


# Multiple child classes inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"


class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"


# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy barks
print(cat.speak())  # Output: Whiskers meows


# 5)Hybrid Inheritance
# Hybrid inheritance is a mix of any two or more types of inheritance
class Animal:
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def has_fur(self):
        return True


class Bird(Animal):
    def can_fly(self):
        return True


# Multiple Inheritance + Multilevel Inheritance
class Bat(Mammal, Bird):
    def is_nocturnal(self):
        return True


# Creating an object
bat = Bat("Bat")
print(bat.has_fur())  # Output: True
print(bat.can_fly())  # Output: True
print(bat.is_nocturnal())  # Output: True


# The super() function is used to call the parent class method inside the child class.
# If you try to create an object of an abstract class, Python will throw an error.