class Transport:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        print(f"Оно является транспортом: {self.brand} {self.model}")


class Car(Transport):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def info(self):
        super().info()
        print(f"Это автомобиль с {self.doors} дверями")

    def drive(self):
        print(f"{self.brand} {self.model} едет по дороге")


class Bike(Transport):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    def info(self):
        super().info()
        print(f"Это велосипед типа: {self.bike_type}")

    def ride(self):
        print(f"{self.brand} {self.model} ездит")
