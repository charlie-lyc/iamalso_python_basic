# 예외처리

# print('나누기 전용 계산기입니다.')
# num1 = int(input('첫 번째 숫자를 입력하세요: '))
# num2 = int(input('두 번째 숫자를 입력하세요: '))
# print('{} / {} = {}'.format(num1, num2, num1 / num2))


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 1. 첫 번째 숫자 입력시 숫자 이외의 다른 값을 입력할 경우(예: '일') 바로 아래와 같은 에러 발생
# ValueError: invalid literal for int() with base 10: ''
# 에러 발생을 알림과 동시에 프로그램이 종료 되어 버림

## 낯선 에러 메시지보다는 알아볼 수 있는 메시지로 출력
# try:
#     print('나누기 전용 계산기입니다.')
#     num1 = int(input('첫 번째 숫자를 입력하세요: '))
#     num2 = int(input('두 번째 숫자를 입력하세요: '))
#     print('{} / {} = {}'.format(num1, num2, num1 / num2))
# except ValueError:
#     print('[에러] 잘못된 값이 입력되었습니다. 반드시 숫자를 입력하세요.')


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 2. 이번에는 첫 번째 숫자는 정상적으로 입력하고 두 번째 값을 0을 입력할 경우 아래와 같은 에러 발생
# ZeroDivisionError: division by zero
# 마찬가지로 에러 발생을 알림과 동시에 프로그램이 종료 되어 버림

## 예외처리를 추가하여 작성
# try:
#     print('나누기 전용 계산기입니다.')
#     num1 = int(input('첫 번째 숫자를 입력하세요: '))
#     num2 = int(input('두 번째 숫자를 입력하세요: '))
#     print('{} / {} = {}'.format(num1, num2, num1 / num2))
# except ValueError:
#     print('[에러] 잘못된 값이 입력되었습니다. 반드시 숫자를 입력하세요.')
# except ZeroDivisionError:
#     print('[에러] 잘못된 값이 입력되었습니다. 두 번째 숫자는 0이외의 숫자를 입력하세요.')

## 또는
# try:
#     print('나누기 전용 계산기입니다.')
#     num1 = int(input('첫 번째 숫자를 입력하세요: '))
#     num2 = int(input('두 번째 숫자를 입력하세요: '))
#     print('{} / {} = {}'.format(num1, num2, num1 / num2))
# except ValueError as e:
#     # print(e) # invalid literal for int() with base 10: '' 또는 division by zero
#     print('[에러] 반드시 숫자를 입력하세요.', e)
# except ZeroDivisionError as err_msg:
#     print('[에러] 두 번째 숫자는 0이외의 숫자를 입력하세요.', err_msg)

## 또는
# try:
#     print('나누기 전용 계산기입니다.')
#     num1 = int(input('첫 번째 숫자를 입력하세요: '))
#     num2 = int(input('두 번째 숫자를 입력하세요: '))
#     print('{} / {} = {}'.format(num1, num2, num1 / num2))
# except Exception as e:
#     # print(type(e))
#     if isinstance(e, ValueError):
#         print('[에러] 잘못된 값이 입력되었습니다. 반드시 숫자를 입력하세요.')
#     elif isinstance(e, ZeroDivisionError):
#         print('[에러] 잘못된 값이 입력되었습니다. 두 번째 숫자는 0이외의 숫자를 입력하세요.')


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 3. 이번에는 위의 코드를 변경하여 아래와 같이 작성할 경우 코드 한줄을 깜빡하여 에러 발생
# IndexError: list index out of range
# 이번에도 마찬가지로 에러 발생을 알림과 동시에 프로그램이 종료 되어 버림

# try:
#     print('나누기 전용 계산기입니다.')
#     nums = []
#     nums.append(int(input('첫 번째 숫자를 입력하세요: ')))
#     nums.append(int(input('두 번째 숫자를 입력하세요: ')))
#     # nums.append(nums[0] / nums[1])
#     print('{} / {} = {}'.format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print('[에러] 잘못된 값이 입력되었습니다. 반드시 숫자를 입력하세요.')
# except ZeroDivisionError:
#     print('[에러] 잘못된 값이 입력되었습니다. 두 번째 숫자는 0이외의 숫자를 입력하세요.')
# except:
#     print('[에러] 알수 없는 에러가 발생하였습니다.')

## 또는
try:
    print('나누기 전용 계산기입니다.')
    nums = []
    nums.append(int(input('첫 번째 숫자를 입력하세요: ')))
    nums.append(int(input('두 번째 숫자를 입력하세요: ')))
    # nums.append(nums[0] / nums[1])
    print('{} / {} = {}'.format(nums[0], nums[1], nums[2]))
except ValueError:
    print('[에러] 잘못된 값이 입력되었습니다. 반드시 숫자를 입력하세요.')
except ZeroDivisionError:
    print('[에러] 잘못된 값이 입력되었습니다. 두 번째 숫자는 0이외의 숫자를 입력하세요.')
except Exception as e:
    print('[에러] 알수 없는 에러가 발생하였습니다.', e)