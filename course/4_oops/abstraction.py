# It is the process of hiding implementation details and exposing only the essential features to the user.
# In Python, abstraction is achieved using abstract classes and abstract methods, which are defined using the ABC (Abstract Base Class) module.

from abc import ABC, abstractmethod


# Abstract Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # This method must be implemented by all subclasses


# Child Classes
class Dog(Animal):
    def make_sound(self):
        return "Bark"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


# Creating Objects
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Bark
print(cat.make_sound())  # Output: Meow
