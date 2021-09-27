# 숫자처리 함수
print(abs(-5))     # 절대값
print(pow(4, 2))   # 거듭제곱
print(max(5, 12))  # 최대값
print(min(5, 12))  # 최소값
print(round(3.14)) # 반올림
print(round(4.99))

# math module 이용
import math
print(math.floor(4.99))
print(math.ceil(3.14))
print(math.sqrt(16))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# random module 이용
import random
print(random.random())           # 0.0 < x < 1.0 임의의 값 생성
print(random.random())
print(random.random())
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print(random.random() * 10)      # 0.0 < x < 10.0 임의의 값 생성
print(random.random() * 10)
print(random.random() * 10)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print(int(random.random() * 10))     # 0 <= x < 10 임의의 정수 생성 : int()를 이용할 경우 기본적으로 math.floor()가 적용
print(int(random.random() * 10))
print(int(random.random() * 10))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print(int(random.random() * 10 + 1)) # 0 < x <= 10 임의의 정수 생성
print(int(random.random() * 10 + 1))
print(int(random.random() * 10 + 1))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# Generate lottery numbers

# print(int(random.random() * 45 + 1)) # 0 < x <= 45 임의의 정수 생성
# print(int(random.random() * 45 + 1))
# print(int(random.random() * 45 + 1))
# print(int(random.random() * 45 + 1))
# print(int(random.random() * 45 + 1))
# print(int(random.random() * 45 + 1))

# print(random.randrange(1, 46))       # 1 <= x < 46 임의의 정수 생성
# print(random.randrange(1, 46))
# print(random.randrange(1, 46))
# print(random.randrange(1, 46))
# print(random.randrange(1, 46))
# print(random.randrange(1, 46))

print(random.randint(1, 45))           # 1 <= x <= 45 임의의 정수 생성
print(random.randint(1, 45))
print(random.randint(1, 45))
print(random.randint(1, 45))
print(random.randint(1, 45))
print(random.randint(1, 45))