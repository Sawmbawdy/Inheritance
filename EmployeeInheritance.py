class Person(object):
    def __init__(self, Name, Id):
        self.Name = Name
        self.Id = Id

    def display(self):
        print("The Name is:", self.Name,"and the Id is", self.Id)

class Employee(Person):
    def __init__(self, Name, Id, Salary, Post):
        self.Salary = Salary
        self.Post = Post
        Person.__init__(self, Name, Id)

Rahul = Employee('Rahul', '001020', 20001, 'Intern')

Rahul.display()