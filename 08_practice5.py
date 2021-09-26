print('a' + 'b')
print('a', 'b', sep='')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# 문자열 포맷

# 방법1
print('나는 %d살 입니다.' % 21)             # decimal integer
print('나는 %s을 좋아해요.' % '파이썬')       # string
print('Apple은 알파벳 %c로 시작해요.' % 'A') # character

# 엄격하게 구분하여 이용하자면 위와 같이 문법을 따라야 함
# 하지만 단순 표현하는데는 %s만 이용하여도 차이도 없음
print('나는 %s살 입니다.' % 21)
print('나는 %s을 좋아해요.' % '파이썬')
print('Apple은 알파벳 %s로 시작해요.' % 'A')

print('나는 %s색과 %s색을 좋아합니다.' % ('파란', '빨간'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 방법2
print('나는 {}살입니다.'.format(22))
print('나는 {}색과 {}색을 좋아합니다.'.format('하늘', '보라'))
print('나는 {0}색과 {1}색을 좋아합니다.'.format('하늘', '보라'))
print('나는 {1}색과 {0}색을 좋아합니다.'.format('하늘', '보라'))

print('나는 {age}살이며, {color}색을 좋아해요.'.format(age=23, color='파란'))
print('나는 {age}살이며, {color}색을 좋아해요.'.format(color='파란', age=23))
age = 20
color = '파란'
print('나는 {}살이며, {}색을 좋아해요.'.format(age, color))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 방법3 : v3.6이상
age = 20
color = '파란'
print(f'나는 {age}살이며, {color}색을 좋아해요.')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# 탈출 문자

# print('나는 '개발자' 입니다.')
print("나는 '개발자' 입니다.")
print('나는 \'개발자\' 입니다.')      # \' : 문자열 내에서 작은 따옴표

# print("나는 "개발자" 입니다.")
print('나는 "개발자" 입니다.')
print("나는 \"개발자\" 입니다.")      # \" : 문자열 내에서 큰 따옴표

print('C:\\Users\\charlie\\Desktop\\python_basic') # \\ : 문자열 내에서 백슬래쉬

print('백문이 불여일견\n백견이 불여일타') # \n : 줄바꿈

print('백문이 불여일견\t백견이 불여일타') # \t : 탭

print('Redd\bApple')              # \b : 백스페이스
# => terminal에서 실행해야 함(플러그인에서는 제대로 실행되지 않음)
# RedApple

print('Red Apple\rPine')          # \r : 커서를 맨 앞으로 이동
# => terminal에서 실행해야 함(플러그인에서는 제대로 실행되지 않음)
# PineApple