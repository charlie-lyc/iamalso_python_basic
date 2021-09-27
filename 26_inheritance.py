# 상속

# 일반 유닛 : 부모 클랙스
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 공격 유닛 : 자식 클래스
class AttackUnit(Unit):

    # super() : 부모 클래스(수퍼 클래스) 대신 이용
    def __init__(self, name, hp, damage):
        # Unit.__init__(self, name, hp)
        super().__init__(name, hp)
        self.damage = damage
        print('{} 공격 유닛이 생성 되었습니다.'.format(self.name))
        print('체력 {}, 공격력 {}'.format(self.hp, self.damage))

    def attack(self, location):
        print('{}: {} 방향으로 적군을 공격합니다. [공격력 {}]'.format(self.name, location, self.damage))

    def damaged(self, damage):
        print('{}: {} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print('{}: 파괴되었습니다.'.format(self.name))
        else:
            print('{}: 현재 체력은 {}입니다.'.format(self.name, self.hp))


marine = AttackUnit('마린', 40, 5)
print('유닛 이름: {}, 체력: {}, 공격력: {}'.format(marine.name, marine.hp, marine.damage))

marine.attack('6시')
marine.damaged(20)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 치료 유닛 : 자식 클래스
class HealUnit(Unit):

    # super() : 부모 클래스(수퍼 클래스) 대신 이용
    def __init__(self, name, hp, amount):
        # Unit.__init__(self, name, hp)
        super().__init__(name, hp)
        self.amount = amount
        print('{} 치료 유닛이 생성 되었습니다.'.format(self.name))
        print('체력 {}, 치료력 {}'.format(self.hp, self.amount))

    def heal(self, target):
        print('{}: {}의 체력을 {}만큼 증가시켰습니다.'.format(self.name, target.name, self.amount))
        target.hp += self.amount

    def damaged(self, damage):
        print('{}: {} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print('{}: 파괴되었습니다.'.format(self.name))
        else:
            print('{}: 현재 체력은 {}입니다.'.format(self.name, self.hp))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 메딕 : 의무병
medic = HealUnit('메딕', 60, 5)
print('유닛 이름: {}, 체력: {}, 치료력: {}'.format(medic.name, medic.hp, medic.amount))

medic.heal(marine)
print(marine.hp)

medic.damaged(20)