import random

cities = ["Paris", "Rome", "London", "Berlin", "Madrid"]

city_temps = {item: random.randint(1, 10) for item in cities}
print(city_temps)

filtered = {key: value for key, value in city_temps.items() if value > 5}
print(filtered)
