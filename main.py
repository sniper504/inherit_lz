from Animal  import Animal
from Animal import Dog


animal = Animal("Общее животное", 0, "Неизвестный вид")
animal.make_sound()
animal.info()

dog = Dog("Овчарка", False, "Бобик", 5, "Собака")
dog.info()
dog.guard_house()


