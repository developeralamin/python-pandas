class MainClass:
    def __init__(self):
        self.name = "John"
        self.age = 20
        self.gender = "male"

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")



main = MainClass()
main.say_hello()