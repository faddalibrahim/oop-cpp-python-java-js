# dir("")  attributes and methods of a class
# help("") documentation of a class

class Apple:
    pass


class Apple:
    color = ""
    flavor = ""


jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"

print(jonagold.flavor)
print(jonagold.color)


class Piglet:
    name = "piglet"
    years = 0

    def speak(self):
        print("oink! I'm {}!".format(self.name))

    def pig_years(self):
        return self.years * 18


hamlet = Piglet()
hamlet.speak()


class Banana:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    # By defining the str method, we are telling python what we want to display when print is called
    # its similar to implementing a toString method in java
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color,self.flavor)


bonagold = Banana("orange", "sour")
print(bonagold.color)

# when we use str or print() to convert objects to strings, we are using useful special method

# what happens when we don't define one
print(bonagold)  # this prints memory address of object
