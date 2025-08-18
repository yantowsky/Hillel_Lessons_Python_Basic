def say_hi(name: str, age: int) -> str:
    string_say_hi = f"Hi. My name is {name} and I'm {age} years old"
    return string_say_hi


assert say_hi(name="Alex", age=32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi(name="Frank", age=68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')
