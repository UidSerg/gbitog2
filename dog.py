from animal import Home_animal, Pack_animal

class Dog(Home_animal):
    def __init__(self, name, date):
        super().__init__(name, date, "Гав-гаф")
        self.id_v = 2

    def comand(self):
        print(f'{self.name} виляет хвостом')

    def bd_type(self):
        return self.id_t

class Cat(Home_animal):
    def __init__(self, name, date):
        super().__init__(name, date, "мяу")
        self.id_v = 1

    def comand(self):
        print(f'{self.name} спит')
        
    def bd_type(self):
        return self.id_t

class Hamster (Home_animal):
    def __init__(self, name, date):
        super().__init__(name, date, "молча лопает")
        self.id_v = 3

    def comand(self):
        print(f'{self.name} бегает по клетке')
        
    def bd_type(self):
        return self.id_t

 #### 
class Horse(Pack_animal):
    def __init__(self, name, date):
        super().__init__(name, date, "иигооо")
        self.id_v = 4

    def comand(self):
        print(f'{self.name} бегает по пастбищу')
        
    def bd_type(self):
        return self.id_t
    
class Camel(Pack_animal):
    def __init__(self, name, date):
        super().__init__(name, date, "молчит")
        self.id_v = 5

    def comand(self):
        print(f'{self.name} лежит')
        
    def bd_type(self):
        return self.id_t
    
class Donkey (Pack_animal):
    def __init__(self, name, date):
        super().__init__(name, date, "ийа-иа-йа")
        self.id_v = 5

    def comand(self):
        print(f'{self.name} бегает по лужайке')
        
    def bd_type(self):
        return self.id_t