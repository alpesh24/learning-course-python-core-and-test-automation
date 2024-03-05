# Complete the following code according to the task in README.md.
# Don't change names of classes. Create names for the variables
# exactly the same as in the task.
class SchoolMember:
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age
    
    def show(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"


class Teacher(SchoolMember):
    def __init__(self, name: str, age: int, salary:int) -> None:
        super().__init__(name, age)
        self.salary = salary
    
    def show(self) -> str:
        return super().show() + f", Salary: {self.salary}"


class Student(SchoolMember):
    def __init__(self, name: str, age: int, grades) -> None:
        super().__init__(name, age)
        self.grades = grades

    def show(self) -> str:
        return super().show() + f", Grades: {self.grades}"


teacher = Teacher("Mr.Snape", 40, 3000)
print(teacher.name)

persons = [teacher, Student("Harry", 16, 75)]
for person in persons:
    print(person.show())