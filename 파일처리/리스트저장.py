import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"이름 : {self.name}\n나이 : {self.age}"
    
p1 = Person("철수", 20)
p2 = Person("영희", 21)
p3 = Person("주영", 22)

persons = [p1, p2, p3]

f = open("./파일처리/person_data.bin", "wb")

pickle.dump(persons, f)

f.close()