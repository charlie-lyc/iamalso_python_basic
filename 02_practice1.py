# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(3*(3+1))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋ")
print("ㅋ" * 5)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# boolean 자료형 : 참 | 거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# 변수
# 애완 동물을 소개해 주세요
print('우리집 강아지의 이름은 연탄이야')
print('연탄이는 4살이고, 산책을 아주 좋아해')
print('연탄이는 어른일까? True')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3
print('우리집 ' + animal + '의 이름은 ' + name + '야')
print(name + '는 ' + str(age) + '살이고, ' + hobby + '을 아주 좋아해')
print(name + '는 어른일까? ' + str(is_adult))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

animal = '고양이'
name = '나비'
age = 2
hobby = '낮잠'
is_adult = age >= 3
print('우리집 ', animal, '의 이름은 ', name, '야', sep='')
print(name, '는 ', str(age), '살이고, ', hobby, '을 아주 좋아해', sep='')
print(name, '는 어른일까? ', str(is_adult), sep='')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# 주석 : 코딩 작성에 포함되지만 실행시 무시

# 한 줄 작성시

'''
여러 줄 작성시
'''

"""
여러 줄 작성시
"""