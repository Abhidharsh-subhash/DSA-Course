# Encapsulation is one of the fundamental concepts in Object-Oriented Programming (OOP).
# It refers to the bundling of data (variables) and methods (functions) into a single unit (class) and restricting direct access to some of the object's details.

# Python achieves encapsulation by using access modifiers:


# 1)Public (public_var) – Accessible anywhere.
# In Python, attributes and methods are public by default, meaning they can be accessed from anywhere.
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


car1 = Car("Toyota", "40,00,000")
print(car1.brand)
print(car1.price)


# 2)Protected (_protected_var) – Accessible within the class and subclasses.
# A protected member is prefixed with a single underscore _, indicating that it should not be accessed directly outside the class but can be accessed within subclasses.
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def details(self):
        return f"Name {self.name} of age {self._age}"


person1 = Person("abhi", 25)


# Using Protected Members in Subclasses
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def details(self):
        return f"Name {self.name} of age {self._age} with salary {self.salary}"


# 3)Private (__private_var) – Not directly accessible outside the class
# A private member is prefixed with double underscores __, making it inaccessible from outside the class.
class BankAccount:
    def __init__(self, Account_number, balance):
        self.Account_number = Account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return f"{amount} deposited to your account."

    def check_balance(self):
        return f"Your account balance is {self.__balance}"


account1 = BankAccount("21435687", 2000)
print(account1.check_balance())
print(account1.deposit(5000))
print(account1.check_balance())
