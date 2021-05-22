# The 4 Pillars of Object-Oriented Programming

- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

# Links

1. [FreeCodeCamp - Intro to Object Oriented Programming](https://www.youtube.com/watch?v=SiBw7os-_zI)

2. [Mosh - Object Oriented Programming in 7 minutes](https://www.youtube.com/watch?v=pTB0EiLXUC8)

3. [Keep on Coding - Object Oriented Programming : The four Pillars of OOP](https://www.youtube.com/watch?v=1ONhXmQuWP8)

# Summary
## 1. **Encapsulation**
means grouping related variables and functions that operate on them into objects

- reduces complexity
- increases re-usability

Furthermore, with encapsulation, we hide data from the outside scope. We expose the data for interaction with the outside using **getters** and **setters**

with setters

- we can validate inputs before mutating our attributes
- set other values that depend on what is being set
for example, if we are setting the date of birth, we can automatically deduce the zodiac sign and set it. No need to have a separate method to set the zodiac. Since it directly depends on date of birth, we set its value as of when we have the date of birth.

with getters,

- we may want certain attributes to be read only


```javascript
// instead of this (which exposes our data to the global scope)
let name = "Faddal Ibrahim",
	age = 21,
	school = "Ashesi University";
    
function speak(name,age,school){
 console.log(`my name is ${name}. I am ${age}. I attend ${school}`
}

// we do this (capture the data and its related functions in one object)
let student = {
	name: "Faddal Ibrahim",
	age: "21",
	school: "Ashesi University"
	speak(){
		console.log(`my name is ${this.name}. I am ${this.age}. I attend ${this.school}`
	}
}
```

## 2. **Abstraction**
means hiding complexities and exposing only the essentials

reduce complexity, hide details, and expose essential parts

For example user.authenticate("Michael") may look simple and easier to call but does some complex processes behind the scenes. The processes may include, reaching out to a database, validating the input etc. but all these are hidden and summarized into just one method (authenticate). the user of our method doesn't have to worry about its intricacies.

## 3. **Inheritance**

Eliminating redundant code

html elements like textbox,select,checkbox have things in common - properties such as hidden and innerHTML; methods such as click() and focus(). Instead of redefining all these methods and properties for every html element, we can define them once in a generic object. Then allow all other elements to inherit them. Interestingly, each element can also have its own unique properties and methods as well.

## 4. **Polymorphism**

Allows us to change the behavior of a method with respect to the type of object being referenced

for example, all html elements have a render method but the way each element is rendered differs. we can't define a generic method that works for all.

we can make them all have the same method name but the body of the method and what it does would be suitable for that particular element.

in this case we dont have to create multiple if or switch statements to handle for different cases of the render element.

> dynamic polymorphism

- occurs during runtime
- method signature is present in both super and subclass
- methods have the same name but different implementations
- child class method overrieds its parent's

> static polymorphism

- occurs during compile-time
- multiple methods of same name but different arguments are defined in the same class. Examples can be seen in (constructors, method overloading - number, type, order of arguments)