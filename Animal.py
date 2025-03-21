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

    def info_d(self):
        print(self.breed)
        print(f"Защитный статус: {'Активирован' if self.guard_status else 'Деактивирован'}")
        print(self.name)
        print(self.age)
        print(self.species) 



    def guard_house(self):
        if self.guard_status:
            self.guard_status = False
            print("защита деактивирована")
        else:
            self.guard_status = True
            print("защита активирована")