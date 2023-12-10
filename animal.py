class Home_animal:
    def __init__(self, name, date, sound):
        self.name = name
        self.date = date
        self.sound = sound
        self.type = "Домашнее"
        self.id_t = 1

    def animal_info (self):
        print(f'{self.name} {self.type} животное родился {self.date} издает звук "{self.sound}"')

class Pack_animal:
    def __init__(self, name, date, sound):
        self.name = name
        self.date = date
        self.sound = sound
        self.type = "Въючное"
        self.id_t = 2

    def animal_info (self):
        print(f'{self.name} {self.type} животное родился {self.date} издает звук "{self.sound}"')