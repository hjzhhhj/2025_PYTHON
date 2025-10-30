class TooLongNameError(Exception):
    pass

class NegativeAgeError(Exception):
    pass

class Person:
    def __init__(self, name, age):
        if len(name) > 20:
            raise TooLongNameError("이름이 Too Long입니다.")
        if age < 0:
            raise NegativeAgeError("나이는 음수일 수 없습니다.")
        
        self.name = name
        self.age = age
        print(f"이름 : {self.name}, 나이 : {self.age}")

try:
    person1 = Person("정희진", 30)  
    person2 = Person("기태기태기태기태기태기태기태연", 30) 
    person3 = Person("김이레", -5)

except TooLongNameError as e:
    print(e)
except NegativeAgeError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)

