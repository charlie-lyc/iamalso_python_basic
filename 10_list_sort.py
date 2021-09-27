# 지하철 칸별로 10명 , 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30
print(subway1, subway2, subway3)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# 리스트 : []
subway = [10, 20, 30]
print(subway)

subway = ['John', 'Jack', 'Pete']
print(subway)
print(subway[0])
print(subway[1])
print(subway[2])
# print(subway[3]) # IndexError: list index out of range

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print('John' in subway)
print('Jack' in subway)
print('Pete' in subway)
print('Jerry' in subway)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# John은 지하철 몇번째 칸에 타고 있는가?
print(subway.index('John') + 1)

# Ethan이 다음 정류장에서 마지막 칸 다음 칸에 탐
subway.append('Ethan')
print(subway)

# Jerry를 John과 Jack사이에 태움
subway.insert(1, 'Jerry')
print(subway)

# 지하철에 타고 있는 사람들을 뒷 칸에서부터 한 명씩 내림 : 총 3명을 내림
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append('John')
print(subway)
print(subway.count('John'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 정렬

# 원본 정렬
num_list = [5, 3, 4, 1, 2]
num_list.sort()             # <list>.sort() : 오름차순 정렬 메소드
print(num_list, end='\n\n')

num_list.sort(reverse=True) # <list>.sort(reverse=True) : 내림차순 정렬 메소드
print(num_list, end='\n\n')

# 원본 순서 뒤집기
num_list.reverse()          # <list>.reverse() : 리스트를 역순으로 배열하는 메소드
print(num_list, end='\n\n')

# 정렬하여 사본으로 반환
num_list = [5, 3, 4, 1, 2]
print(sorted(num_list))               # sorted(<list>) : 오름차순 정렬 빌트인 함수
print(num_list, end='\n\n')

print(sorted(num_list, reverse=True)) # sorted(<list>, reverse=True) : 내림차순 정렬 빌트인 함수
print(num_list, end='\n\n')

# 순서 뒤집어 사본으로 반환
print(reversed(sorted(num_list)))     # reversed(<list>) : 리스트를 역순으로 배열하는 빌트인 함수 - 실행 결과 리스트로 반환되지는 않음
print(list(reversed(sorted(num_list))))
print(num_list, end='\n\n')

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 다양한 자료형과 함께 사용
mix_list = ['John', 20, True]
print(mix_list)

# 리스트 확장
print(mix_list + num_list)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 모두 지우기
num_list.clear()
print(num_list)
