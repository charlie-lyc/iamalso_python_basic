# 클래스

# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음.
name = '마린' # 유닛의 이름
hp = 40      # 유닛의 체력
damage = 5   # 유닛의 공격력

print('{} 유닛이 생성되었습니다.'.format(name))
print('체력 {}, 공격력 {}'.format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있음. 일반 모드 / 시즈 모드
tank_name = '탱크'
tank_hp = 150
tank_damage = 35

print('{} 유닛이 생성되었습니다.'.format(tank_name))
print('체력 {}, 공격력 {}'.format(tank_hp, tank_damage))

def attack(name, location, damage):
	print('{}: {} 방향으로 적군을 공격합니다. [공격력 {}]'.format(name, location, damage))

attack(name, '1시', damage)
attack(tank_name, '1시', tank_damage)

# 탱크 1대 더 생성
tank2_name = '탱크2'
tank2_hp = 150
tank2_damage = 35

print('{} 유닛이 생성되었습니다.'.format(tank2_name))
print('체력 {}, 공격력 {}'.format(tank2_hp, tank2_damage))

attack(tank2_name, '2시', tank2_damage)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 유닛
class Unit:
	# _init_ : 생성자 함수
	def __init__(self, name, hp, damage):
		# 멤버 변수 : 클래스내에서 정의된 변수
		self.name = name
		self.hp = hp
		self.damage = damage
		print('{} 유닛이 생성 되었습니다.'.format(self.name))
		print('체력 {}, 공격력 {}'.format(self.hp, self.damage))


# 인스턴스 객체 : 클래스의  생성자 함수에 의해 생성된 객체
marine = Unit('마린', 40, 5)
tank = Unit('탱크', 150, 35)
tank2 = Unit('탱크2', 150, 35)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음) 기능
wraith = Unit('레이스', 80, 5)

# 동일한 클래스를 적용하였기 때문에 동일한 멤버 변수들을 가지고 있음
print('유닛 이름: {}, 체력: {}, 공격력: {}'.format(wraith.name, wraith.hp, wraith.damage))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 멤버 변수의 확장

# 레이스 1기를 더 추가하고, 이 레이스는 클로킹 기능 개발이 완료됨
wraith2 = Unit('레이스2', 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
	print('{}는 현재 클로킹 상태입니다.'.format(wraith2.name))

# if wraith.clocking == True: # AttributeError: 'Unit' object has no attribute 'clocking'
# 	print('{}는 현재 클로킹 상태입니다.'.format(wraith.name))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 공격 유닛
class AttackUnit:

	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage
		print('{} 유닛이 생성 되었습니다.'.format(self.name))
		print('체력 {}, 공격력 {}'.format(self.hp, self.damage))
	# 메소드 함수
	def attack(self, location):
		print('{}: {} 방향으로 적군을 공격합니다. [공격력 {}]'.format(self.name, location, self.damage))
	# 메소드 함수
	def damaged(self, damage):
		print('{}: {} 데미지를 입었습니다.'.format(self.name, damage))
		self.hp -= damage
		if self.hp <= 0:
			print('{}: 파괴되었습니다.'.format(self.name))
		else:
			print('{}: 현재 체력은 {}입니다.'.format(self.name, self.hp))


# 파이어뱃 : 공격 유닛, 화염방시기를 쏠수 있음
firebat = AttackUnit('파이어뱃', 50, 16)
firebat.attack('5시')

# 2번의 공격을 받음
firebat.damaged(25)
firebat.damaged(25)