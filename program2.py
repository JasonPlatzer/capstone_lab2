class Student:
    def __init__(self, name, school_id, gpa):
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self):
        return f'Student name: {self.name}, school id: {self.school_id}, gpa = {self.gpa}'


alex = Student('Alex', 'abcdef', '3.0')
# print(alex.name)
# print(alex.school_id)
print(alex)
alex.gpa = '4.0'
print(alex)
tom = Student('Tom', 'xyzxyz', ' 3.2')
print(tom)
tom.gpa = '3.4'
print(tom)