# Python 기본 문법 익히기

print("Hello! AI")
print(3.141592 * 10.0 * 10.0)
print((1/100) * 1234)

# 1. 평균 계산해서 출력하기

x=  int(input("첫번째 수: "))
y = int(input("두번째 수: "))
z = int(input("세번째 수: "))

print("평균:", (x+y+z)/3)

# 2. 화씨온도를 입력받아 섭씨온도를 계산하여 섭씨온도 화면에 출력하기

f = float(input("화씨온도를 입력하세요: "))
c = (f-32)*5/9
print("섭씨온도:", c)

# 3. 신장과 체중을 입력받아 BMI 값을 계산하여 계산된 BMI를 화면에 출력하기

kg = float(input("몸무게를 kg 단위로 입력하시오: "))
meter = float(input("키를 m 단위로 입력하시오: "))
bmi = kg/(meter**2)
print("당신의 BMI 수치:", bmi)

# 4. 숫자 입력받아 홀짝 구분하기
num = int(input("숫자를 입력하시오: "))
if num%2 >0:
    print("홀수입니다.")
else: 
    print("짝수입니다.")
print("프로그램 종료.")

# 5. 숫자 하나를 입력받아 7이 아니라면 프로그램 진행, 7이면 종료 출력
num2 = int(input("숫자를 입력하시오: "))
if not (num2==7):
    print("프로그램 진행.")
else:
    print("프로그램 종료")

# 6. 입력한 연도가 윤년인지 아닌지 판단하여 화면에 출력
year = int(input("년도를 입력하시오: "))
if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")
print("프로그램 종료.")

# 7. 입력한 숫자에 따라 수식을 선택 계산하여 출력
num3 = int(input("숫자를 입력하시오: "))
if num3 >= 0:
    print(num3**2 + 2*num3 +1)
else:
    print(num3**3 - num3)

# 8. 1부터 20까지 총합을 계산하고 화면에 결과를 출력하시오.
# 주의: 값이 없는 변수에 숫자를 더할 수 없으므로 초기화 필요

sum = 0
for i in range(1, 21, 1):
    sum += i
print("1부터 20까지 총합: ", sum)

# 9. 숫자 1개를 입력받아 입력받은 정수의 팩토리얼 값을 출력하시오

n = int(input("정수를 입력하세요: "))
factorial = 1

for i in range(1, n+1, 1):
    factorial *= i

print("정수 ", n,"의 facotrial 값: ", factorial)

# 10. 2부터 100까지 짝수의 총합을 계산하고 계산 결과를 출력하시오.

ans = 0
for i in range(1, 101):
    if i%2 == 0:
        ans += i

print("2부터 100까지 짝수의 총합: ", ans)

# 11. 숫자 1개를 입력받아 입력받은 정수의 구구단을 출력하시오.

n = int(input("정수를 입력하시오: "))
for i in range(1, 10, 1):
    print(n,"*",i,"=",n*i)