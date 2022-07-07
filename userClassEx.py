# 유저 정보 클래스 만들고 관리 프로그램
class User:
    def __init__(self, name, phone, gender):
        self.name = name
        self.phone = phone
        self.gender = gender
    def info(self):
        print("이름:", self.name)
        print("번호:", self.phone)
        print("성별:", self.gender)

userList = [] # [User, User, User]

num = int(input("반복할 횟수 입력:"))

for i in range(num):
    work = input("명령어 종류 입력(add, remove, find):")

    if work == "add":
        name = input("이름:")
        phone = input("번호:")
        gender = input("성별:")
        user = User(name, phone, gender) # 단일 객체 생성
        userList.append(user)

    elif work == "remove":
        name = input("삭제할 이름 입력:")
        isExist = False

        for j in range(len(userList)):
            if name == userList[j].name: 
                isExist = True
                userList.pop(j)
                print("삭제 완료")
                break

        if isExist == False:
            print("존재하지 않음")

    elif work == "find":
        name = input("찾을 이름:")
        isExist = False

        for j in range(len(userList)):
            if name == userList[j].name:
                isExist = True
                userList[j].info()
                break

        if isExist == False:
            print("존재하지 않음")

for i in userList:
    i.info()
    print("--------------")