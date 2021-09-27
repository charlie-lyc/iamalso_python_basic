# 파일 입출력

# 1. 파일 쓰기(덮어쓰기)

# score_file = open(file='score.txt', mode='w', encoding='utf8')
# print('수학: 0', file=score_file)
# print('영어: 50', file=score_file)
# score_file.close()

# print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 2. 파일 이어쓰기

# score_file = open('score.txt', 'a', encoding='utf8')
# score_file.write('과학: 70\n')  # print 함수와 달리 줄바꿈을 명시해야 함
# score_file.write('코딩: 100\n')
# score_file.close()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 3. 파일 읽기

score_file = open('score.txt') # 'r'과 encoding='utf8' 설정은 Default

print(score_file)

#  (1) read() : 파일 전체를 한꺼번에 읽기
scores = score_file.read()
print(scores)

score_file.close()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

#  (2) readlines() : 파일 전체를 한줄씩 끊어 읽기, list 형태로 저장

# 앞서 파일 객체 score_file 에 대하여 read() 메소드가 이미 실행되어 재이용 불가
# 따라서 다시 읽어들이는 과정이 필요
score_file = open('score.txt')

scores = score_file.readlines()
print(type(scores))
for score in scores:
    print(score, end='')
print()

score_file.close()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# (3) readline() : 한줄씩 읽기, 한줄 읽고 커서는 다음 줄에 대기(\n을 만나면 멈춤)

score_file = open('score.txt')

# line = score_file.readline()
# print(line, end='')
#
# line = score_file.readline()
# print(line, end='')
#
# line = score_file.readline()
# print(line, end='')
#
# line = score_file.readline()
# print(line, end='')

# 파일에 몇 줄이 작성되었는지 알고 있을 때
for i in range(4):
    line = score_file.readline()
    print(line, end='')
print()

score_file.close()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

score_file = open('score.txt')

# 파일에 몇 줄이 작성되었는지 알수 없을 때
while True:
    line = score_file.readline()
    # if not line: # line의 내용이 없으면
    if line == '':
        break
    print(line, end='')
print()

score_file.close()