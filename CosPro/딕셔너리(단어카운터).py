text_data = "I love Python. You love Python."

word_dic = {}

for word in text_data.split():
    if word in word_dic:
        word_dic[word] += 1
    else:
        word_dic[word] = 1

for w, count in sorted(word_dic.items()):
    print(w, "의 등장횟수=", count)