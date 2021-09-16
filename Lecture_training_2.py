class person:
    def __init__(self):
        print("person class")
        self.hello = "hello"

class student(person):
    def __init__(self):
        print("student class")
        super().__init__()
        self.school = "JBNU"

james = student()
print(james.hello)

class family:
    lastname = "Kim"
family.lastname = "Moon"

a = family()
b = family()

print(a.lastname)
print(b.lastname)
