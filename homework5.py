data = {}

def Datamake():
    for i in range(0, 5):
        name = input("이름: ")
        hakk = input("학과: ")
        hakbun = int(input("학번: "))
        korean = int(input("국어: "))
        english = int(input("영어: "))
        math = int(input("수학: "))
        sum = korean + english + math
        print("총점: %d" % (sum))
        ave = sum / 3
        print("평균: %d" % (ave))
        if ave >= 90:
            hakjum = 'A'
        elif ave >= 80:
            hakjum = 'B'
        elif ave >= 70:
            hakjum = 'C'
        elif ave >= 60:
            hakjum = 'D'
        else:
            hakjum = 'F'
        print("학점: %s" % (hakjum))
        data[name] = [hakk, hakbun, korean, english, math, sum, ave, hakjum]

def Search():
    searchname = input("찾을 이름을 검색하시오: ")
    if data.get(searchname) is None:
        print("없는 학생입니다.")
    else:
        print(data.get(searchname))

def Sortdata():
    import operator
    sort_data = sorted(data.items(), key=operator.itemgetter(1))
    print(sort_data)

while True:
    choice = int(input("1. 데이터 추가\n2. 데이터 검색\n3. 데이터 삭제\n4. 데이터 정렬\n5. 종료\n"))
    if choice == 1:
        Datamake()
    elif choice == 2:
        Search()
    elif choice == 3:
        delname = input("삭제할 학생의 이름을 입력하시오: ")
        del(data[delname])
    elif choice == 4:
       Sortdata()
    elif choice == 5:
        print("프로그램을 종료합니다.")
        exit()













    