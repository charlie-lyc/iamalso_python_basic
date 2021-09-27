# 패키지 : 여러 개의 모듈을 작성, 취합(하여 만든 일종의 규모가 큰 모듈)

# import travel.thailand # import <패키지>.<모듈>
# import travel.vietnam
#
# thai = travel.thailand.ThailandPackage()
# viet = travel.vietnam.VietnamPackage()
#
# thai.detail()
# viet.detail()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# import travel.thailand as thailand # import <패키지>.<모듈> as <이름>
# import travel.vietnam as vietnam
#
# thai = thailand.ThailandPackage()
# viet = vietnam.VietnamPackage()
#
# thai.detail()
# viet.detail()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# from travel import thailand, vietnam # from <패키지> import <모듈>
#
# thai = thailand.ThailandPackage()
# viet = vietnam.VietnamPackage()
#
# thai.detail()
# viet.detail()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

from travel.thailand import ThailandPackage # from <패키지>.<모듈> import <클래스>
from travel.vietnam import VietnamPackage

ThailandPackage().detail()
VietnamPackage().detail()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

from travel.thailand import ThailandPackage as ThaiPack # from <패키지>.<모듈> import <클래스> as <이름>
from travel.vietnam import VietnamPackage as VietPack

ThaiPack().detail()
VietPack().detail()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# from travel.thailand import * # from <패키지>.<모듈> import *
# from travel.vietnam import *
#
# ThailandPackage().detail()
# VietnamPackage().detail()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# from travel import * # from <패키지> import *
#
# thailand.ThailandPackage().detail() # NameError: name 'thailand' is not defined
# vietnam.VietnamPackage().detail() # NameError: name 'vietnam' is not defined

######################
# *** 주의할 점!!! *** #
######################
# 만약  import * 코드를 이용하여 가져올 대상이 <모듈>일 경우에는 
# __init__.py 에 다음과 같이 허용하는 모듈들의 리스트를 작성하여 명시해야함!!!
# __all__ = ['thailand', 'vietnam']

# thailand.ThailandPackage().detail()
# vietnam.VietnamPackage().detail()

