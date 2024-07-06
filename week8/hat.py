import random

    # CLASS METHODS
class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # class variables

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry") # acessing a class method inside the class Hat()
