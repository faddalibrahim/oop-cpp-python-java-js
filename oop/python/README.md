# Links

1. Introduction to Python : Google IT Automation Course
2. [OOP in python - Traversy Media](https://www.youtube.com/watch?v=MikphENIrOo)

```python
dir("hello")
help(12)
```

> Python class

```python
class Fruit:
    pass
```

> Python class with attributes

```python
class Fruit:
    color = ""
    flavor = ""
```

> Access Modifiers

\_protected (preceded by single underscore)
still accessible and modifiable outside the class scope by any instance of the class

\_\_private (preceded by double underscore)
still accessible and modifiable via 'instance.\_Class\_\_privateValue'
python only mangles the name

```python
class Fruit:
    _color = ""
    __flavor = ""
```

> Python class with initialized attributes and methods

```python
class Fruit:
    color = "crimson"

    def speak(self):
        print("Krrrr! I'm {}!".format(self.color))

    def fruit_years(self):
        return self.years * 12
```

> Python class with constructor and special method

```python
class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This fruit is {} and its flavor is {}".format(self.color,self.flavor)


bonagold = Banana("orange", "sour")

# without the __str__ special method, the print function would only print the memory location of the object

# Think of the __str__ special method as an implementation of the toString() method in java
print(bonagold.color)

```

> Documenting your functions, classes and methods using docstrings

```python
class Fruit:
    """Represents a fruit that can speak"""

    def speak(self):
        """Outputs a message including the color of the piglet"""
        print("Krrrr! I'm {}!".format(self.color))
```

> Inheritance

```python
class Fruit:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

afri_apple = Apple("green","tart")
afri_grape = Apple("pink","sour")
```

> Composition

```python
class Repository:
    def __init__(self):
        self.packages = {}

    def add_package(self,package):
        self.packages[package.name] = package

    def total_size(self):
        result = 0
        for package in self.package.values():
            result += package.size
        return result
```
