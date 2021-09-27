# 표준 출력
print('Python', 'Java', sep=' ') # Default

print('Python', 'Java', sep=', ')

print('Python', 'Java', sep=' vs ')

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print('Python', end='\n') # Default
print('Java')

print('Python', end=' ')
print('Java')

print('Python', end=', ')
print('Java')

print('Python', end=' vs ')
print('Java')

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

import sys

print('Python', 'Java', file=sys.stdout) # 표준 출력
print('Python', 'Java', file=sys.stderr) # 표준 에러 처리

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 시험 성적 출력
scores = {'Math': 0, 'English': 50, 'Coding': 100}
for subject, score in scores.items():
	print(subject, score)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# ljust: left just
# rjust: right just
scores = {'Math': 0, 'English': 50, 'Coding': 100}
for subject, score in scores.items():
	print(subject.ljust(7), str(score).rjust(3), sep=': ')

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 은행 대기 순번표 : 001, 002, 003, ..
for num in range(1, 11):
	print('대기번호: ', num)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# zfill : zero fill
for num in range(1, 11):
	print('대기번호: ', str(num).zfill(3))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 표준 입력 : 항상 문자로 저장됨
answer = input('아무 값이나 입력하세요 : ')
print('입력하신 값은 ' + answer + '입니다.')