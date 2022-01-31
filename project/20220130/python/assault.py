# 라이브러리 선언
import time
import sys
import os
import termcolor

# 기본 변수
functionLogic = 0
page = "mainPage"
progress = 1

# 문자 출력 속도 조절
delayTime = 0.05

# 플레이어 관련 변수
playerName = ""
playerJob = "견습생"
playerAtk = 0
playerDef = 0
playerAgi = 0
playerAcc = 0
playerHp = 0
playerStm = 0
playerDmg = 0
playerAvd = 0
playerFatk = 0
playerFlee = 0

dictionaryPlayerStatus = {"이름" : playerName, "직업" : playerJob, "공격력" : playerAtk, "방어력" : playerDef, "민첩성" : playerAgi, "정확도" : playerAcc, "체력" : playerHp, "스태미나" : playerStm, "데미지" : playerDmg, "회피율" : playerAvd, "선공확률" : playerFatk, "후퇴확률" : playerFlee}

# 기타 출력문
strError = "다시 입력해주세요."
strLine = "================================================================================"

# 프롤로그 출력문
strPrologue = '''================================================================================
  [프롤로그]
  203X 년 저녁.
  그 여느 때와 같이 평화롭던 지구 상공에 정체불명의 우주선이 갑작스럽게 등장하게 된다.
  인간들이 대책을 세울 틈도 없이 우주선에서 밝은 빛이 뿜어져 나오게 되고, 그 빛을 따라 외계 우주선들이 튀어나오게 된다.
  외계인들은 놀라 도망치는 인간들을 공격하기 시작하였고, 인간들은 속수무책으로 당하기 시작하며, 주요 도시들이 함락되기에 이른다.
  하지만, 그 와중에 인간들은 끝까지 항전하며 일부 우주선들을 파괴하였고, 특수한 약품이 들은 우주선 한 대를 나포하게 되었다.
  인간들은 이 우주선을 나포하여 수색하게 되고, 해당 우주선의 화물칸 속에는 미지의 약품이 들어있었다.
  해당 약품들을 획득한 정부는 소수의 인간을 데려와 인체실험을 벌이게 되고, 해당 약품을 인간 동맥에 투약하면, 강력한 신체 능력을 갖출 수 있음을 알아내게 된다.
  이에 정부는 이러한 인간들에게 ‘에이전트’라는 이름을 붙이고, 이들을 불러 모아 외계인들과 대적할 군대를 양성하기 시작하였다.
  또한, 해당 약품을 제작해내기 위해 정부는 비밀리에 연구를 시작하게 된다.
'''

# 명령어 입력 함수
def commandInputFunction(page):
    commandInput = input("입력: ")

    functionLogic, page = commandJudgmentFunction(commandInput, page)

    if(functionLogic == 1):
        print(strError)
        return page

    else:
        return page

# 명령어 판단 함수
def commandJudgmentFunction(commandInput, page):
    # 전역변수 선언
    global playerName

    # 메인 페이지 판단
    if(page == "mainPage"):
        if(commandInput == "1"):
            page = "characterGeneration"
            functionLogic = 0
            return functionLogic, page

        elif(commandInput == "2"):
            print("아직 구현되지 않은 시스템입니다.")
            page = "mainPage"
            functionLogic = 1
            return functionLogic, page

        elif(commandInput == "0"):
            print("프로그램을 종료합니다.")
            sys.exit()
        
        else:
            functionLogic = 1
            return functionLogic, page

    # 캐릭터 생성 페이지 판단
    if(page == "characterGeneration"):
        if((len(commandInput) > 0) and (len(commandInput) < 13)):
            if(commandInput.encode().isalpha() == True):
                playerName = commandInput
                print("앞으로 진행할 에이전트의 이름은", playerName, "입니다.")
                page = "prologue"
                functionLogic = 0
                return functionLogic, page

            else:
                functionLogic = 1
                return functionLogic, page

        else:
            functionLogic = 1
            return functionLogic, page

    # 프롤로그 페이지 판단
    if(page == "prologue"):
        if(commandInput == "Y"):
            stringOutputFunction(strPrologue)
            page = "inGame"
            functionLogic = 0
            return functionLogic, page

        elif(commandInput == "N"):
            page = "inGame"
            functionLogic = 0
            return functionLogic, page

        else:
            functionLogic = 1
            return functionLogic, page

    # 인게임 페이지 판단
    if(page == "inGame"):
        if(commandInput == "S"):
            statementSpaceFunction()
            functionLogic = 0
            return functionLogic, page

        elif(commandInput == "E"):
            equipmentSpaceFunction()
            functionLogic = 0
            return functionLogic, page

        elif(commandInput == "K"):
            skillSpaceFunction()
            functionLogic = 0
            return functionLogic, page

        elif(commandInput == "I"):
            itemSpaceFunction()
            functionLogic = 0
            return functionLogic, page

        elif(commandInput == "A"):
            IllustratedGuideSpaceFunction()
            functionLogic = 0
            return functionLogic, page

# 데이터 관리 함수
def dataManagementFunction():
    123

# 스텟창 함수
def statementSpaceFunction():
    123

# 장비창 함수
def equipmentSpaceFunction():
    123

# 스킬창 함수
def skillSpaceFunction():
    123

# 아이템창 함수
def itemSpaceFunction():
    123

# 도감창 함수
def IllustratedGuideSpaceFunction():
    123

# 문자열 출력 함수
def stringOutputFunction(strings):
    for i in strings:
        print(i, end="", flush=True)
        if(i == "."):
            time.sleep(delayTime * 15)
        
        elif(i == ","):
            time.sleep(delayTime * 7.5)

        else:
            time.sleep(delayTime)

while True:
    # 메인 진행 부분
    if(page == "mainPage"):
        print("1. 게임시작")
        print("2. 세이브파일 불러오기")
        print("0. 게임종료")
        print(strLine)
        page = commandInputFunction(page)

    # 캐릭터 생성 부분
    elif(page == "characterGeneration"):
        print(strLine)
        print("앞으로 모험을 시작할 에이전트의 닉네임을 입력해주세요. (1~12글자 공백 없는 영문)")
        print(strLine)
        page = commandInputFunction(page)
    
    # 프롤로그 부분
    elif(page == "prologue"):
        print(strLine)
        print("프롤로그를 보시겠습니까? (Y/N)")
        print(strLine)
        page = commandInputFunction(page)
    
    elif(page == "inGame"):
        progress = 0
        print(strLine)
        page = commandInputFunction(page)
