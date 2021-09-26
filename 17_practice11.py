# 함수

# 정의
def open_account():
    print('새로운 계좌가 생성되었습니다.')

# 실행
open_account()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 전달값 : balance, money
# 반환값 : balace + money

def deposit(balance, money):
    print('{}원 입금이 완료되었습니다. 잔액은 {}원 입니다.'.format(money, balance + money))
    return balance + money

balance = 0

balance = deposit(balance, 1000)
print(balance)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 조건에 따라 다른 반환값
def withdraw(balance, money):
    if balance < money:
        print('잔액이 모자랍니다. 잔액은 {}원입니다.'.format(balance))
        return balance
    print('{}원 출금이 완료되었습니다. 잔액은 {}원 입니다.'.format(money, balance - money))
    return balance - money

balance = 1000

balance = withdraw(balance, 1100)
print(balance)

balance = withdraw(balance, 1000)
print(balance)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 동시에 여러 개의 반환값
def withdraw_night(balance, money):
    commission = 100 # 수수료
    if balance < money + commission:
        print('잔액이 모자랍니다. 잔액은 {}원입니다.'.format(balance))
        return commission, balance
    print('{}원 출금이 완료되었으며, 수수료는 {}원 입니다. 잔액은 {}원 입니다.'.format(money, commission, balance - money - commission))
    return commission, balance - money - commission

balance = 1000

commission, balance = withdraw_night(balance, 1000)
print(commission, balance)

commission, balance = withdraw_night(balance, 900)
print(commission, balance)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 기본(전달)값 

# 학생의 이름, 나이, 프로그래밍수업 주사용 언어
def profile(name, age, main_lang):
    print('이름: {}\t나이: {}\t주사용 언어: {}' \
        .format(name, age, main_lang))

profile('John', 20, 'python')
profile('Pete', 25, 'java')

# 그런데 만일 같은 학년, 같은 수업을 듣는 학생이라면?
# 나이가 같거나 주사용 언어가 같음
def profile(name, age=20, main_lang='python'):
    print('이름: {}\t나이: {}\t주사용 언어: {}'.format(name, age, main_lang))

profile('Jack')
profile('Jerry')

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 키워드 값

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name='Ethan', main_lang='java', age=21)
profile(main_lang='python', age=20, name='John' )

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 갯수를 알수 없는 전달값

def profile(name, age, lang1, lang2, lang3):
    print('이름: {}\t나이: {}\t사용 언어: '.format(name, age), end='')
    print(lang1, lang2, lang3)

profile('Jack', 20, 'python', 'java', 'javascript')

# 만약 사용할 줄 아는 언어가 두가지 뿐이라면?
# profile('Jerry', 20, 'python', 'java') # TypeError: profile() missing 1 required positional argument: 'lang3'
profile('Jerry', 20, 'python', 'java', '')

# 또는 사용할 줄 아는 언어가 네가지 이상이라면?
# profile('Jerry', 20, 'python', 'java', 'javascript', 'c') # TypeError: profile() takes 5 positional arguments but 6 were given

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 가변 인자 : *args

def profile(name, age, *langs):
    print('이름: {}\t나이: {}\t사용언어: '.format(name, age), end='')
    for lang in langs:
        print(lang, end=' ')
    print()

profile('Ethan', 20, 'java', 'javascript')
profile('John', 20, 'python', 'java', 'javascript', 'c')