class Dog():
    def __init__(self,name,age,colour):
        self.name = name
        self.age = age
        self.colour = colour

    def jump(self): 
       print(f"{self.name} JUMP !!!!!!!")
       print(f"{self.name} is jumping ..........")

    def owner(self):
        print(f"My dog is called {self.name},it is {self.age} year old and its {self.colour} in colour")

class puppy(Dog):
    def __init__ (self,name,age,colour):
        super(). __init__(name,age,colour)



gemern_puppy = puppy("Jess","14","Brown")
gemern_puppy.jump()






#german_shepherd = Dog("Rex",3,"blue")
#bull_dog = Dog("Simba",5,"White")

#german_shepherd.owner()
#bull_dog.jump()
#german_shepherd.owner()
