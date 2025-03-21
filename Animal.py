class Animal:
    def __init__ (self,name,age,species):
        self.name = name
        self.age = age
        self.species = species

    def make_sound(self):
        print("издает звук")

    def info(self):
        print(self.name)
        print(self.age)
        print(self.species)   

    def __del__ (self):
        print("обьект удален")     


class Dog(Animal):
    def __init__(self,breed,guard_status,name,age,species):
        super().__init__(name,age,species)
        self.breed = breed
        self.guard_status = guard_status

    def info(self):
        print(self.breed)
        print(self.guard_status)
        print(self.name)
        print(self.age)
        print(self.species) 



    def guard_house(self):
        self.guard_status = not self.guard_status  
        if self.guard_status:
            print("защита активирована")
        else:
            print("защита деактивирована")

