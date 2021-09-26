class VietnamPackage:
    def detail(self):
        print('[베트남 패키지 3박 5일] 다낭 효도 여행 60만원')

if __name__ == '__main__': # 모듈 직접 실행의 경우
    print('[vietnam 모듈 직접 실행]')
    print('- 이하 내용은 모듈을 직접 실행할 때만 출력되는 내용입니다. - ')
    VietnamPackage().detail()
else: # 모듈 외부 호출의 경우
    print('[vietnam 모듈 외부 호출]')