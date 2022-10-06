
import time
import pickle
import pickletools

class User:
    def __init__(self, age=25, name="lockcy"):
        self.age = age
        self.name = name

    def say(self):
        print("hello")

    def sleep(self):
        print("start to sleep")
        time.sleep(2)
        print("end sleeping")


if __name__ == '__main__':
    u = User()
    data = pickle.dumps(u)
    print(data)
    data = b'\x80\x04\x955\x00\x00\x00\x00\x00\x00\x00\x8c\x08' \
           b'__main__\x94\x8c\x04User\x94\x93\x94)\x81\x94}\x94(\x8c\x03age\x94K\x19\x8c\x04name\x94\x8c\x06lockcy\x94ub.'
    pickletools.dis(data)
