import math
from abc import ABC, abstractmethod

class Person:
    def __init__(self):
        self._age = 0

    def set_age(self, age):
        if age < 0:
            print("Ошибка: Возраст не может быть отрицательным!")

        else:
            self._age = age

    def get_age(self):
        return self._age

p = Person()
p.set_age(25)
print(f"Возраст человека: {p.get_age()}")
p.set_age(-5)

print("-" * 20)

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog("Buddy")
cat = Cat("Kitty")
print(f"{dog.name} говорит: {dog.speak()}")
print(f"{cat.name} говорит: {cat.speak()}")

print("-" * 20)

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()

car = Car()
bike = Bicycle()
print(f"Автомобиль: {move(car)}")
print(f"Велосипед: {move(bike)}")

print("-" * 20)

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

rect = Rectangle(4, 5)
circ = Circle(3)
print(f"Площадь прямоугольника (4x5): {rect.area()}")
print(f"Площадь круга (r=3): {circ.area()}")

