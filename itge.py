# class ReverseIterator:
#     def __init__(self, lst):
#         self.lst = lst
#         self.index = len(lst) - 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index < 0:
#             raise StopIteration
#         value = self.lst[self.index]
#         self.index -= 1
#         return value

# lst = [5, 10, 15]
# for item in ReverseIterator(lst):
#    print(item)

def greeting(name):
    def say_hello():
        print(f"Hello, {name}!")
    return say_hello


hello_john = greeting("John")
hello_john()
