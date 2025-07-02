temps = []

for i in range(4):
    o = float(input(f"{i+1}월의 평균 온도 : "))
    
    # 자동 내림차순 정렬 삽입
    inserted = False
    for j in range(len(temps)):
        if o > temps[j]:  # 새 온도가 더 크면 그 자리에 끼워넣기
            temps.insert(j, o)
            inserted = True
            break
    if not inserted:  # 끝까지 돌았는데 더 큰 게 없으면 맨 뒤에 추가
        temps.append(o)

print(f"내림차순으로 정렬된 평균 온도: {temps}")
