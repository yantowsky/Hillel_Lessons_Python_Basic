import zipfile

# Creating a zip archive
with zipfile.ZipFile('pb_hw_14_2.zip', 'w') as my_zip:
    # Add human.py
    my_zip.writestr('pb_hw_14_2/human.py', '''class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}"
''')

    # Add student.py
    my_zip.writestr('pb_hw_14_2/student.py', '''from human import Human

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

    def __eq__(self, other):
        return isinstance(other, Student) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))
''')

    # Add group.py
    my_zip.writestr('pb_hw_14_2/group.py', '''class LimitGroupError(Exception):
    pass


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise LimitGroupError(f"Unable to add {student.first_name} {student.last_name} to Group: {self.number}."
                                  f" There are already {len(self.group)} students in this group.")
        self.group.add(student)

    def delete_student(self, last_name):
        self.group.discard(self.find_student(last_name))

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\\n'.join(map(str, self.group))

        return f"Group Number: {self.number}\\n{all_students}"
''')

    # Add main.py
    my_zip.writestr('pb_hw_14_2/main.py', '''from student import Student
from group import Group, LimitGroupError

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st3 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st4 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st5 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st6 = Student('Male', 19, 'John', 'Doe', 'AN146')
st7 = Student('Female', 20, 'Mary', 'Johnson', 'AN147')
st8 = Student('Male', 21, 'Alex', 'Smith', 'AN148')
st9 = Student('Female', 22, 'Emma', 'Brown', 'AN149')
st10 = Student('Male', 23, 'Michael', 'Davis', 'AN150')
st11 = Student('Female', 24, 'Sophia', 'Miller', 'AN151')
st12 = Student('Male', 26, 'Daniel', 'Wilson', 'AN152')
st13 = Student('Female', 27, 'Olivia', 'Moore', 'AN153')
st14 = Student('Male', 28, 'James', 'Taylor', 'AN154')

gr = Group('PD1')

try:
    for stds in [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11, st12, st13, st14]:
        gr.add_student(stds)
except LimitGroupError as e:
    print(e)
finally:
    print(gr)

assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None
print('Tests OK')
''')

    # Add __init__.py
    my_zip.writestr('pb_hw_14_2/ __init__.py', '')

print("The zip archive has been created")
