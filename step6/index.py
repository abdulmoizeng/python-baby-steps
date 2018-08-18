# **********         Object Oriented             **************
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
        print("{} is {} cm tall and {} kg and say {}. Owned by {}.".format(self.name, self.height, self.weight, self.sound, self.owner))


dog = Dog('Tommy', 40, 15, 'Bark', 'Obama')
dog.info()
print(dog.get_name())
print(dog.get_height())
print(dog.get_weight())
print(dog.get_sound())
dog.set_owner('Donald Trump')
print(dog.get_owner())
# *****************                     ***********************