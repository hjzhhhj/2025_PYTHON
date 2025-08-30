class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def set_numerator(self, numerator):
        self.numerator = numerator
    
    def set_denominator(self, denominator):
        self.denominator = denominator

    def add(self, other):
        if self.denominator == other.denominator:
            new_numerator = self.numerator + other.numerator
            return Fraction(new_numerator, self.denominator)
        
    def sub(self, other):
        if self.denominator == other.denominator:
            new_numerator = self.numerator - other.numerator
            return Fraction(new_numerator, self.denominator)
        
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
f1 = Fraction(1, 2)
f2 = Fraction(1, 2)

print(f"f1: {f1}")
print(f"f2: {f2}")

result_add = f1.add(f2)
print(f"f1 + f2 = {result_add}")

result_sub = f1.sub(f2)
print(f"f1 - f2 = {result_sub}")