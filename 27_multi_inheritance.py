# 다중 상속 : 부모 클래스가 여러 개인 경우

# 일반 유닛
class Unit:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit):

    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage

    def attack(self, location):
        print('{}: {} 방향으로 적군을 공격합니다. [공격력 {}]'.format(self.name, location, self.damage))

    def damaged(self, damage):
        print('{}: {} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print('{}: 파괴되었습니다.'.format(self.name))
        else:
            print('{}: 현재 체력은 {}입니다.'.format(self.name, self.hp))


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# *** 공중 이동이 가능한 클래스 ***
class Flyable():

    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, location):
        print('{} 방향으로 날아갑니다. [속도 {}]'.format(location, self.flying_speed))


plane = Flyable(10)
plane.fly('1시')

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 공중 유닛
class FlyableUnit(Unit, Flyable):

    def __init__(self, name, hp, flying_speed):
        Unit.__init__(self, name, hp)
        Flyable.__init__(self, flying_speed)


# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 기능은 없음
dropship = FlyableUnit('드랍쉽', 150, 8)
dropship.fly('3시')

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):

    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


# 레이스 : 공중 공격 유닛.
wraith = FlyableAttackUnit('레이스', 100, 6, 10)
wraith.fly('6시')
wraith.attack('6시')
wraith.damaged(20)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit('발키리', 200, 8, 5)
valkyrie.fly('9시')
valkyrie.attack('9시')
valkyrie.damaged(20)