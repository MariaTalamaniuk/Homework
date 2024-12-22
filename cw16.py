# наслідування
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return 'Гав-гав!'

class Cat(Animal):
    def sound(self):
        return 'Мяу-мяу!'

animals = [Dog(),Cat()]

for animal in animals:
    print(animal.sound())