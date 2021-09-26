# 스타크래프트 클래스 총 정리

# 일반 유닛
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


# 공격 유닛
class AttackUnit(Unit):

    def __init__(self, name, hp, speed, damage):
        super().__init__(name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print('{}: {} 방향으로 적군을 공격합니다. [공격력 {}]'.format(self.name, location, self.damage))


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

### '마린' 유닛
class Marine(AttackUnit):

    def __init__(self):
        super().__init__('마린', 40, 1, 5)

    # 스팀팩 : 일정 시간동안 체력 10을 감소 시키면서 이동 및 공격 속도를 증가 시킴
    def stimpack(self):
        if self.hp > 10:
            print('{}: 스팀팩을 사용합니다. 현재 체력 {}, 속도 {} [체력 10 감소, 속도 2 증가]'.format(self.name, self.hp, self.speed))
            self.hp -= 10
            self.speed += 2
            print('{}: 현재 체력 {}, 속도 {}'.format(self.name, self.hp, self.speed))
        else:
            print('{}: 체력이 부족하여 스팀팩을 사용할 수 없습니다.'.format(self.name))


marine1 = Marine()
marine1.move('1시')
marine1.attack('1시')
marine1.damaged(10)
marine1.stimpack()


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

### '탱크' 유닛
class Tank(AttackUnit):

    # 시즈 모드 : 작동되면 고정되어 움직일수 없으나, 공격력이 2배로 증가
    seize_developed = False # 시즈 모드 개발 여부 : 클래스 변수

    def __init__(self):
        super().__init__('탱크', 150, 1, 35)
        self.seize_mode = False # 시즈 모드 변경 상태 : 매개 변수

    # def set_seize_mode(self):
    #     if Tank.seize_developed == True:
    #         print('{}: 시즈 모드를 사용합니다. 현재 속도 {}, 공격력 {} [속도 0, 공격력 2배 설정]'.format(self.name, self.speed, self.damage))
    #         self.seize_mode = True
    #         self.speed = 0
    #         self.damage *= 2
    #         print('{}: 현재 속도 {}, 공격력 {}'.format(self.name, self.speed, self.damage))
    #     else:
    #         print('아직 시즈 모드가 개발되지 않아 사용할 수 없습니다.')
    #         return
    #
    # def unset_seize_mode(self):
    #     if self.seize_mode == True:
    #         print('{}: 시즈 모드를 해제합니다. 현재 속도 {}, 공격력 {} [기본 속도, 공격력 설정]'.format(self.name, self.speed, self.damage))
    #         self.seize_mode = False
    #         self.speed = 1
    #         self.damage /= 2
    #         print('{}: 현재 속도 {}, 공격력 {}'.format(self.name, self.speed, self.damage))
    #     else:
    #         print('시즈 모드 상태가 아닙니다.')
    #         return

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


tank1 = Tank()
tank1.move('1시')
tank1.attack('1시')
tank1.damaged(10)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# tank1.set_seize_mode()
# print(tank1.seize_mode)
#
# Tank.seize_developed = True
# tank1.set_seize_mode()
# print(tank1.seize_mode)
#
# tank1.unset_seize_mode()
# print(tank1.seize_mode)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

tank1.toggle_seize_mode()
print(tank1.seize_mode)

Tank.seize_developed = True
tank1.toggle_seize_mode()
print(tank1.seize_mode)

tank1.toggle_seize_mode()
print(tank1.seize_mode)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# *** 공중 이동이 가능한 클래스 ***
class Flyable():

    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{}: {} 방향으로 날아갑니다. [속도 {}]'.format(name, location, self.flying_speed))


# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):

    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 이동 속도 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

### '레이스' 유닛
class Wraith(FlyableAttackUnit):

    def __init__(self):
        super().__init__('레이스', 80, 20, 5)
        self.clocked = False # 클로킹 모드

    def toggle_clocking(self):
        if self.clocked == False:
            print('{}: 클로킹 모드를 사용합니다.'.format(self.name))
            self.clocked = True
        else:
            print('{}: 클로킹 모드를 해제합니다.'.format(self.name))
            self.clocked = False


wraith1 = Wraith()
wraith1.move('1시')
wraith1.attack('1시')
wraith1.damaged(10)

wraith1.toggle_clocking()
print(wraith1.clocked)
wraith1.toggle_clocking()
print(wraith1.clocked)