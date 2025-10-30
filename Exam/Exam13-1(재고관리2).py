class ProductNotFoundError(Exception):
    pass

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

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.name in self.products:
            self.products[product.name].add_stock(product.quantity)
        else:
            self.products[product.name] = product

    def remove_product(self, name: str, amount: int):
        if name not in self.products:
            raise ProductNotFoundError(f"{name}을(를) 찾을 수 없습니다.")
        self.products[name].remove_stock(amount)
        if self.products[name].quantity == 0:
            del self.products[name]

    def set_price(self, name: str, new_price: int):
        if name not in self.products:
            raise ProductNotFoundError(f"{name}을(를) 찾을 수 없습니다.")
        self.products[name].set_price(new_price)

    def get(self, name: str) -> Product:
        if name not in self.products:
            raise ProductNotFoundError(f"{name}을(를) 찾을 수 없습니다.")
        return self.products[name]

    def total_inventory_value(self) -> int:
        return f"창고 전체 재고 가치: {sum(product.price * product.quantity for product in self.products.values())}원"

    def __str__(self):
        if not self.products:
            return "창고가 텅~ 비어 있습니다."
        return "\n".join(str(product) for product in self.products.values())

inventory = Inventory()

try:
    product1 = Product("픽셀리네꿀단지스낵", 2500, 2)
    product2 = Product("젼언니스윗믹스젤리", 3000, 1)
    inventory.add_product(product1)
    inventory.add_product(product2)
    print(inventory, "\n")

    inventory.set_price("픽셀리네꿀단지스낵", 2000)
    print(inventory, "\n")

    inventory.remove_product("젼언니스윗믹스젤리", 1)
    print(inventory, "\n")

    print(inventory.total_inventory_value(), "\n")

    inventory.remove_product("우웩", 1) 

except (ProductNotFoundError, StockError, PriceError) as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
