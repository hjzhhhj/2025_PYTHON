country = input("배송지(현재는 korea와 us만 가능) 입력>> ").lower()

if country == "korea":
    price = int(input("상품 가격 입력>> "))
    if price > 20000:
        print("배송비 = X")
    else:
        print("배송비 = 3000")
elif country == "us":
    price = int(input("상품 가격 입력>> "))
    if price > 100000:
        print("배송비 = X")
    else:
        print("배송비 = 8000")
else:
    print("한국 미국만 배송가능합니다.")