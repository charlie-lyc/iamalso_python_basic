# 연산자
print(1 + 1)
print(3 - 2)
print(5 * 2)
print(6 / 3)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print(2 ** 3)  # 거듭제곱
print(5 % 3)   # 나머지
print(10 % 3)
print(5 // 3)  # 몫
print(10 // 3)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)
print(1 != 3)
print(not (1 != 3))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))
print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print(5 > 4 > 3)
print(5 > 4 > 7)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# 간단한 수식
print(2 + 3 * 4)
print((2 + 3) * 4)

number = 2 + 3 * 4
print(number)

# number = number + 5
# print(number)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
number += 5
print(number)

number -= 5
print(number)

number *= 4
print(number)

number /= 4
print(number)

number %= 3
print(number)

number //= 2
print(number)