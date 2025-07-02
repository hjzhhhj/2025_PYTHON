name = ["강일", "박삼", "정오", "이칠", "김이", "김사", "장육", "이팔", "hi"]
name.sort()  # 이름순 정렬
lst = []     # 결과 담을 리스트
hi = 0

put = input("성씨를 입력하세요: ")

while hi < len(name):  # hi가 리스트 길이보다 작을 때까지 반복
    if name[hi].startswith(put):  # 성씨가 일치하면
        if hi < 4:                # 정렬된 리스트에서 0~3번 안이면
            lst.append(name[hi])  # 결과 리스트에 추가
        else:
            print(put, "씨는 번호가 4번 이하가 아닙니다.")
            break  # 이미 번호가 넘어가면 멈춤
    hi += 1

# 결과 출력
if lst:
    print(lst)
else:
    print("해당 성씨를 가진 학생이 없습니다.")
