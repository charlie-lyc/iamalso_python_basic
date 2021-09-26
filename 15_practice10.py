# 반복

# print('대기번호 : 1')
# print('대기번호 : 2')
# print('대기번호 : 3')
# print('대기번호 : 4')
# print('대기번호 : 5')
# print('대기번호 : ...')

# 1. for
for waiting_number in [1, 2, 3, 4, 5]:
    print('대기번호 : {}'.format(waiting_number))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

for waiting_number in range(1, 6): # 1 ~ 5 시퀀스 생성
    print('대기번호 : {}'.format(waiting_number))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

for number in range(5): # 0 ~ 4 시퀀스 생성(for문을 이용해서 5회 반복)
    print(number)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

starbucks = ['Ironman', 'Thor', 'Groot']
for customer in starbucks:
    print('{}님, 커피가 준비되었습니다.'.format(customer))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 2. while

# 호출 5번해도 응답이 없으면 커피 폐기
customer = 'Ironman'
index = 5
while index >= 1:
    index -= 1
    print('{}님, 커피가 준비되었습니다. 호출 {}번 남았습니다.'.format(customer, index))
    if index == 0:
        print('커피는 폐기되었습니다.')

# 응답이 있을 때까지 계속 호출
# customer = 'Thor'
# count = 0
# while True: # 무한 루프 : Control + c 로 멈춤
#     print('{}님, 커피가 준비되었습니다.'.format(customer))
#     count += 1
#     print('호출 {}회'.format(count))

# 커피를 주문한 사람이 맞을 때까지 계속 호출
# orderer = 'Thor'
# customer = 'Unknown' 
# while customer != orderer:
#     print('{}님, 커피가 준비되었습니다.'.format(orderer))
#     customer = input('이름이 어떻게 되세요? ')

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 3. break, continue

# orderer = 'Thor'
# customer = 'Unknown' 
# while True:
#     print('{}님, 커피가 준비되었습니다.'.format(orderer))
#     customer = input('이름이 어떻게 되세요? ')
#     if customer == orderer:
#         break

absent = [2, 5] # 결석한 학생의 번호
lost_book = [7] # 교과서를 분실한 학생
for student in range(1, 11):
    if student in absent:
        continue
    elif student in lost_book:
        print('{}번, 교무실로 따라와!'.format(student))
        break
    print('{}번, 책을 읽어봐.'.format(student))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 4. 한줄로 작성하는 for

# 학생들의 출석 번호에 100을 더하기
students_numbers = [1, 2, 3, 4, 5]
print(students_numbers)

new_numbers = [ number + 100 for number in students_numbers ]
print(new_numbers)

# 학생들의 이름을 그 길이로 바꾸기
students_names = ['Ironman', 'Thor', 'Groot']
print(students_names)

name_lengths = [ len(name) for name in students_names ]
print(name_lengths)

# 학생들의 이름을 대문자로 바꾸기
upper_names = [ name.upper() for name in students_names ]
print(upper_names)