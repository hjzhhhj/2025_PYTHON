price = 0

print("사과 1000원, 배 2000원, 감 3000원, 샤인머스켓 4000원")
print("딸기 5000원, 바나나 6000원, 포도 7000원, 블루베리 8000원")
print("**최소 주문 금액 : 10000원**")

while True:
    fruit = input("\n구매할 과일을 입력해주세요 ( 장바구니 입력 시 종료 ) : ")

    if fruit == "장바구니":
        if price >= 10000:
            print("\n구매가능합니다! 총 금액은", price, "원입니다.")
            break
        else:
            print("\n최소 주문 금액을 채워주세요! 현재 :", price, "원")
            continue

    if fruit == "사과":
        price += 1000
        print("사과를 담았습니다. 현재 :", price, "원")
    elif fruit == "배":
        price += 2000
        print("배를 담았습니다. 현재 :", price, "원")
    elif fruit == "감":
        price += 3000
        print("감을 담았습니다. 현재 :", price, "원")
    elif fruit == "샤인머스켓":
        price += 4000
        print("샤인머스켓을 담았습니다. 현재 :", price, "원")
    elif fruit == "딸기":
        price += 5000
        print("딸기를 담았습니다. 현재 :", price, "원")
    elif fruit == "바나나":
        price += 6000
        print("바나나를 담았습니다. 현재 :", price, "원")
    elif fruit == "포도":
        price += 7000
        print("포도를 담았습니다. 현재 :", price, "원")
    elif fruit == "블루베리":
        price += 8000
        print("블루베리를 담았습니다. 현재 :", price, "원")
    else:
        print("없는 과일입니다. 다시 입력해주세요.")
