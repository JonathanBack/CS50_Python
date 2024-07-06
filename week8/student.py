
def main():
   student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw" # this only works with lists, not tuples
    print(f"{student[0]} from {student[1]}")

#def get_name():
    return input("Name: ")

#def get_house():
    return input("House: ")

    # Returning a tuple with name and house, instead of doing different functions
#def get_student():
    #name = input("Name: ")
    #house = input("House: ")
    #return (name, house)  # returning ONE value, which is a tuple
    # a tuple is very similar to a list, but it is IMMUTABLE, you can not change the values inside a tuple
    # TypeError: 'tuple' object does not support item assignment

    #return [name, house] # this is EXPLICITY a list, which is MUTABLE, you can assign values


    # using dictionaries instead of lists of tuples
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f'{student["name"]} from {student["house"]}')

def get_student():

    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

    name = input("Name: ")
    house = input("House: ")

    return {"name": name, "house": house} # you can return a dictionary instead of creating an empty one and filling it

if __name__ == "__main__":
    main()
    # Classes


    # this is the blueprint that will be modified to construct objects

class Student: # here you create a class which is your own data type, and comes with methods
    def __init__(self, name, house, patronus): #__init__ is an instance method.
    # this is the initialization method, initializes the object for you
        # raising exceptions during the initialization of the object
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name    # assign the values name and house to instance variables of an object, which is an instance of a class
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
         match self.patronus:
            case "Stag":
                return "🐴"

            case "Otter":
                return "🦦"

            case "Jack Russel terrier":
                 return "🐶"

            case _: # default case
                 return "🪄"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus) # giving arguments to the Student() class to construct an object


class Student: # here you create a class which is your own data type, and comes with methods
    def __init__(self, name, house): #__init__ is an instance method.
    # this is the initialization method, initializes the object for you
        # raising exceptions during the initialization of the object


        # this is unecessary now because the setter will check this exceptions
        #if not name:
            #raise ValueError("Missing name")
        #if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            #raise ValueError("Invalid house")

        self.name = name    # assign the values name and house to instance variables of an object, which is an instance of a class
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name
        
    # Getter (gets an atribute)
    @property
    def house(self):
        return self._house

    # Setter (sets some value). Does not allow to access self.house and assign to a new value skipping the steps bellow
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) # giving arguments to the Student() class to construct an object

if __name__ == "__main__":
    main()

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()
