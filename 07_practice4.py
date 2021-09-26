# 문자열 표현
sentence1 = '나는 소년입니다.'
print(sentence1)

sentence2 = '파이썬은 쉬워요.'
print(sentence2)

sentence3 = '''
    나는 소년이고,
    파이썬은 쉬워요.
'''
print(sentence3)

sentence4 = """
    나는 장년이고,
    파이썬은 어려워요.
"""
print(sentence4)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# 문자열 슬라이싱
jumin = '990123-1234567'

print('성별 : ' + jumin[7])
# print('생년 : ' + jumin[0:2])
print('생년 : ' + jumin[:2])
print('생월 : ' + jumin[2:4])
print('생일 : ' + jumin[4:6])
# print('생년월일 : ' + jumin[0:6])
print('생년월일 : ' + jumin[:6])
# print('뒤7자리 : ' + jumin[7:14])
print('뒤7자리 : ' + jumin[7:])
# print('뒤7자리 (뒤부터): ' + jumin[-7:0])
print('뒤7자리 (뒤부터): ' + jumin[-7:])
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# 문자열 처리함수
python = 'Python is Amazing.'

print(python.lower())
print(python.upper())
print(python.capitalize())
print(python[0].islower())
print(python[0].isupper())
print(len(python))
print(python.replace('Python', 'Java'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print(python.index('n'))            # 문자열에서 첫 번째 'n'의 인덱스

index = python.index('n')
print(python.index('n', index + 1)) # 문자열에서 두 번째 'n'의 인덱스

# print(python.index('b')) # ValueError: substring not found
print(python.find('b'))  # -1

print(python.count('n'))