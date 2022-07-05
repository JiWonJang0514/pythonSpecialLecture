import random

# 1~50 사이 난수 생성
random_num = random.randrange(1,51)
# while True: #언제 맞힐지 모름 -> 무한루프 사용
#     num = int(input("하나의 숫자 입력: "))
#     if num > random_num:
#         print("숫자가 너무 큽니다")
#     elif num < random_num:
#         print("숫자가 너무 작습니다")
#     else:
#         print("맞습니다")
#         break

#포
family = ["mother", "father", "brother", "me", "sister"]
for i in family:
    print(i)

#레인지 함수
li1 = range(50)
li1 = list(li1)
print(li1)

for i in range(4,50):
    print(i)

#레인지 범위만큼만 포
value = int(input("숫자 입력: "))
for i in range(value):
    print(i)

#구구단
want = int(input("몇 단을 출력할까요: "))
for i in range(1,10):
    print(want, "X" , i, "=", want*i)

for i in range(1,10):
    for j in range(1,10):
        print(i, "X", j, "=", i*j)

#1부터 입력값까지 각각 제곱 프린트
input_num = int(input("정수 입력: "))
for i in range(1, input_num+1):
    print(i, i**2) # ** : 제곱

# if문
money = 2000
card = True
if card == True:
    print("결제 가능")
elif money >= 1000:
    print("결제 가능")
else: 
    print("결제 불가능")

# 함수1
def func1(*args):
    result = 0
    for i in args:
        result+=i
    return result

print(func1(3,5,4325))

# 함수2
def func2(name, old, man=True):
    print(name, old, man)

func2("a", 15)
func2("b", 17)
func2("c", 18, False)

# 함수3
a = 1
def func3(b):
    b += 1

func3(a)
func3(a)


# 파일 쓰기
f = open("새파일.txt","w")
for i in range(10):
    f.write(str(i)+"번째 줄입니다.\n")
f.close()

# 파일 읽기
f = open("새파일.txt","r")
line = f.readline()
print(line)
f.close()

