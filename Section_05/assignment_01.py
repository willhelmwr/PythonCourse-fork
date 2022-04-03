# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""
# Your Code Below:

class Animal:

    def __init__(self):
        print("\n\nAnimal constructing...")

    def move(self):
        print("animal moves")

    def eat(self):
        print("animal eats")


class Dog(Animal):

    def __init__(self, name, age):
        Animal.__init__(self)
        self.name = name
        self.age = age
        print("I'm a dog!")

    def move(self):
        print("I like to walk and run")



class Bird(Animal):

    def __init__(self, name, age):
        Animal.__init__(self)
        self.name = name
        self.age = age
        print("I'm a bird!")

    def move(self):
        print("I like to fly in the sky")

    # def eat(self):
    #     print("I like to eat seed")

class Fish(Animal):

    def __init__(self, name, age):
        Animal.__init__(self)
        self.name = name
        self.age = age
        print("I'm a fish!")

    def move(self):
        print("I like to swim in the water")
    #
    # def eat(self):
    #     print("I like to eat small seeds")

dog1 = Dog("Reksio", 3)
dog1.move()
dog1.eat()

bird1 = Bird("Kanarek", 2)
bird1.move()
bird1.eat()

fish1 = Fish("Rekin", 1)
fish1.move()
fish1.eat()






# Solution:
# class Animal:
#     def __init__(self):
#         print("Animal Constructed")
#
#     def move(self):
#         print("Animal Moving...")
#
#     def eat(self):
#         print("Animal Eating...")
#
#
#
# class Bird(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Bird flying...")
#
#
#
# class Fish(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Fish Swimming...")
#
#
# class Dog(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Dog Running ...")
#
# mydog = Dog(3, "wolfy")
# mydog.move()
# mydog.eat()
#
# mydog = Fish(1, "nemo")
# mydog.move()
# mydog.eat()
#
# mydog = Bird(3, "jojo")
# mydog.move()
# mydog.eat()