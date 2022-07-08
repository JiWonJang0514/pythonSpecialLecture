class Student:
    def __init__(self, name, grade, math, eng, kor):
        self.name = name
        self.grade = grade
        self.math = math
        self.eng = eng
        self.kor = kor
    
    def avg(self): # 평균 계산
        return (self.math+self.eng+self.kor)/3

    def info(self): # 정보 출력
        print("이름:", self.name)
        print("학년:", self.grade)
        print("수학:", self.math)
        print("영어:", self.eng)
        print("국어:", self.kor)
        print("평균:", self.avg())

    def exam(self, math, eng, kor): # 시험 보기
        self.math = math
        self.eng = eng
        self.kor = kor


studentNum = int(input("학생수를 입력해주세요:"))
studentList = []

for i in range(studentNum):
    name = input("이름:")
    grade = input("학년:")
    math = int(input("수학 점수:"))
    eng = int(input("영어 점수:"))
    kor = int(input("국어 점수:"))
    std = Student(name, grade, math, eng, kor)
    studentList.append(std)

print("학생 등록 완료")

cmdNum = int(input("명령어 실행할 횟수:"))

for i in range(cmdNum):
    cmd = input("명령어 입력(remove,find,exam):")

    # 삭제
    if cmd == "remove":
        try:
            name = input("삭제할 학생의 이름을 입력해주세요:")

            for j in range(len(studentList)):
                if studentList[j].name == name: 
                    del studentList[j] 
                    print("삭제 성공")
                    break 
                if j == len(studentList)-1: 
                    raise Exception # 에러 반환

        except: # 에러가 있을 때
            print("해당하는 유저가 없습니다.")

    # 찾기
    elif cmd == "find": 
        try:
            name = input("찾을 학생의 이름을 입력해주세요:")

            for j in range(len(studentList)):
                if studentList[j].name == name:
                    studentList[j].info()
                    break
                if j == len(studentList)-1:
                    raise Exception # 에러 반환

        except: # 에러가 있을 때
            print("해당하는 유저가 없습니다.")

    # 시험보기
    elif cmd == "exam":
        try:
            name = input("시험 볼 학생의 이름을 입력해주세요:")

            for j in range(len(studentList)):
                if studentList[j].name == name: 
                    # 새 점수 입력
                    math = int(input("수학 점수:"))
                    eng = int(input("영어 점수:"))
                    kor = int(input("국어 점수:"))
                    # 덮어 씌우기
                    studentList[j].exam(math, eng, kor)
                    break
                if j == len(studentList)-1:
                    raise Exception # 에러 반환

        except: # 에러가 있을 때
            print("해당하는 유저가 없습니다.")


# 최대값 찾기

maxIdx = 0 
if len(studentList) < 1:
    print("학생이 비었습니다")
else:
    for i, std in enumerate(studentList): 
        if studentList[maxIdx].avg() < std.avg():
            maxIdx = i 
    studentList[maxIdx].info()
