sentence = input("문장을 입력하세요: ")
words = sentence.split()

reversed_words = [word[::-1] for word in words]
print(" ".join(reversed_words))
