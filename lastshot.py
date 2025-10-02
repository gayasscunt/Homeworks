# # Задание первое
# class Animal:
#     def speak(self):
#         raise NotImplementedError("Error! You forgot who should speak.")
# class Dog(Animal):
#     def speak(self):
#         return "Dog says: Woof!"
# class Cat(Animal):
#     def speak(self):
#         return "Cat says: Meow!"
# class Parrot(Animal):
#     def speak(self):
#         return "Parrot says: I'm a pirate!"

# # Задание 2
# def who_am_i(obj):
#     print("Тип объекта:", type(obj))
#     print("Атрибуты и методы:", dir(obj))
#     if type(obj).__module__ == 'builtins':
#         print("Это встроенный тип.")
#     else:
#         print(f"Это не встроенный тип и его модуль: {type(obj).__module__}).")

# # Задание 3
# import sys

# def main():
#     print("Версия Python:", sys.version)
#     print("Путь к Python:", sys.executable)
#     print("Аргументы командной строки:", sys.argv)
#     print("Имя платформы:", sys.platform)

# if __name__ == "__main__":
#     main()

def calculator():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        operation = input("Введите операцию (+, -, *, /): ")

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            try:
                result = a / b
            except ZeroDivisionError:
                print("Ошибка: деление на ноль!")
                return
        else:
            print("Ошибка: неизвестная операция!")
            return

        print("Результат:", result)

    except ValueError:
        print("Ошибка: введено не число!")

if __name__ == "__main__":
    calculator()
