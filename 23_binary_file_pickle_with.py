# pickle 모듈
import pickle

# 쓰기 : open(mode='wb'), pickle.dump()

# profile_file = open('profile.pickle', 'wb') # write binary
# profile = { '이름': 'John', '나이': 30, '취미': ['축구', '골프', '코딩']}
# print(profile)

# pickle.dump(profile, profile_file) # profile 정보를 binary 데이터로 profile_file에 쓰기
# profile_file.close()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

## profile_file = open('profile.pickle')
## print(profile_file) # <_io.TextIOWrapper name='profile.pickle' mode='r' encoding='UTF-8'>

# 읽기 : open(mode='rb'), pickle.load()

profile_file = open('profile.pickle', 'rb') # read binary
print(profile_file) # <_io.BufferedReader name='profile.pickle'>

profile = pickle.load(profile_file)
print(profile)
profile_file.close()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# with : close() 필요없음, 블록내의 명령 실행이 완료되면 파일이 자동으로 닫힘
# Context Manager 

with open('profile.pickle', 'rb') as profile_file:
	profile = pickle.load(profile_file)
	print(profile)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

with open('score.txt') as score_file:
	print(score_file.read())

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

with open('score.txt') as score_file:
	for line in score_file.readlines():
		print(line, end='')

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

with open('score.txt') as score_file:
	while True:
		line = score_file.readline()
		if not line:
			break
		print(line, end='')

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# with open('study.txt', 'w') as study_file:
# 	study_file.write('파이썬을 열심히 공부하고 있어요.')

with open('study.txt') as study_file:
	print(study_file.read())
