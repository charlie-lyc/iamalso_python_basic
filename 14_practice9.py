# 분기

# if 조건:
#   실행명령문

weather = '비'
if weather == '비':
    print('우산 챙기기')

weather = '맑음'
if weather == '비':
    print('우산 챙기기')
else:
    print('준비물 필요 없음')

weather = '미세먼지'
if weather == '비':
    print('우산 챙기기')
elif weather == '미세먼지':
    print('마스크 챙기기')
else:
    print('준비물 필요 없음')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 사용자 동적 입력
# weather = input("오늘 날씨 어때요?('비', '맑음', '미세먼지' 중 선택) ")
# if weather == '비':
#     print('우산 챙기기')
# elif weather == '미세먼지':
#     print('마스크 챙기기')
# else:
#     print('준비물 필요 없음')

weather = input("오늘 날씨 어때요? ('비', '눈', '미세먼지', '맑음' 중 선택) ")
if weather == '비' or weather == '눈':
    print('우산 챙기기')
elif weather == '미세먼지':
    print('마스크 챙기기')
else:
    print('준비물 필요 없음')

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

temp = int(input('오늘 기온은 몇도 정도인가요? (정수로 입력)'))
if temp >= 30:
    print('너무 더워요. 나가지 마세요.')
elif 10 <= temp < 30:
    print('괜찮은 기온이네요.')
elif 0 <= temp and temp < 10:
    print('외투를 챙기세요.')
else:
    print('너무 추워요. 나가지 마세요.')