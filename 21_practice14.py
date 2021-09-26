# 다양한 출력포맷

print('{1} {0}'.format(1000, 500)) # x번째(인덱스)의 값이 포맷에 매핑됨

print('{} {}'.format(500, 1000))   # 인덱스 값이 생략될 경우 순서대로 매핑됨

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 총 10자리 공간을 확보하고, 오른쪽 정렬을 하되, 빈 자리는 빈공간으로 두기
print('{0:10}'.format(500)) # ':'을 이용하여 포맷 옵션을 나타낼 수 있음
print('{:10}'.format(500))  # 순서대로 매핑될 경우 인덱스 값 생략
print('{:>10}'.format(500)) # 주어지는 공간이 문자의 갯수보다 클 경우 오른쪽 정렬이 Default

# 총 10자리 공간을 확보하고, 왼쪽 정렬 하기
print('{:<10}'.format(500))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print('{:>10}'.format(+500))
print('{:>10}'.format(-500))

# 양수일 때는 + 표시, 음수일 때는 - 표시
print('{:>+10}'.format(500))
print('{:>+10}'.format(-500))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 총 10자리 공간을 확보하고, 오른쪽 정렬을 하되, 빈 자리는 0으로 채우기
print('{:0>10}'.format(500))
print('{:010}'.format(500))   # 숫자만 사용될 때는 정렬기호(>) 생략 가능
# print('{:_10}'.format(500)) # 기호가 사용될 때는 정렬기호(>) 생략 불가

# 총 10자리 공간을 확보하고, 오른쪽 정렬을 하되, 빈 자리는 _으로 채우기
print('{:_>10}'.format(500))

# 총 10자리 공간을 확보하고, 왼쪽 정렬을 하되, 빈 자리는 _으로 채우기
print('{:_<10}'.format(500))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 3자리 마다 콤마 찍기
print('{:,}'.format(1000000))

# 3자리 마다 콤마 찍고, +- 부호 붙이기
print('{:+,}'.format(1000000))
print('{:+,}'.format(-1000000))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 총 12자리 공간을 확보하고, 왼쪽 정렬을 하되, 빈자리는 ^로 채우기. 그리고 3자리 마다 콤마를 찍으며, +- 부호를 붙이기
print('{:^<+12,}'.format(1000000))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 소수점 출력
print('{}'.format(5/3))
print('{:f}'.format(5/3))

# 소수점 특정 자리수 까지만 표시
print('{:.7}'.format(5/3))  # 소수점 7번째에서 반올림하고, 6자리까지 표시
print('{:.6f}'.format(5/3)) # 소수점 7번째에서 반올림하고, 6자리까지 표시

# 소수점 기준으로 왼쪽은 앞서 표시한 방식을 따름
print('{:10.2f}'.format(5/3))
print('{:_>10.2f}'.format(5/3))
print('{:_>+10.2f}'.format(5/3))