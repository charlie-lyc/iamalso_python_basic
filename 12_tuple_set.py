# 튜플
menu = ('돈까스', '치즈까스')
print(menu[0])
print(menu[1])
print(menu)

# 변경 불가
# menu.add('생선까스')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# name = 'John'
# age = 20
# hobby = '코딩'
# print(name, age, hobby)

name, age, hobby = 'John', 20, '코딩'
print(name, age, hobby)

(name, age, hobby) = ('John', 20, '코딩')
print(name, age, hobby)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# 세트('집합') : 중복 안됨, 순서 없음
# 수학에서 다루는 '집합'의 개념 적용(교집합, 합집합, 차집합 등)
my_set = {1, 2, 3, 3, 3}
print(my_set)

# 자바와 파이썬을 개발할 수 있는 개발자
java = {'John', 'Jack', 'Pete'}
python = set(['John', 'Jerry'])

# 교집합(자바와 파이썬 모두 개발할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합(자바 또는 파이썬을 개발할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합(자바는 가능하지만 파이썬은 불가능한 개발자)
print(java - python)
print(java.difference(python))

# 차집합(파이썬은 가능하지만 자바는 불가능한 개발자)
print(python - java)
print(python.difference(java))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 추가
print(python)
python.add('Ethan')
print(python)

# 삭제
print(java)
java.remove('Pete')
print(java)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# 자료 구조의 상호 변경
menu = {'커피', '우유', '주스'}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))