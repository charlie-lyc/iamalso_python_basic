# pass 이용

# 일반 유닛
class Unit:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 건물 짓기
class BuildingUnit(Unit):

    def __init__(self, name, hp, location):
        pass # 아무것도 작성되지 않았지만 코드 실행시 이상이 없는 것으로 취급하고 넘어감


# 서플라이 디폿 : 건물, 1개일때 8 유닛 생산 가능
supply_depot = BuildingUnit('서플라이디폿', 500, '7시') # 실행시 이상 없음

# print(supply_depot.name, supply_depot.hp, supply_depot.location) # AttributeError: 'BuildingUnit' object has no attribute 'name'

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    pass

game_start()
game_over()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# super() 이용

# 건물 짓기
class BuildingUnit(Unit):

    def __init__(self, name, hp, location):
        ##################################
        # Unit.__init__(self, name, hp)
        ## 또는
        super().__init__(name, hp)
        ##################################
        self.location = location


supply_depot = BuildingUnit('서플라이디폿', 500, '7시')

print(supply_depot.name, supply_depot.hp, supply_depot.location)