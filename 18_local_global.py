# 지역변수와 전역변수

gun = 10

def checkpoint(soldiers): # 경계 근무나가는 군인 수에 대한 총기 체크
	gun = gun - soldiers
	print('[함수 내] 남은 총 : {}'.format(gun))

# print('전체 총: {}'.format(gun))

# 2명이 경계 근무 나감
# checkpoint(2)                  # UnboundLocalError: local variable 'gun' referenced before assignment

# print('전체 총: {}'.format(gun))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

gun = 10 # 전역 변수

def checkpoint(soldiers):
	gun = 20 # 지역 변수
	gun = gun - soldiers
	print('[함수 내] 남은 총 : {}'.format(gun))

print('전체 총: {}'.format(gun)) # 전역 변수 gun
checkpoint(2)                  # 지역 변수 gun
print('전체 총: {}'.format(gun)) # 전역 변수 gun

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

gun = 10

# 함수 내에서 전역 변수를 이용할 것을 '선언'
def checkpoint(soldiers):
	global gun
	gun = gun - soldiers
	print('[함수 내] 남은 총 : {}'.format(gun))

print('전체 총: {}'.format(gun))
checkpoint(2)                 
print('전체 총: {}'.format(gun))


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

gun = 10

# 함수 내에서 전역 변수를 '선언'하고, 새로운 값을 할당
def checkpoint(soldiers):
	global gun
	gun = 20
	gun = gun - soldiers
	print('[함수 내] 남은 총 : {}'.format(gun))

print('전체 총: {}'.format(gun))
checkpoint(2)                 
print('전체 총: {}'.format(gun))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# global은 자칫 혼란을 야기시킬 수 있으므로 사용을 자제하고, 가급적 전달값과 반환값을 이용
gun = 10

def checkpoint_return(gun, soldiers):
	gun = gun - soldiers 
	print('[함수 내] 남은 총 : {}'.format(gun))
	return gun

print('전체 총: {}'.format(gun))
gun = checkpoint_return(gun, 2)                 
print('전체 총: {}'.format(gun))