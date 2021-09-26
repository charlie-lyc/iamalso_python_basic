class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print('{} 유닛이 생성되었습니다.'.format(self.name))
    def move(self, location):
        print('{}: {} 방향으로 이동합니다. [속도 {}]'.format(self.name, location, self.speed))
    def damaged(self, damage):
        print('{}: {} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print('{}: 파괴되었습니다.'.format(self.name))
        else:
            print('{}: 현재 체력은 {}입니다.'.format(self.name, self.hp))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        super().__init__(name, hp, speed)
        self.damage = damage
    def attack(self, location):
        print('{}: {} 방향으로 적군을 공격합니다. [공격력 {}]'.format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        super().__init__('마린', 40, 1, 5)
    def stimpack(self):
        if self.hp > 10:
            print('{}: 스팀팩을 사용합니다. 현재 체력 {}, 속도 {} [체력 10 감소, 속도 2 증가]'.format(self.name, self.hp, self.speed))
            self.hp -= 10
            self.speed += 2
            print('{}: 현재 체력 {}, 속도 {}'.format(self.name, self.hp, self.speed))
        else:
            print('{}: 체력이 부족하여 스팀팩을 사용할 수 없습니다.'.format(self.name))

class Tank(AttackUnit):
    seize_developed = False
    def __init__(self):
        super().__init__('탱크', 150, 1, 35)
        self.seize_mode = False
    def toggle_seize_mode(self):
        if Tank.seize_developed == True:
            if self.seize_mode == False:
                print('{}: 시즈 모드를 사용합니다. 현재 속도 {}, 공격력 {} [속도 0, 공격력 2배로 설정]'.format(self.name, self.speed, self.damage))
                self.seize_mode = True
                self.speed = 0
                self.damage *= 2
                print('{}: 현재 속도 {}, 공격력 {}'.format(self.name, self.speed, self.damage))
            else:
                print('{}: 시즈 모드를 해제합니다. 현재 속도 {}, 공격력 {} [기본 속도, 공격력으로 설정]'.format(self.name, self.speed, self.damage))
                self.seize_mode = False
                self.speed = 1
                self.damage /= 2
                print('{}: 현재 속도 {}, 공격력 {}'.format(self.name, self.speed, self.damage))
        else:
            print('아직 시즈 모드가 개발되지 않아 사용할 수 없습니다.')
            return

class Flyable():
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print('{}: {} 방향으로 날아갑니다. [속도 {}]'.format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        super().__init__('레이스', 80, 20, 5)
        self.clocked = False
    def toggle_clocking(self):
        if self.clocked == False:
            print('{}: 클로킹 모드를 사용합니다.'.format(self.name))
            self.clocked = True
        else:
            print('{}: 클로킹 모드를 해제합니다.'.format(self.name))
            self.clocked = False

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 보조 함수 : 게임 시작과 끝
def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    print('Player: gg')
    print('[Player]님이 게임에서 퇴장하셨습니다.')

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 스타크래프트 실제 게임

# 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()
# 탱크 2기 생성
t1 = Tank()
t2 = Tank()
# 레이스 1기 생성
w1 = Wraith()

# 공격 유닛 일괄 행동
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전 유닛 이동
for unit in attack_units:
    unit.move('1시')

# 이동 중 탱크 시즈 모드 개발 완료
Tank.seize_developed = True
print('[알림] 탱크 시즈 모드 개발이 완료되었습니다.')

# 이동하다가 적을 만나게 되어서 교전 준비 : 마린은 스팀백 사용, 탱크는 시즈 모드로 전환, 레이스는 클로킹 모드로 전환
for unit in attack_units:
    # if unit.name == '마린':
    if isinstance(unit, Marine):
        unit.stimpack()
    # elif unit.name == '탱크':
    elif isinstance(unit, Tank):
        unit.toggle_seize_mode()
    # elif unit.name == '레이스':
    elif isinstance(unit, Wraith):
        unit.toggle_clocking()

# 전 유닛 공격
for unit in attack_units:
    unit.attack('1시')

import random

# 전군 피해 상황
for unit in attack_units:
    # unit.damaged(random.randrange(5, 51))
    unit.damaged(random.randint(5, 50))

# 피해를 너무 많이 입어서 게임 포기하고 끝냄
game_over()