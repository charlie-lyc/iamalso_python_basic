# Quiz5) 당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
#   10명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
#
# 조건1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
#
# (출력 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 10번째 손님 (소요시간 : 16분)
# 총 탑승 승객 : 2명

# My Solution
import random

customer_count = 0
for match_count in range(1, 11):
    required_time = random.randint(5, 50)
    if 5 <= required_time <= 15:
        customer_count += 1
        is_counted = 'O'
    else:
        is_counted = ' '
    print('[{}] {}번째 손님 (소요시간 : {}분)'.format(is_counted, match_count, required_time))
print('총 탑승 승객 : {}명'.format(customer_count))

################################################################################
# Instructor's Solution

cnt = 0                            # 총 탑승 승객 수
for i in range(1, 11):             # 10번의 매칭 기회
    time = random.randrange(5, 51) # 5분 ~ 50분의 소요 시간
    if 5 <= time <= 15:            # 5분 ~ 15분일때 매칭 성공 
        cnt += 1                   # 총 탑승 승객 수 증가
        print('[O] {}번째 손님 (소요시간: {}분'.format(i, time))
    else:
        print('[ ] {}번째 손님 (소요시간: {}분'.format(i, time))
print('총 탑승 승객 : {}명'.format(cnt))