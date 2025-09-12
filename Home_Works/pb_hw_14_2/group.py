class LimitGroupError(Exception):
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
        all_students = '\n'.join(map(str, self.group))
        return f'Group Number: {self.number}\n{all_students}'
