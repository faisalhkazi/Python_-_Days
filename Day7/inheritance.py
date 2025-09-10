# This is the example of inheritance to understand better

class Father:

    def talk(self):
        print("Hello")

    def laugh(self):
        print("Ha Ha Ha")


class Mother:

    def laugh(self):
        print("Ha Ha")

class Child(Father, Mother):

    def talk(self):
        print("How are you?")

class Granchild(Child):

    pass

my_grandchild = Granchild()

my_grandchild.talk()

my_grandchild.laugh()       #So, Grandchild can inherit from Child which is getting inherited from both Mother and Father. So, he will get all the values

