class Dog:

    species = 'Canis familiaris'

    def __init__(self, name: str, age: int):
        self.name = name
        # self.set_age(age)
        # skladowe prywatne
        self.age = age
        '''
        if type(age) == int:
            # __age uniemozliwia modyfikacje spoza klasy
            self.__age = age
        # to nie zabezpiecza przed pozniejsza bledna modyfikacja zmiennej
        else:
            raise TypeError
        '''

    def description(self):
        older = self.__age + 1
        return f'{self.name} is {older} years old'
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if type(age) == int:
            self.__age = age
        else:
            raise TypeError('Bledny typ argumentu')
    
    def speak(self, sound = 'Arf'):
        return f'{self.name} says {sound}'
    
    def __str__(self):
        return self.description()

#d = Dog('Reksio', 'trolololo')
e = Dog('Reksio', 3)
f = e
#d.name = 'Burek'
e.name = 'Kicia'
#d.age
e.species = 'Golab'

Dog.species = 'Wrobel'

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(f"fffffffffff {sound} !!!!!!!!!!!!!")
class Dachshund(Dog):
    def speak(self, sound="Arf"):
        return "Zawsze szczekam tak samo"
class Bulldog(Dog):
   def speak(self, sound="Wrrrrrrrr!"):
       return super().speak(sound)

if __name__ == '__main__':
    r = Dog('Reksio', 3)
    b = Dog('Burek', 5)
    bb = Bulldog('Bulldog',10)
    jr = JackRussellTerrier('Jack', 4)
    da = Dachshund('Dachshund', 2)

    lista = [bb, jr, da, r, b]

    for pies in lista:
        print("_________________________")
        print(type(pies))   #😍[]
        print(pies.speak())
