Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
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