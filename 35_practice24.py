# 에러 발생시키기 : 개발자가 의도적으로 에러를 발생시킴

# try:
#     print('한 자리 숫자 나누기 전용 계산기입니다.')
#     num1 = int(input('첫 번째 숫자를 입력하세요: '))
#     num2 = int(input('두 번째 숫자를 입력하세요: '))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print('{} / {} = {}'.format(num1, num2, num1 / num2))
# except ValueError:
#     print('[에러] 잘못된 값이 입력되었습니다. 한 자리 숫자만 입력하세요.')


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 사용자 정의 예외처리 : Exception 클래스를 상속받아 사용자가 직접 에러 클래스를 정의
#                   앞서 다루었던 ValueError 또는 ZeroDivisionError 들도 이런 과정을 거쳐 정의됨


# class BigNumberError(Exception):
#     pass
#
#
# try:
#     print('한 자리 숫자 나누기 전용 계산기입니다.')
#     num1 = int(input('첫 번째 숫자를 입력하세요: '))
#     num2 = int(input('두 번째 숫자를 입력하세요: '))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError
#     print('{} / {} = {}'.format(num1, num2, num1 / num2))
# except ValueError:
#     print('[에러] 잘못된 값이 입력되었습니다. 숫자만 입력하세요.')
# except BigNumberError:
#     print('[에러] 잘못된 값이 입력되었습니다. 한 자리 숫자만 입력하세요.')


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

class BigNumberError(Exception):

    def __init__(self, msg):
        self.msg = msg

    # __str__() : 인스턴스 객체를 출력하였을 때 반환되는 값을 정의하는 메소드
    # 즉, print(<instance>) 를 실행하면 => <instance>.__str__() 의 반환값 출력
    def __str__(self):
        return self.msg


# try:
#     print('한 자리 숫자 나누기 전용 계산기입니다.')
#     num1 = int(input('첫 번째 숫자를 입력하세요: '))
#     num2 = int(input('두 번째 숫자를 입력하세요: '))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError('한 자리 숫자만 입력하세요.')
#     print('{} / {} = {}'.format(num1, num2, num1 / num2))
# except ValueError:
#     print('[에러] 잘못된 값이 입력되었습니다. 숫자만 입력하세요.')
# except BigNumberError as e:  # e = BigNumberError('한 자리 숫자만 입력하세요.')
#     print('[에러] 잘못된 값이 입력되었습니다.', e)


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# finally : 정상적인 동작 또는 예외 처리의 경우에 관계없이 항상 실행

try:
    print('한 자리 숫자 나누기 전용 계산기입니다.')
    num1 = int(input('첫 번째 숫자를 입력하세요: '))
    num2 = int(input('두 번째 숫자를 입력하세요: '))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError('한 자리 숫자만 입력하세요.')
    print('{} / {} = {}'.format(num1, num2, num1 / num2))
except ValueError:
    print('[에러] 잘못된 값이 입력되었습니다. 숫자만 입력하세요.')
except BigNumberError as e: # e = BigNumberError('한 자리 숫자만 입력하세요.')
    print('[에러] 잘못된 값이 입력되었습니다.', e)
finally:
    print('계산기를 이용해 주셔서 감사합니다.')