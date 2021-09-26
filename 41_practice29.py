### 내장함수

# 1. type(): 객체의 타입(클래스)을 표시
# 2. dir() : 객체가 어떤 변수와 함수를 가지고 있는지 표시(객체를 간단하게 들여다 보는 함수)
# 3. help(): 객체가 가진 변수와 함수가 어떻게 정의되어 있는지 아주 상세하게 '출력'

import random

print(type(random))
print(dir(random))
# help(random)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

import pickle

print(type(pickle))
print(dir(pickle))
# help(pickle)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

list1 = []
print(type(list1))
print(dir(list1))
# help(list1)


# 4. input() : 사용자 입력을 받는 함수

# language = input('무슨 프로그래밍 언어를 좋아하세요? ')
# print('{}은 아주 좋은 프로그래밍 언어입니다.'.format(language))


# 5. 기타 : https://docs.python.org/3/library/functions.html 참고

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

### 외장함수

# 1. glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 운영체제에서 'dir' 명령과 유사)

import glob

print(glob.glob('*.py')) # 동일한 경로에 존재하는 확장자 .py인 모든 파일 조회: 리스트로 반환


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 2. os : 운영체제에서 제공하는 기본 기능

import os

print(dir(os))

print(os.getcwd())  # 현재 작업중인 디렉토리 표시: /Users/charlie/Documents/YouTube/IAmAlsoCoding/python_basic
print(os.listdir()) # 현재 디렉토리에 존재하는 모든 파일과 디렉토리 조회: 리스트로 반환


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

folder = 'sample_dir'

if os.path.exists(folder): # 경로가 존재하는지 확인
    print('이미 존재하는 폴더입니다.')
else:
    print('존재하지 않는 폴더입니다.')
    os.makedirs(folder) # 디렉토리 생성
    print(folder, '폴더를 생성하였습니다.')


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 3. time, datetime : 시간 관련 함수

import time

print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S')) # string format time
print(time.strftime('%y %h'))
print(time.strftime('%D, %s'))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

import datetime

print(datetime.date.today())

today = datetime.date.today()
time_delta = datetime.timedelta(days=100)

print('오늘부터 100일 전:', today - time_delta)
print('오늘부터 100일 뒤:', today + time_delta)