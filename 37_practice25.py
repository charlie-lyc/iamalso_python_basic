# 모듈

# import theater_module # import <모듈>
#
# theater_module.price(1)
# theater_module.price_morning(2)
# theater_module.price_soldier(3)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# import theater_module as theater # import <모듈> as <이름>
#
# theater.price(4)
# theater.price_morning(5)
# theater.price_soldier(6)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

from theater_module import price, price_morning # from <모듈> import <함수>

price(1)
price_morning(2)
# price_soldier(3) # NameError: name 'price_soldier' is not defined

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

from theater_module import price_soldier as price # from <모듈> import <함수> as <이름>

price(2)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# from theater_module import * # from <모듈> import *
#
# price(7)
# price_morning(8)
# price_soldier(9)