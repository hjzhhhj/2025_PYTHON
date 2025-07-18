STUDENTS = 5
data = []
count = 0

for i in range(STUDENTS):
    value = int(input("성적을 입력하세요: "))
    data.append(value)

print("성적 평균= ", sum(data) / len(data))
print("최대점수= ", max(data))
print("최소점수= ", min(data))

# count = len([score for score in data if score >= 80])  # 리스트 컴프리헨션
# count = len(list(filter(lambda x: x >= 80, data)))      # 필터 함수

for score in data:  # for 활용
    if score >= 80:
        count += 1
print("80점 이상= ", count)
