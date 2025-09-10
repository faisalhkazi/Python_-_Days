class Bird:

    wings = True

    def __init__(self, color, species):
        self.color = color
        self.species = species

    def chirp(self):
        print("tweet")

    def fly(self, feet):
        print(f"The bird flies {feet} feet high")

    def paint_black(self):
        self.color = "Black"
        print(f"Now the bird is {self.color}")

#git
# tweet = Bird("Blue", "Canary")
#
# tweet.paint_black()

    @classmethod
    def lay_egg(cls, number):
        print(f"It laid {number} Eggs")
        cls.wings = False
        print(Bird.wings)

Bird.lay_egg(77)