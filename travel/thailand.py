class ThailandPackage:
    def detail(self):
        print('[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원')

if __name__ == '__main__': # 모듈 직접 실행의 경우
    print('[thailand 모듈 직접 실행]')
    print('- 이하 내용은 모듈을 직접 실행할 때만 출력되는 내용입니다. - ')
    ThailandPackage().detail()
else: # 모듈 외부 호출의 경우
    print('[thailand 모듈 외부 호출]')