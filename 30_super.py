# super() 심화

class Unit:
    def __init__(self):
        print('Unit 생성자')


class Flyable:
    def __init__(self):
        print('Flyable 생성자')


# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         super().__init__()
#
#
# dropship = FlyableUnit() # 'Unit 생성자'만 출력(두 개의 부모 클래스 중 맨 처음 한개만 적용)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# class FlyableUnit(Flyable, Unit):
#     def __init__(self):
#         super().__init__()
#
#
# dropship = FlyableUnit() # 'Flyable 생성자'만 출력(두 개의 부모 클래스 중 맨 처음 한개만 적용)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)


dropship = FlyableUnit()