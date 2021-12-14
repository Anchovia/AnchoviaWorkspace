# 기본 변수 모음
equalSignCount = 52 # print 되는 등호 갯수 변수
inputError = "다시 입력해주시길 바랍니다." # 인풋 에러 문자열 변수

# 학년반관리 관련 변수 모음
# 1학년
dictionaryGrade1Class1 = {'담임' : '김단웅', '인원' : 30}
dictionaryGrade1Class2 = {'담임' : '김점복', '인원' : 27}
dictionaryGrade1Class3 = {'담임' : '이서연','인원' : 25}
listGrade1 = [dictionaryGrade1Class1, dictionaryGrade1Class2, dictionaryGrade1Class3] # 1학년 딕셔너리 모음 리스트

# 2학년
dictionaryGrade2Class1 = {'담임' : '김규태', '인원' : 29}
dictionaryGrade2Class2 = {'담임' : '박진홍', '인원' : 28}
dictionaryGrade2Class3 = {'담임' : '유준영', '인원' : 31}
listGrade2 = [dictionaryGrade2Class1, dictionaryGrade2Class2, dictionaryGrade2Class3] # 2학년 딕셔너리 모음 리스트

# 3학년
dictionaryGrade3Class1 = {'담임' : '홍준서', '인원' : 27}
dictionaryGrade3Class2 = {'담임' : '김진우', '인원' : 33}
dictionaryGrade3Class3 = {'담임' : '박단비', '인원' : 32}
listGrade3 = [dictionaryGrade3Class1, dictionaryGrade3Class2, dictionaryGrade3Class3] # 3학년 딕셔너리 모음 리스트

listGradeGather = [listGrade1, listGrade2, listGrade3] # 1, 2, 3 학년 모음 리스트

# 시간표관리 관련 변수 모음
listSubject = ["국어", "영어", "수학", "사회", "과학", "도덕", "기술가정", "정보", "음악", "미술"] # 전체 과목

# 1학년 시간표
listMondayTimeTable1stGrade = ["국어", "수학", "사회", "기술가정", "체육", "미술"] # 월요일
listTuesdayTimeTable1stGrade = ["미술", "영어", "과학", "정보", "국어", "수학"] # 화요일
listWednesdayTimeTable1stGrade = ["과학", "과학", "사회", "수학", "도덕", "영어"] # 수요일
listThursdayTimeTable1stGrade = ["국어", "정보", "영어", "기술가정", "음악", "수학"] # 목요일
listFridayTimeTable1stGrade = ["체육", "사회", "음악", "도덕", "영어", "국어"] # 금요일
dictionaryTimeTable1stGrade = {"월요일" : listMondayTimeTable1stGrade, "화요일" : listTuesdayTimeTable1stGrade, "수요일" : listWednesdayTimeTable1stGrade, "목요일" : listThursdayTimeTable1stGrade, "금요일" : listFridayTimeTable1stGrade} # 1학년 시간표 모음 딕셔너리

# 2학년 시간표
listMondayTimeTable2ndGrade = ["국어", "수학", "사회", "기술가정", "체육", "미술"] # 월요일
listTuesdayTimeTable2ndGrade = ["미술", "영어", "과학", "정보", "국어", "수학"] # 화요일
listWednesdayTimeTable2ndGrade = ["과학", "과학", "사회", "수학", "도덕", "영어"] # 수요일
listThursdayTimeTable2ndGrade = ["국어", "정보", "영어", "기술가정", "음악", "수학"] # 목요일
listFridayTimeTable2ndGrade = ["체육", "사회", "음악", "도덕", "영어", "국어"] # 금요일
dictionaryTimeTable2ndGrade = {"월요일" : listMondayTimeTable2ndGrade, "화요일" : listTuesdayTimeTable2ndGrade, "수요일" : listWednesdayTimeTable2ndGrade, "목요일" : listThursdayTimeTable2ndGrade, "금요일" : listFridayTimeTable2ndGrade} # 2학년 시간표 모음 딕셔너리

# 3학년 시간표
listMondayTimeTable3rdGrade = ["국어", "수학", "사회", "기술가정", "체육", "미술"] # 월요일
listTuesdayTimeTable3rdGrade = ["미술", "영어", "과학", "정보", "국어", "수학"] # 화요일
listWednesdayTimeTable3rdGrade = ["과학", "과학", "사회", "수학", "도덕", "영어"] # 수요일
listThursdayTimeTable3rdGrade = ["국어", "정보", "영어", "기술가정", "음악", "수학"] # 목요일
listFridayTimeTable3rdGrade = ["체육", "사회", "음악", "도덕", "영어", "국어"] # 금요일
dictionaryTimeTable3rdGrade = {"월요일" : listMondayTimeTable3rdGrade, "화요일" : listTuesdayTimeTable3rdGrade, "수요일" : listWednesdayTimeTable3rdGrade, "목요일" : listThursdayTimeTable3rdGrade, "금요일" : listFridayTimeTable3rdGrade}  # 2학년 시간표 모음 딕셔너리

listTimaTableGather = [dictionaryTimeTable1stGrade, dictionaryTimeTable2ndGrade, dictionaryTimeTable3rdGrade] # 시간표 딕셔너리 모음 리스트

# 일정관리 관련 변수 모음
# 월별 딕셔너리
dictionaryJanuarySchedule = {}
dictionaryFebruarySchedule = {}
dictionaryMarchSchedule = {}
dictionaryAprilSchedule = {}
dictionaryMaySchedule = {}
dictionaryJuneSchedule = {}
dictionaryJulySchedule = {}
dictionaryAugustSchedule = {}
dictionarySeptemberSchedule = {}
dictionaryOctoberSchedule = {}
dictionaryNovemberSchedule = {}
dictionaryDecemberSchedule = {}

listScheduleGather = [dictionaryJanuarySchedule, dictionaryFebruarySchedule, dictionaryMarchSchedule, dictionaryAprilSchedule, dictionaryMaySchedule, dictionaryJuneSchedule, dictionaryJulySchedule, dictionaryAugustSchedule, dictionaryAugustSchedule, dictionarySeptemberSchedule, dictionaryOctoberSchedule, dictionaryNovemberSchedule, dictionaryDecemberSchedule] # 월별 딕셔너리 모음 리스트

# 학년반관리 함수
def gradeClassManagement():
    while 1:
        # 전역변수 선언파트
        global dictionaryGrade1Class1
        global dictionaryGrade1Class2
        global dictionaryGrade1Class3
        global listGrade1
        global dictionaryGrade2Class1
        global dictionaryGrade2Class2
        global dictionaryGrade2Class3
        global listGrade2
        global dictionaryGrade3Class1
        global dictionaryGrade3Class2
        global dictionaryGrade3Class3
        global listGrade3
        global listGradeGather

        # 상호작용 종류에 대해 출력
        print("1. 학년별 담임 및 제적인원 확인")
        print("2. 수정하기")
        print("0. 종료")
        print("=" * equalSignCount)

        logicInput = int(input("입력: ")) # 상호작용 활동에 대해 입력받음

        # 학년별 담임 및 제적인원 확인
        if logicInput == 1:
            # 학년, 반 입력
            print("=" * equalSignCount)
            grade = int(input("확인하고 싶은 학년을 입력하세요: "))
            classes = int(input("확인하고 싶은 반을 입력하세요: "))
            print("=" * equalSignCount)
            
            # 학년이 존재하는가
            if grade == 1 or grade == 2 or grade == 3:
                # 반이 존재하는가
                if classes == 1 or classes == 2 or classes == 3:
                    # 출력부분
                    print("[%d학년 %d반]" % (grade, classes))
                    for key, value in (listGradeGather[grade - 1])[classes - 1].items():
                        if type(value) == str:
                            print("%s: %s" % (key, value))
                        elif type(value) == int:
                            print("%s: %s명" % (key, value))
                else:
                    # 예외처리
                    print(inputError)
            
            else:
                # 예외처리
                print(inputError)

            print("=" * equalSignCount)
        
        # 수정하기
        elif logicInput == 2:
            # 상호작용 종류에 대해 출력
            print("=" * equalSignCount)
            print("1. 담임 수정하기")
            print("2. 제적인원 수정하기")
            print("0. 종료")
            print("=" * equalSignCount)

            logicInput = int(input("입력: ")) # 상호작용 활동에 대해 입력받음
            print("=" * equalSignCount)

            # 담임변경
            if logicInput == 1:
                # 학년, 반, 변경할 담임, 변경 담임 입력받음
                grade = int(input("수정하고 싶은 학년을 입력하세요: "))
                classes = int(input("수정하고 싶은 반을 입력하세요: "))
                oldTeacher = input("수정하고 싶은 담임 성함을 입력하세요: ")
                teacher = input("변경하고 싶은 담임 이름을 입력하세요: ")
                print("=" * equalSignCount)

                # 학년이 존재하는가
                if grade == 1 or grade == 2 or grade == 3:
                    # 반이 존재하는가
                    if classes == 1 or classes == 2 or classes == 3:
                        # 담임이 존재하는가
                        if ((listGradeGather[grade - 1])[classes - 1]["담임"]) in oldTeacher:
                            # 담임 변경
                            ((listGradeGather[grade - 1])[classes - 1])["담임"] = teacher
                            print("%d학년 %d반의 담임 '%s'가 '%s'로 변경되었습니다." % (grade, classes, oldTeacher, teacher))
                        
                        else:
                            # 예외처리
                            print(inputError)
                    
                    else:
                        # 예외처리
                        print(inputError)

                else:
                    # 예외처리
                    print(inputError)
                
                print("=" * equalSignCount)
            
            # 제적인원 변경
            elif logicInput == 2:
                # 학년, 반, 변경을 원하는 인원에 대해 입력받음
                grade = int(input("수정하고 싶은 학년을 입력하세요: "))
                classes = int(input("수정하고 싶은 반을 입력하세요: "))
                personnel = int(input("변경하고 싶은 인원을 입력해주세요: "))
                print("=" * equalSignCount)

                # 학년이 존재하는가
                if grade == 1 or grade == 2 or grade == 3:
                    # 반이 존재하는가
                    if classes == 1 or classes == 2 or classes == 3:
                        # 재적인원 변경
                        oldPersonnel = ((listGradeGather[grade - 1])[classes - 1])["인원"] # 구 인원
                        ((listGradeGather[grade - 1])[classes - 1])["인원"] = personnel # 신 인원
                        print("%d학년 %d반의 인원이 %d명에서 %d명으로 변경되었습니다." % (grade, classes, oldPersonnel, personnel))
                    
                    else:
                        # 예외처리
                        print(inputError)
                
                else:
                    # 예외처리
                    print(inputError)
                
                print("=" * equalSignCount)
            
            # 종료
            elif logicInput == 0:
                continue

            else:
                # 예외처리
                print(inputError)
        
        # 종료
        elif logicInput == 0:
            # 무한반복 탈출
            break

        else:
            # 예외처리
            print(inputError)

# 시간표관리 함수
def timeTableManagement():
    # 전역변수 선언파트
    global listSubject
    global listMondayTimeTable1stGrade
    global listTuesdayTimeTable1stGrade
    global listWednesdayTimeTable1stGrade
    global listThursdayTimeTable1stGrade
    global listFridayTimeTable1stGrade
    global dictionaryTimeTable1stGrade
    global listMondayTimeTable2ndGrade
    global listTuesdayTimeTable2ndGrade
    global listWednesdayTimeTable2ndGrade
    global listThursdayTimeTable2ndGrade
    global listFridayTimeTable2ndGrade
    global dictionaryTimeTable2ndGrade
    global listMondayTimeTable3rdGrade
    global listTuesdayTimeTable3rdGrade
    global listWednesdayTimeTable3rdGrade
    global listThursdayTimeTable3rdGrade
    global listFridayTimeTable3rdGrade
    global dictionaryTimeTable3rdGrade
    global listTimaTableGather

    while 1:
        # 상호작용 종류에 대해 출력
        print("1. 시간표확인")
        print("2. 시간표수정")
        print("0. 종료")
        print("=" * equalSignCount)

        logicInput = int(input("입력: ")) # 상호작용 활동에 대해 입력받음

        # 시간표확인
        if logicInput == 1:
            # 학년 입력받음
            print("=" * equalSignCount)
            grade = int(input("확인하고 싶은 학년을 입력하세요: "))
            print("=" * equalSignCount)

            # 학년이 존재하는가
            if grade == 1 or grade == 2 or grade == 3:
                # 시간표 출력
                print("[%d학년 시간표]" % grade)
                # 딕셔너리 키, 벨류값 출력
                for key, value in listTimaTableGather[grade - 1].items():
                    print("%s - " % key, end = "") # 자동 줄바꿈 제외
                    i = 1 # 교시 출력을 위한 변수 i
                    # 교시 및 과목 출력
                    for j in value:
                        if i <= 5:
                            print("%d교시: %s, " % (i, j), end = "")
                            i += 1
                        elif i == 6:
                            print("%d교시: %s " % (i, j), end = "")
                    print("")

            else:
                # 예외처리
                print(inputError)
        
        # 시간표 수정
        elif logicInput == 2:
            # 학년, 요일, 수정을 원하는 교시, 바꾸고 싶은 과목, 바꿀 과목 입력받음
            print("=" * equalSignCount)
            grade = int(input("수정하고 싶은 학년을 입력하세요: "))
            week = input("수정하고 싶은 요일을 입력하세요: ")
            period = int(input("수정하고 싶은 교시를 입력하세요: "))
            selectSubject = input("바꾸고 싶은 과목을 입력하세요: ")
            changeSubject = input("바꿀 과목을 입력하세요: ")
            print("=" * equalSignCount)

            # 학년이 존재하는가
            if grade == 1 or grade == 2 or grade == 3:
                # 요일이 존재하는가
                if week == "월요일" or week == "화요일" or week == "수요일" or week == "목요일" or week == "금요일":
                    # 교시가 존재하는가
                    if period == 1 or period == 2 or period == 3 or period == 4 or period == 5 or period == 6:
                        # 바꾸고 싶은 과목이 존재하는가
                        if selectSubject in listSubject:
                            # 바꿀 과목이 존재하는가
                            if changeSubject in listSubject:
                                index = ((listTimaTableGather[grade - 1])[week]).index(selectSubject) # 바꾸고 싶은 과목에 대해 리스트 인덱스 찾기
                                ((listTimaTableGather[grade - 1])[week])[index] = changeSubject # 바꾸고 싶은 과목으로 바꾸기

                                print("%d학년 %s의 %d교시 과목인 '%s'과목이 '%s'과목으로 변경되었습니다." % (grade, week, period, selectSubject, changeSubject))
                            
                            else:
                                # 예외처리
                                print(inputError)
                        
                        else:
                            # 예외처리
                            print(inputError)
                    
                    else:
                        # 예외처리
                        print(inputError)
                
                else:
                    # 예외처리
                    print(inputError)
            
            else:
                # 예외처리
                print(inputError)

        # 종료
        elif logicInput == 0:
            # 무한반복 탈출
            break

        # 예외처리
        else:
            print(inputError)

        print("=" * equalSignCount)

# 일정관리 함수
def scheduleManagement():
    # 전역변수 선언파트
    global dictionaryJanuarySchedule
    global dictionaryFebruarySchedule
    global dictionaryMarchSchedule
    global dictionaryAprilSchedule
    global dictionaryMaySchedule
    global dictionaryJuneSchedule
    global dictionaryJulySchedule
    global dictionaryAugustSchedule
    global dictionarySeptemberSchedule
    global dictionaryOctoberSchedule
    global dictionaryNovemberSchedule
    global dictionaryDecemberSchedule
    global listScheduleGather

    while 1:
        # 상호작용 종류에 대해 출력
        print("1. 일정확인")
        print("2. 일정수정")
        print("0. 종료")
        print("=" * equalSignCount)

        logicInput = int(input("입력: ")) # 상호작용 활동에 대해 입력받음

        # 일정확인
        if logicInput == 1:
            # 월 입력받음
            print("=" * equalSignCount)
            month = int(input("확인하고 싶은 월을 입력해주세요: "))
            print("=" * equalSignCount)
            
            # 월이 존재하는가?
            if month == 1 or month == 2 or month == 3 or month == 4 or month == 5 or month == 6 or month == 7 or month == 8 or month == 9 or month == 10 or month == 11 or month == 12:
                # 리스트에 일정이 있는가?
                if len(listScheduleGather[month - 1]) > 0:
                    # 일정 출력
                    print("[%d월 일정]" % month)
                    # 딕셔너리 정렬
                    listScheduleGather[month - 1] = dict(sorted(listScheduleGather[month - 1].items()))
                    # 딕셔너리 내용 출력
                    for key, value in listScheduleGather[month - 1].items():
                        print("%d일 - %s" % (key, value))
                
                # 일정 없을때
                else:
                    print("%d월에는 일정이 존재하지 않습니다." % month)
            
            else:
                # 예외처리
                print(inputError)
            
            print("=" * equalSignCount)
        
        # 일정수정
        elif logicInput == 2:
            while 1:
                # 상호작용 종류에 대해 출력
                print("=" * equalSignCount)
                print("1. 일정추가")
                print("2. 일정삭제")
                print("0. 종료")
                print("=" * equalSignCount)

                logicInput = int(input("입력: ")) # 상호작용 활동에 대해 입력받음
                print("=" * equalSignCount)

                # 일정추가
                if logicInput == 1:
                    # 월, 날짜, 추가하고 싶은 내용에 대해 입력받음
                    month = int(input("추가하고 싶은 월을 입력해주세요: "))
                    day = int(input("추가하고 싶은 날짜를 입력해주세요: "))
                    contents = input("추가하고 싶은 일정 내용을 입력해주세요: ")

                    # 달, 날짜가 존재하는가 ?
                    if ((month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (day >= 0 and day <= 31)):
                        # 일정 추가
                        (listScheduleGather[month - 1])[day] = contents
                        print("=" * equalSignCount)
                        print('%d월 %d일에 "%s" 일정이 추가되었습니다.' % (month, day, contents))

                    elif ((month == 2 and day >= 1) and (day <= 28)):
                        # 일정 추가
                        (listScheduleGather[month - 1])[day] = contents
                        print("=" * equalSignCount)
                        print('%d월 %d일에 "%s" 일정이 추가되었습니다.' % (month, day, contents))

                    elif ((month == 4 or month == 6 or month == 9 or month == 11) and (day >= 0 and day <= 30)):
                        # 일정 추가
                        (listScheduleGather[month - 1])[day] = contents
                        print("=" * equalSignCount)
                        print('%d월 %d일에 "%s" 일정이 추가되었습니다.' % (month, day, contents))

                    else:
                        # 예외처리
                        print(inputError)
                
                # 일정삭제
                elif logicInput == 2:
                    # 월, 날짜 입력받음
                    month = int(input("삭제하고 싶은 월을 입력해주세요: "))
                    day = int(input("삭제하고 싶은 날짜를 입력해주세요: "))

                    # 달, 날짜가 존재하는가?
                    if ((month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (day >= 0 and day <= 31)):
                        # 일정 삭제
                        if day in listScheduleGather[month - 1]:
                            contents = listScheduleGather[month - 1].pop(day)
                            print("=" * equalSignCount)
                            print('%d월 %d일 "%s" 일정이 삭제되었습니다.' % (month, day, contents))

                        # 일정 없을때
                        else:
                            print('%d월 %d일에는 일정이 존재하지 않습니다.' % (month, day))

                    elif ((month == 2 and day >= 1) and (day <= 28)):
                        # 일정 삭제
                        if day in listScheduleGather[month - 1]:
                            contents = listScheduleGather[month - 1].pop(day)
                            print("=" * equalSignCount)
                            print('%d월 %d일 "%s" 일정이 삭제되었습니다.' % (month, day, contents))

                        # 일정 없을때
                        else:
                            print('%d월 %d일에는 일정이 존재하지 않습니다.' % (month, day))

                    elif ((month == 4 or month == 6 or month == 9 or month == 11) and (day >= 0 and day <= 30)):
                        # 일정 삭제
                        if day in listScheduleGather[month - 1]:
                            contents = listScheduleGather[month - 1].pop(day)
                            print("=" * equalSignCount)
                            print('%d월 %d일 "%s" 일정이 삭제되었습니다.' % (month, day, contents))
                        
                        # 일정 없을때
                        else:
                            print('%d월 %d일에는 일정이 존재하지 않습니다.' % (month, day))

                    else:
                        # 예외처리
                        print(inputError)

                # 종료
                elif logicInput == 0:
                    # 무한 반복 탈출
                    break

                # 예외처리
                else:
                    print(inputError)
        
        # 종료
        elif logicInput == 0:
            # 무한 반복 탈출
            break

        # 예외처리
        else:
            print(inputError)

# 도움말 함수
def help():
    # 도움말 출력
    print("해당 프로그램은 다양한 학사 활동을 전산형으로 관리할 수 있게 도와주는 프로그램입니다.")
    print("'1. 학년반관리'를 통해 각 반 별 인원과 담당교사에 대해 확인 및 수정 작업을 진행할 수 있습니다.")
    print("'2. 시간표관리'를 통해 학년별 시간표를 확인 및 수정할 수 있습니다.")
    print("'3. 일정관리'를 통해 월별 일정을 확인 및 수정할 수 있습니다.")
    print("'4. 도움말'을 통해 프로그램 사용법을 숙지할 수 있습니다.")
    print("'0. 종료'를 입력하면 프로그램을 종료합니다.")

# 프로그램 작동부
# 기본 내용 출력
print("=" * equalSignCount)
print("2021 학년도 A 중학교 학사 행정 관리 프로그램입니다.")
print("시행하고 싶은 상호작용에 대해 숫자를 입력해주십시오.")

while 1:
    # 상호작용 종류에 대해 출력
    print("=" * equalSignCount)
    print("1. 학년반관리")
    print("2. 시간표관리")
    print("3. 일정관리")
    print("4. 도움말")
    print("0. 종료")
    print("=" * equalSignCount)

    logicInput = int(input("입력: ")) # 상호작용 활동에 대해 입력받음

    # 받은 입력이 1일때 '학년반관리' 함수 실행
    if logicInput == 1:
        print("=" * equalSignCount)
        gradeClassManagement()
    
    # 받은 입력이 2일때 '시간표관리' 함수 실행
    elif logicInput == 2:
        print("=" * equalSignCount)
        timeTableManagement()

    # 받은 입력이 3일때 '일정관리' 함수 실행
    elif logicInput == 3:
        print("=" * equalSignCount)
        scheduleManagement()

    # 받은 입력이 4일때 '도움말' 함수 실행
    elif logicInput == 4:
        print("=" * equalSignCount)
        help()

    # 받은 입력이 0일때 프로그램 종료
    elif logicInput == 0:
        print("=" * equalSignCount)
        print("프로그램을 종료합니다.")
        print("=" * equalSignCount)
        break

    # 예외처리
    else:
        print(inputError)