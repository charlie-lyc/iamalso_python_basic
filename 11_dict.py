# 딕셔너리
cabinet = { 3: 'John', 100: 'Jack' }
print(cabinet[3])
print(cabinet[100])
# print(cabinet[101])   # KeyError: 101
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print(cabinet.get(3))
print(cabinet.get(100))
print(cabinet.get(101)) # None 출력
print(cabinet.get(101, '키값 사용 가능')) # None 대신에 메시지 출력

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print(3 in cabinet)
print(100 in cabinet)
print(101 in cabinet)

# print('John' in cabinet)
# print('Jack' in cabinet)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

cabinet = { 'A-3': 'Pete', 'B-100': 'Jerry'}
print(cabinet['A-3'])
print(cabinet['B-100'])
print(cabinet)

# 추가
cabinet['C-101'] = 'Ethan'
print(cabinet)

# 수정(갱신)
cabinet['A-3'] = 'John'
print(cabinet)

# 삭제
del cabinet['C-101']
print(cabinet)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 키들만 출력
print(cabinet.keys())

# 값들만 출력
print(cabinet.values())

# 키-값들 출력
print(cabinet.items())

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 모두 지우기
cabinet.clear()
print(cabinet)