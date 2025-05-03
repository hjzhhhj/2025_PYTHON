s = input("문자열을 입력하세요: ").replace(" ", "").lower()
counter = {}

for ch in s:
    counter[ch] = counter.get(ch, 0) + 1

max_count = max(counter.values())
for k, v in counter.items():
    if v == max_count:
        print(f"가장 많이 등장한 문자: {k} (횟수: {v})")
        break
