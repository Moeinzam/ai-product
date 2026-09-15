class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
            print(f"My name is {self.name} and my age is {self.age}")

user = User("Moein", 29)
user.introduce()