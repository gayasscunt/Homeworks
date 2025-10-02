class Car:
    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def info(self):
        print(f"Машина: {self.brand} {self.model}, номер {self.number}")

    def start_engine(self):
        print(f"{self.brand} {self.model} с номером {self.number} стоит в гараже дома")


class Pet:
    def __init__(self, name, typee, sound):
        self.name = name
        self.typee = typee
        self.sound = sound
    
    def play_sound(self):
        print(f"{self.typee} по имени {self.name} говорит: {self.sound}")

class Human:
    def __init__(self, name, age, pets = None,):
        self.name = name
        self.age = age
        self.pets = []
    
    def getpet(self, pet):
        if isinstance(pet, Pet):
            print(f"Невозможно взять к себе питомца.")
            return
        else:
            print(f"{self.name} взял к себе {pet}")
            self.pets.append(pet)
        
    def play_with_pets(self):
        if self.pets:
            print(f"{self.name} играет с питомцами: ")
            for pet in self.pets:
                pet.play_sound()
        else:
            print(f"У {self.name} нет питомцев чтобы играть с ними")


class House:
    def __init__(self,adress):
        self.adress = adress
        self.peoples = []
    def move_in(self,human):
        if not isinstance(human,Human):
            print("Пеерезд невозможен, детка!")
        else:
            self.peoples.append(human)
            print(f"Переезд был сделан")
    
    def who_lives(self):
        if self.peoples:
            print("Тут живут:")
            for people in self.peoples:
                print(people.name)
                if people.pets:
                    print("А еще питомцы: ")
                    for pet in people.pets:
                        print(pet.name)
        else: print("Никого нет")
        
bob.play_with_pets()
bob.getpet(murzik)
bob.play_with_pets()

dom1 = House("Syganak 47")
dom1.who_lives()
dom1.move_in(bob)
dom1.who_lives()

car1 = Car("Toyota", "Corolla", "MPW0294023")
car1.info()
car1.start_engine()