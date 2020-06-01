st1=st2=st3=st4=st5=None
data = [st1,st2,st3,st4,st5]
class Student:
    name = ""
    hakk = ""
    hakbun = 0
    korean = 0
    english = 0
    math = 0
    sum = 0
    ave = 0
    hakjum = ''


def Datamake():
    for i in range(0,len(data)):
        data[i] = Student()
        data[i].name = input("이름: ")
        data[i].hakk = input("학과: ")
        data[i].hakbun = int(input("학번: "))
        data[i].korean = int(input("국어: "))
        data[i].english = int(input("영어: "))
        data[i].math = int(input("수학: "))
        data[i].sum = data[i].korean + data[i].english + data[i].math
        print("총점: %d" % (data[i].sum))
        data[i].ave = data[i].sum / 3
        print("평균: %d" % (data[i].ave))
        if data[i].ave >= 90:
            data[i].hakjum = 'A'
        elif data[i].ave >= 80:
            data[i].hakjum = 'B'
        elif data[i].ave >= 70:
            data[i].hakjum = 'C'
        elif data[i].ave >= 60:
            data[i].hakjum = 'D'
        else:
            data[i].hakjum = 'F'
        print("학점: %s" % (data[i].hakjum))

def Search():
    searchname = input("찾을 이름을 검색하시오: ")
    for i in range(0,len(data)):
        if data[i].name == searchname:
            print("이름:", data[i].name, "\n학과:", data[i].hakk, "\n학번:", data[i].hakbun, "\n국어:", data[i].korean, "\n영어:",
                  data[i].english, "\n수학:", data[i].math, "\n총합:", data[i].sum, "\n평균:", data[i].ave)
            print("\n학점:", data[i].hakjum)
            return 1
    print("없는 학생입니다.")
    return 0

def Delname():
    delname = input("삭제할 이름을 입력하시오: ")
    for j in range(0,len(data)):
        if data[j].name == delname:
            del(data[j])
            return 0
def Sortdata():
    min_hak = 0
    temp = 0
    for i in range(0, len(data) - 1):
        min_hak = i
        for j in range(i + 1, len(data)):
            if data[min_hak].hakbun > data[j].hakbun:
                min_hak = j
        temp = data[i]
        data[i] = data[min_hak]
        data[min_hak] = temp

    for i in range(0,len(data)):
        print("이름:", data[i].name, "\n학과:", data[i].hakk, "\n학번:", data[i].hakbun, "\n국어:", data[i].korean, "\n영어:",
              data[i].english, "\n수학:", data[i].math, "\n총합:", data[i].sum, "\n평균:", data[i].ave)
        print("\n학점:", data[i].hakjum)


while True:
    choice = int(input("1. 데이터 추가\n2. 데이터 검색\n3. 데이터 삭제\n4. 데이터 정렬\n5. 종료\n"))
    if choice == 1:
        Datamake()
    elif choice == 2:
        Search()
    elif choice == 3:
        Delname()
    elif choice == 4:
       Sortdata()
    elif choice == 5:
        print("프로그램을 종료합니다.")
        exit()






