# class Dog :
#     def __init__(self,name,age): # to make instance
#         self.name = name  # attribute
#         self.age = age
#         # print(type(name))
#     def get_name(self): 
#             return self.name
#     def get_age(self):
#          return self.age
#     def set_age(self,new_age):
#         self.age = new_age
#     def add_one(self,x):
#         return x+1 
#     def bark(self):
#         print("Woof!")
# d = Dog("Tim",2)
# d2=Dog("Bill",5)
# print(d.name)
# print(d2.name)
# print(d.get_age())
# d.set_age(3)
# # d.bark()
# # print(d.add_one(2))
# # print(type(d))
# class Students :
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade # 0 --> 4
#     def get_info(self):
#         return f"{self.name} is {self.age} years old and is in grade {self.grade}"
#     def get_grade(self):
#         return self.grade
# class Course:
#     def __init__(self,name,max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students=[]
#         self.is_active = False
#     def add_student(self,student):
#         if len(self.students)<self.max_students and student not in self.students:
#             self.students.append(student)
#             return True 
#         else:
#             print("Course is full or student is already in the course")
#             return False
#     def get_average_grade(self):
#         value = 0 
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)
# s1 = Students("Ahmed",19 , 3.47)
# s2 = Students("Sameh",20 , 3.75)
# s3 = Students("Bill",21,3.54)
# course = Course("Science",2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.students[0].name)
# print(course.add_student(s3))
# print(f"{course.get_average_grade():0.2f}")
# class Pet :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(f"{self.name} is {self.age} years old")

# class Cat(Pet): #inherit from pet class
#     def __init__(self, name, age,color):
#         self.color = color
#         super().__init__(name,age)
#     def speak(self):
#         print("Meow!")
#     def show(self):
#         print(f"{self.name} is {self.age} years old and my color is {self.color}")
# class Dog(Pet):
#     def speak(self):
#         print("Woof!")
# class Fish(Pet): #inherit from pet class
#     def swim(self):
#         print("Splash!")
# p = Pet("Tim",4)
# p.show()
# c = Cat("Bill",3,"red")
# c.show()
# f = Fish("Bubbles",2)
# f.swim()
# class Person:
#     number_of_people = 0 #class attr
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Person.add_person()
        
#     @classmethod    
#     def number_of_people_(cls):#class method
#         return cls.number_of_people
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1
# p1 = Person("tim",35)
# p2 = Person("jill",22)
# p3 = Person("jame",32)
# print(Person.number_of_people_())
# class Math:
#     @staticmethod
#     def add5():/
#         return x + 50

