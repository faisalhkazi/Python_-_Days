#This is the example of the polumorphism

class Cow:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(self.name + " MOOS")

class Sheep:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(self.name + " BOOOO")

cow1 = Cow("Messi")
sheep1 = Sheep("Ronaldo")

cow1.talk()
sheep1.talk()