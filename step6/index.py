# Object Oriented Programming in Python
class Animal:
    __name = ''
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.name = name
        self.height = height
        self.weight = weight
        self.sound = sound

    def set_name(self, name):
        self.name = name

    def set_height(self, height):
        self.height = height

    def set_weight(self, weight):
        self.weight = weight

    def set_sound(self, sound):
        self.sound = sound

    def get_name(self):
        return self.name

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_sound(self):
        return self.sound

    def info(self):
        print("{} is {} cm tall and {} kg and say {}.".format(self.name, self.height, self.weight, self.sound))


cat = Animal('Whiskers', 33, 10, 'Meow')
cat.info()
print(cat.get_name())
print(cat.get_height())
print(cat.get_weight())
print(cat.get_sound())


# Inheritance

class Dog(Animal):
    __owner = ''

    def __init__(self, name, height, weight, sound, owner):
        self.owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.owner = owner

    def get_owner(self):
        return self.owner

    def info(self):
        print("{} is {} cm tall and {} kg and say {}. Owned by {}.".format(self.name, self.height, self.weight,
                                                                           self.sound, self.owner))


dog = Dog('Tommy', 40, 15, 'Bark', 'Obama')
dog.info()
print(dog.get_name())
print(dog.get_height())
print(dog.get_weight())
print(dog.get_sound())
dog.set_owner('Donald Trump')
print(dog.get_owner())

# Abstract Class
"""
Abstract Base Classes or ABCs are the classes that contains at least one or more abstract methods. Initially
there was no support for such classes in Python but in Python 3.0 they added a package called abc to make
Abstract classes.
"""

from abc import ABCMeta, abstractmethod


class AbstractHuman:

    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def type(self): pass

    @abstractmethod
    def introduction(self):
        print('Hello All')

    @abstractmethod
    def set_name(self, name): pass

    @abstractmethod
    def get_name(self): pass

    __metaclass__ = ABCMeta

    name = property(get_name, set_name)


class Man(AbstractHuman):

    def __init__(self, name):
        self._name = name

    def name(self):
        return self.name

    def type(self):
        print("I am a Man")

    def introduction(self):
        super(Man, self).introduction()
        print("My name is {} . I am a man ".format(self.name))

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    name = property(get_name, set_name)


osama = Man(name="Osama")

osama.type()
osama.introduction()


# @property decorator
class Employee(object):

    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, full_name):
        self.first_name, self.last_name = full_name.split(' ')

    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None
        print('Full Name deleted')


emp1 = Employee(first_name='Osama', last_name='bashir', id=1)
print(emp1.full_name)

emp1.full_name = 'Osama Bashir'
print(emp1.full_name)

del emp1.full_name  # del keyword is use for removing or to de-init an object from memory.
print(emp1.full_name)
