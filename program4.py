from dataclasses import dataclass

@dataclass
class Student:
    name: str
    school_id: str
    gpa: float

    #from video
    def __str__(self):
        return f'Name: {self.name}, School ID: {self.school_id} GPA: {self.gpa}'

def main():
    alex = Student('Alex', 'abcedf', 3.4)
    print(alex)
    print(alex.name)
    print(alex.school_id)
    print(alex) 

    sam = Student('Sam', 'xyzxyz', 3.2)
    print(sam)
    print(sam.school_id)
    
if __name__ == '__main__':
    main()


# Over the summer I read a book about object oriented programming,
# I only saw classes made the other way, I had trouble for no reason
# using data classes. I was just so used to the other way of making classes
# Right now I prefer the other way of making classes, but I think I 
# will like data classes more if I use them more.