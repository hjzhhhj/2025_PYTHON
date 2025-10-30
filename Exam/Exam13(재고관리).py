class StockError(Exception):
    pass

class PriceError(Exception):
    pass

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        if price < 0:
            raise PriceError("가격은 -일 수 없습니다.")
        self.price = price
        if quantity < 0:
            raise StockError("재고는 -일 수 없습니다.")
        self.quantity = quantity

    def set_price(self, price):
        if price < 0:
            raise PriceError("가격은 -일 수 없습니다.")
        self.price = price

    def add_stock(self, amount):
        if amount < 0:
            raise StockError("추가할 재고는 0보다 커야합니다.")
        self.quantity += amount

    def remove_stock(self, amount):
        if amount > self.quantity:
            raise StockError("재고가 부족합니다.")
        self.quantity -= amount

    def total_value(self):
        return f"현 재고의 총 가치 : {self.price * self.quantity}원"

    def __str__(self):
        return f"상품명: {self.name}, 가격: {self.price}원, 재고: {self.quantity}개"
    
try:
    product = Product("꿀맛과자!", 1000, 10)
    print(product)

    product.set_price(1200)
    print(product)

    # product.set_price(-1200)  
    # print(product)

    product.add_stock(5)
    print(product)

    # product.add_stock(-5)  
    # print(product)

    product.remove_stock(5)
    print(product)

    # product.remove_stock(20)  
    # print(product)

    print(product.total_value())

except StockError as e:
    print(e)
except PriceError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)