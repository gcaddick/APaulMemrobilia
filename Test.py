class mammal():
    breastfeed=True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    @classmethod
    def whatisit(cls):
        print("It is a mammal")
    @staticmethod
    def staticmethod(hello):
        print(hello)



person1=mammal("Danyal", 25)
print(person1.getAge())

class Pet(mammal):
    def __init__(self, name, age, kind):
        super().__init__(name,age)
        self.kind=kind
    def setSpecies(self,kind):
        self.kind=kind
    def getSepecies(self):
        return self.kind

Pet1 = Pet("Bodgers", 8, "cat")

print(Pet1.getAge(), Pet1.getSepecies(), Pet1.getName())
print(mammal.breastfeed)
print(person1.breastfeed)
print(person1.whatisit())
print(mammal.staticmethod(hello=""))