# 사용자로부터 이름, 키, 체중 값을 입력 받아 
# 비만도를 구하고 출력하는 코드를 작성하시오.

# 비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
# 표준 체중 계산 식 : 표준 체중 = (현재 키 – 100) * 0.9

# 출력 예제 : 홍길동님의 비만도는 112.15% 입니다.
name = input('이름 : ')
tall = float(input('키 : '))
weight = float(input('체중 : '))
std_weight = (tall - 100) * 0.9
pat = weight / std_weight * 100

print('{}님의 비만도는 {:.2f}% 입니다.'.format(name, pat))