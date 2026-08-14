class Demo:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

d = Demo()
print(d.add(1, 2, 3,4   ))

# class Grandparent:
#     def house(self):
#         print("Owns a house")

# class Parent(Grandparent):
#     def car(self):
#         print("Owns a car")

# class Child(Parent):
#     def bike(self):
#         print("Owns a bike")

# c = Child()
# c.house()
# c.car()
# c.bike()

# class Father:
#     def skills(self):
#         print("Driving")

# class Mother:
#     def talents(self):
#         print("Cooking")

# class Child(Father, Mother):
#     pass

# c = Child()
# c.skills()
# c.talents()