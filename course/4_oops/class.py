class StarCookie:
    milk = "10%"

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"Cookie {self.color} of {self.weight}g"


Cookie1 = StarCookie("Red", 16)
Cookie2 = StarCookie("Orange", 19)
print(Cookie1.milk)
print(Cookie2.milk)
Cookie1.milk = "15%"
print(Cookie1.milk)
print(Cookie1.__dict__)
print(Cookie2.__dict__)
print(StarCookie.__dict__)
print(Cookie1)


class Youtube:
    def __init__(self, username, subscribers=0, subsriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subsriptions = subsriptions

    def subscribe(self, user):
        user.subscribers += 1
        self.subsriptions += 1


user1 = Youtube("Ramu")
user2 = Youtube("Raju")
user1.subscribe(user2)
print(user1.subscribers)
print(user1.subsriptions)
print(user2.subscribers)
print(user2.subsriptions)
