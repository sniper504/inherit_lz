from Animal  import Animal
from Animal import Dog


animal = Animal("Общее животное", 1, "Неизвестный вид")
animal.make_sound()
animal.info()

dog = Dog("Овчарка", True, "Бобик", 5, "Собака")
dog.info()
dog.guard_house()

