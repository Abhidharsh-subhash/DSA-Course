# Polymorphism means "many forms". In object-oriented programming (OOP),
# polymorphism allows different classes to have methods with the same name but
# behave differently based on the object that is calling them.


# Python supports two main types of polymorphism:

# 1) Compile-time Polymorphism (Method Overloading) – Not directly supported in Python.
# Method overloading allows a class to have multiple methods with the same name but different parameters.
# Python does NOT support method overloading directly, because functions in Python can take a variable number of arguments
# How to Achieve Method Overloading in Python?
# Use default arguments or *args to handle multiple parameters.


class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c


obj = MathOperations()
print(obj.add(10, 20))
print(obj.add(10, 20, 30))


# 2)Run-time Polymorphism (Method Overriding & Operator Overloading) – Supported in Python.
# Method overriding allows a child class to provide a specific implementation of a method that is already defined in the parent class.
class Animal:
    def sound(self):
        return "fearing sound"


class Dog(Animal):
    def sound(self):
        return "Bow Bow"


class Cat(Animal):
    def sound(self):
        return "Meow"


dog = Dog()
cat = Cat()
print(dog.sound())
print(cat.sound())


# 3)Operator Overloading (Supported in Python)
# Python allows us to overload operators so they can work with user-defined objects.


class Book:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"Book with pages {self.pages}"

    def __add__(self, other):
        return f"{self.pages + other.pages} pages"

    def __sub__(self, other):
        return f"{self.pages - other.pages} pages"

    def __mul__(self, other):
        return f"{self.pages * other.pages} pages"


book1 = Book(220)
book2 = Book(500)
print(book1 + book2)
print(book1 - book2)
print(book1 * book2)
