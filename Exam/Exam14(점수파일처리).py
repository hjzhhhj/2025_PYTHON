file_path = 'Exam/score.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    
for line in lines:
    line = line.strip()
    name, subjects_str, scores_str = line.split('/')
    subjects = subjects_str.split(',')
    scores = list(map(int, scores_str.split(',')))
    subject_count = len(subjects)
    average_score = sum(scores) / subject_count
    print(f"{name} : {subject_count}과목 수강, 평균 {average_score:.1f}점")