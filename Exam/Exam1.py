price = 0

while True:
    print("\n1. 사과 : 1000원, 2. 배 2000원, 3. 감 3000원, 4. 샤인머스켓 4000원\n5. 딸기 5000원, 6. 바나나 6000원, 7. 포도 7000원, 8. 블루베리 8000원")
    print("최소 주문 금액 : 5000원")
    buy = int(input("구매할 과일의 번호를 입력해주세요! : "))

    if ( buy == 1 ) : price += 1000
    elif ( buy == 2 ) : price += 2000
    elif ( buy == 3 ) : price += 3000
    elif ( buy == 4 ) : price += 4000
    elif ( buy == 5 ) : price += 5000
    elif ( buy == 6 ) : price += 6000
    elif ( buy == 7 ) : price += 7000
    elif ( buy == 8 ) : price += 8000

    answer = input(str(price)+"원 담겼습니다. 주문을 종료하시겠습니까? ( Y / N ) : ")

    if answer == "Y" :
        if price < 5000 : print("\n최소 주문 금액을 채워주세요! 현 금액 : "+str(price))
        else : break