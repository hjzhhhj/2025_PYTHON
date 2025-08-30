class Car:
    count = 0
    def __init__(self, type, speed):
    self.type = type
    self.speed = speed
    Car.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
    
print(Car.get_count())
c1 = Car(ˮ스포츠카ˮ, 100)
c2 = Car(ˮ트럭ˮ, 50)
print(Car.get_count())  