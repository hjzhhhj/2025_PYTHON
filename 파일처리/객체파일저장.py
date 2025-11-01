import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"이름 : {self.name}\n나이 : {self.age}"
    
f = open("./파일처리/person_data.bin", "wb")

p = Person("철수", 20)

pickle.dump(p, f)

f.close()