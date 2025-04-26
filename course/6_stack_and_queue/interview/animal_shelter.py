# An animal shelter which holds only dogs and cats, operates on a strictly "first in first out" basis. People must either adopt the "oldest" (based on arrival time) of all
# animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal
# they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog and dequeueCat.


class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == "cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueCat(self):
        if len(self.cats) == 0:
            return "No cats are avialable"
        popped = self.cats.pop(0)
        return popped

    def dequeueDog(self):
        if len(self.dogs) == 0:
            return "No dogs are available"
        popped = self.dogs.pop()
        return popped

    def dequeueAny(self):
        if len(self.dogs):
            popped = self.dogs.pop(0)
            return popped
        elif len(self.cats):
            popped = self.cats.pop(0)
            return popped
        else:
            return "No animals were available"


shelter = AnimalShelter()
shelter.enqueue("german shepperd", "dog")
shelter.enqueue("beagle", "dog")
shelter.enqueue("rot wheeler", "dog")
shelter.enqueue("somes", "cat")
print(shelter.dequeueCat())
print(shelter.dequeueCat())
print(shelter.dequeueDog())
print(shelter.dequeueDog())
print(shelter.dogs)
print(shelter.cats)
