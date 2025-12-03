>>> class Roommate:
...     def __init__(self, name, age, gender, height, complexion, hobby):
...         self.name = name
...         self.age = age
...         self.gender = gender
...         self.height = height
...         self.complexion = complexion
...         self.hobby = hobby
... 
...     def show_details(self):
...         print("Roommate Details:")
...         print("Name:", self.name)
...         print("Age:", self.age)
...         print("Gender:", self.gender)
...         print("Height:", self.height)
...         print("Complexion:", self.complexion)
...         print("Hobby:", self.hobby)
... 
... mate = Roommate("Shanice", 20, "Female", "169", "Dark", "Singing")

...mate.show_details()
