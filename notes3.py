# One way to do this is to represent each employee as a list:

kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]
student = ["shivam",103,"average",363563]


class father:
    # class attribute
    humanities = "little bit"
    
    def __init__(self,species,planet):
        self.species=species
        self.planet=planet
        
        
  
        
        


class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
        

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
miles = Dog("Miles", 4)

miles.description()
# 'Miles is 4 years old'

miles.speak("Woof Woof")
# 'Miles says Woof Woof'

miles.speak("Bow Wow")
# 'Miles says Bow Wow'




class Dog:
    # Leave other parts of Dog class as-is

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        
miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

buddy.speak("Yap")
# 'Buddy says Yap'

jim.speak("Woof")
# 'Jim says Woof'

jack.speak("Woof")
# 'Jack says Woof'

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)


miles.species
# 'Canis familiaris'
buddy.name
# 'Buddy'

print(jack)
# Jack is 3 years old

jim.speak("Woof")
# 'Jim says Woof'
