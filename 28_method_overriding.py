# 메소드 오버라이딩

# 일반 유닛
class Unit:

    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed # 지상 이동 속도

    def move(self, location):
        print('[지상 유닛 이동]', end='')
        print('{}: {} 방향으로 이동합니다. [속도 {}]'.format(self.name, location, self.speed))


# 공격 유닛
class AttackUnit(Unit):

    def __init__(self, name, hp, speed, damage):
        super().__init__(name, hp, speed)
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


# *** 공중 이동이 가능한 클래스 ***
class Flyable():

    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('[공중 유닛 이동]', end='')
        print('{}: {} 방향으로 날아갑니다. [속도 {}]'.format(name, location, self.flying_speed))


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):

    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 이동 속도 0
        Flyable.__init__(self, flying_speed)


# 벌처 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit('벌쳐', 80, 10, 20)

# 배틀크루저 : 공중 공격 유닛. 체력, 공격력 최고
battlecruiser = FlyableAttackUnit('배틀크루저', 500, 25, 3)

vulture.move('11시')
battlecruiser.fly('배틀크루저', '9시')
# 이렇게 메소드를 이용할 때 마다 지상 또는 공중 유닛인지 확인하고 move 또는 fly를 사용해야 하나?

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):

    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 이동 속도 0
        Flyable.__init__(self, flying_speed)

    # 메소드 오버라이딩(Method Overriding) : 기존의 메소드를 새로운 메소드를 작성하는데 활용(덮어쓰기)
    def move(self, location):
        self.fly(self.name, location)


vulture = AttackUnit('벌쳐', 80, 10, 20)
battlecruiser = FlyableAttackUnit('배틀크루저', 500, 25, 3)

vulture.move('11시')
battlecruiser.move('9시')