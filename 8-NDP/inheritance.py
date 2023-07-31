class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        # print("Person created")
    
    def who_am_i(self):
        print("I am a person")

class Student(Person):
    def __init__(self,name,surname,num):
        Person.__init__(self,name,surname)
        self.num = num
        # print("Student created")
    def sayHi(self):
        print("Hello I am a student")

class Teacher(Person):
    def __init__(self,name,surname,branch):
        super().__init__(name,surname)
        self.branch = branch

    def who_am_i(self):
        print(f'I am a {self.branch} teacher')

p1 = Person("K","E")
s1 = Student("K","E",956)
t1 = Teacher("K","E","pc")

print(p1.name + p1.surname)
print(s1.name + s1.surname + str(s1.num))

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()


s1.sayHi()