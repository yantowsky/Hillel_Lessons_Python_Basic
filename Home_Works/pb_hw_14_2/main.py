from student import Student
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