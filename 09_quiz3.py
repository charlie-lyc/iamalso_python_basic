# Quiz3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
#
#  예) https://naver.com
# 규칙1: https:// 부분은 제외 => naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성
#              (nav)           (5)          (1)        (1)
#       따라서 생성된 비밀 번호 : nav51!
# (출력문 예제)
# https://naver.com의 비밀번호는 nav51!로 생성되었습니다.

# My Solution
site = 'https://naver.com'
site = 'https://daum.net'
site = 'https://google.com'
site = 'https://youtube.com'

index1 = site.find('/')
index2 = site.find('.')
site_name = site[index1+2:index2]
# print(site_name)

print('{}의 비밀번호는 {}{}{}{}입니다.'.format(site, site_name[:3], len(site_name), site_name.count('e'), '!'))


################################################################################
# Instructor's Solution
url = 'https://naver.com'
url = 'https://daum.net'
url = 'https://google.com'
url = 'https://youtube.com'

# 규칙1
my_str = url.replace('https://', '')
# print(my_str)

# 규칙2
my_str = my_str[:my_str.index('.')]
# print(my_str)

# 규칙3
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
print('{}의 비밀번호는 {}입니다.'.format(url, password))