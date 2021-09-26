# 모듈 직접 실행 : 모듈을 본격적으로 이용하기 전에 실제 잘 작동되는지 확인이 필요

# 아래와 같이 모듈 파일의 맨 아래쪽에 작성하고 실행해봄으로써 확인 가능
# if __name__ == '__main__': # 모듈 직접 실행의 경우
#   ...
# else: # 모듈 외부 호출의 경우
#   ...

# % python3 thailand.py
# % python3 vietnam.py

from travel.thailand import ThailandPackage # from <패키지>.<모듈> import <클래스>
from travel.vietnam import VietnamPackage as Viet

ThailandPackage().detail()
Viet().detail()


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 패키지, 모듈 위치 확인 : inspect.getfile(<임포트된 대상(이름)>)

import inspect
import random

print(inspect.getfile(inspect)) # /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/inspect.py
print(inspect.getfile(random)) # /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/random.py

# print(inspect.getfile(travel)) # NameError: name 'travel' is not defined
# print(inspect.getfile(travel.thailand)) # NameError: name 'travel' is not defined
# print(inspect.getfile(thailand)) # NameError: name 'thailand' is not defined

print(inspect.getfile(ThailandPackage)) # /Users/charlie/Documents/YouTube/IAmAlsoCoding/python_basic/travel/thailand.py
print(inspect.getfile(Viet)) # /Users/charlie/Documents/YouTube/IAmAlsoCoding/python_basic/travel/vietnam.py