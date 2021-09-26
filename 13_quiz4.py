# Quiz4) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
#   참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
#   댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
#   추첨 프로그램을 작성하시오.
#
# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈의 shuffle와 sample을 활용
#
# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --
#
# (활용 예제)
# from random import *
# first = [1, 2, 3, 4, 5]
# print(first)
# shuffle(first)
# print(first)
# print(sample(first, 1))

# My Solution
import random

ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
random.shuffle(ids)
# print(ids)

chicken = random.sample(ids, 1)
# print(chicken)

# 중복 당첨을 피하기 위해 치킨 당첨자를 제외
index = ids.index(chicken[0])
ids.pop(index)
# print(ids)

coffee = random.sample(ids, 3)
# print(coffee)

print('-- 당첨자 발표 --')
print('치킨 당첨자 :', chicken[0])
print('커피 당첨자 :', coffee)
print('-- 축하합니다 --')

################################################################################
# Instructor's Solution
users = range(1, 21) # range() : 시퀀스 생성 빌트인 함수
# print(type(users))

users = list(users)
# print(type(users))

# print(users)
random.shuffle(users)
# print(users)

# 중복 당첨을 피하기 위해 치킨, 커피 당첨자들을 한 꺼번에 선택
winners = random.sample(users, 4)

print('-- 당첨자 발표 --')
print('치킨 당첨자 : {}'.format(winners[0]))
print('커피 당첨자 : {}'.format(winners[1:]))
print('-- 축하합니다 --')