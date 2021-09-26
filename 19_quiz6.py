# Quiz6) 표준 체중을 구하는 프로그램을 작성하시오.
#   
# * 표준 체중 : 각 개인의 키에 적당한 체중
#
# (성별에 따른 공식)
# 여자: 키(m) X 키(m) X 21
# 남자: 키(m) X 키(m) X 22
#
# 조건1: 표준 체중은 별도의 함수 내에서 계산
# 		* 함수명: std_weight
#		* 전달값: 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 둘째 자리까지 표시
#
# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# My Solution
def std_weight(height, gender):
	if gender == '여자':
		weight = round((height/100)*(height/100)*21, 2)
	else: 
		weight = round((height/100)*(height/100)*22, 2)
	print('키 {}cm {}의 표준 체중은 {}kg 입니다.'.format(height, gender, weight))

std_weight(175, '남자')

################################################################################
# Instructor's Solution
def std_weight(height, gender):
	if gender == '여자':
		return height * height * 21
	else:
		return height * height * 22

height = 175
gender = '남자'
weight = std_weight(height/100, '남자')
print('키 {}cm {}의 표준 체중은 {}kg 입니다.'.format(height, gender, round(weight, 2)))
