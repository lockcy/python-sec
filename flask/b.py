
import pickle
import pickletools

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name}\nage: {self.age}"


class Child(Person):
    def __setstate__(self, state):
        print("invoke __setstate__")
        self.name =state
        self.age =10

    def __getstate__(self):
        print("invoke __getstate__")
        return "Child"


c1 =Child("TEST")
print(c1)
# name: TEST
# age: 0

opcode =pickle.dumps(c1 ,protocol=0)
print(opcode)
# invoke __getstate__
# b'ccopy_reg\n_reconstructor\np0\n(c__main__\nChild\np1\nc__builtin__\nobject\np2\nNtp3\nRp4\nVChild\np5\nb.'

c2 =pickle.loads(opcode)
print(c2)
# invoke __setstate__
# name: Child
# age: 10