#1. -1이 입력될때까지 리스트 입력 받아서 저장(-1은 저장X)
numList = []
while True:
    num = int(input("입력:"))
    if num == -1:
        break
    else:
        numList.append(num)
print(numList)


#2. 이름을 입력 받아서 선언한 리스트에 존재여부와 idx 출력
nameList = ["홍길동", "김철수", "박현진", "이승우", "조재혁", "강승완"]
name = input("찾을 이름: ")
for i in range(len(nameList)):
    if nameList[i] == name:
        print("해당 이름이 ",i,"번째에 있음")
        break
    if i == nameList[-1]:
        print("존재하지 않음")

#3. [84, 3, 53, 59, 20, 98, -1, 32, 16]에서 최댓값과 최솟값의 인덱스 출력하기
num = [84,3,53,59,20,98,-1,32,16]
maxIdx = 0
minIdx = 0
for i in range(len(num)):
    if num[maxIdx] < num[i]:
        maxIdx = i
    if num[minIdx] > num[i]:
        minIdx = i
print("최댓값 인덱스:", maxIdx)
print("최솟값 인덱스:", minIdx)