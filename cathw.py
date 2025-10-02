class Pet:
    species = "Кошка"
    
    def __init__(self, name="Not Given", age=0, hunger=50, energy=50, happiness=50):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness

    def __bool__(self):
        return self.hunger < 80 and self.energy > 20 and self.happiness > 30

    def __str__(self):
        return f"{self.species} {self.name} (возраст {self.age} дн.)"

    def Info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)
        print("Голод:", self.hunger, "/100")
        print("Энергия:", self.energy, "/100")
        print("Счастье:", self.happiness, "/100")

    # Простейшие действия
    def feed(self, amount=20):
        self.hunger = max(0, self.hunger - amount)
        self.happiness = min(100, self.happiness + 5)
        print(f"{self.name} поел(а). Голод теперь {self.hunger}/100")

    def play(self, minutes=15):
        self.energy = max(0, self.energy - minutes//2)
        self.hunger = min(100, self.hunger + minutes//3)
        self.happiness = min(100, self.happiness + minutes//2)
        print(f"{self.name} поиграл(а). Настроение {self.happiness}/100")


p1 = Pet("Темми", age=180, hunger=40, energy=60, happiness=70)

print(bool(p1))
print(p1)
p1.Info()        
p1.feed(25)
p1.play(20)
p1.Info()
