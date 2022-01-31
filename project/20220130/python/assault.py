# 라이브러리 선언
import time
import sys
import os
import termcolor

# 기본 변수
funcLogic = 0
page = "mainPage"
progress = 1

# 문자 출력 속도 조절
timeDelay = 0.045

# 플레이어 스텟 관련 변수
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
dictPlayerStat = {"이름" : playerName, "직업" : playerJob, "공격력" : playerAtk, "방어력" : playerDef, "민첩성" : playerAgi, "정확도" : playerAcc, "체력" : playerHp, "스태미나" : playerStm, "데미지" : playerDmg, "회피율" : playerAvd, "선공확률" : playerFatk, "후퇴확률" : playerFlee}

playerAP = 2
playerSP = 0

# 플레이어 장비 관련 변수
playerWeapon = ""
playerHelmet = ""
playerBoots = ""
playerArmor = ""
playerAmmo = 0
dictPlayerEquip = {"무기" : playerWeapon, "헬멧" : playerHelmet, "부츠" : playerBoots, "방탄복" : playerArmor, "탄약" : playerAmmo}

# 기타 출력문
strError = "다시 입력해주세요."
strLine = "============================================================================================================================================================="

strSetStat = '''[가능한 입력]
1. 공격력
2. 방어력
3. 민첩성
4. 정확도
5. 체력
6. 스태미나
0. 취소'''

# 프롤로그 출력문
strPrologue = '''
  [프롤로그]
  203X 년 저녁.
  그 여느 때와 같이 평화롭던 지구 상공에 정체불명의 우주선이 갑작스럽게 등장하게 된다.
  인류가 대책을 세울 틈도 없이 우주선에서 밝은 빛이 뿜어져 나오게 되고, 그 빛을 따라 외계 우주선들이 튀어나오게 된다.
  외계인들은 놀라 도망치는 인간들을 공격하기 시작하였고, 인류는 속수무책으로 당하기 시작하며, 주요 도시들이 함락되기에 이른다.
  하지만, 그 와중에 인류는 끝까지 항전하며 일부 우주선들을 파괴하였고, 특수한 약품이 들은 우주선 한 대를 나포하게 되었다.
  인류는 이 우주선을 수색하게 되고, 우주선의 화물칸 속에는 미지의 약품이 들어있었다.
  해당 약품들을 획득한 정부는 소수의 인간을 데려와 인체실험을 벌이게 되고, 해당 약품을 인간 동맥에 투약하면, 강력한 신체 능력을 갖출 수 있음을 알아내게 된다.
  이에 정부는 이러한 인간들에게 ‘에이전트’라는 이름을 붙이고, 이들을 불러 모아 외계인들과 대적할 군대를 양성하기 시작하였다.
  또한, 해당 약품을 제작해내기 위해 정부는 비밀리에 연구를 시작하게 된다.

'''

# 명령어 입력 함수
def cmdInputFunc(page):
    cmdInput = input("입력: ")
    
    funcLogic, page = cmdJudgFunc(cmdInput, page)

    if(funcLogic == 1):
        print(strError)
        return page

    else:
        return page

# 명령어 판단 함수
def cmdJudgFunc(cmdInput, page):
    # 전역변수 선언
    global playerName
    global playerAtk
    global playerDef
    global playerAgi
    global playerAcc
    global playerHp
    global playerStm
    global dictPlayerStat

    # 메인 페이지 판단
    if(page == "mainPage"):
        if(cmdInput == "1"):
            page = "characterGeneration"
            funcLogic = 0
            return funcLogic, page

        elif(cmdInput == "2"):
            print("아직 구현되지 않은 시스템입니다.")
            funcLogic = 1
            return funcLogic, page

        elif(cmdInput == "0"):
            print("프로그램을 종료합니다.")
            sys.exit()
        
        else:
            funcLogic = 1
            return funcLogic, page

    # 캐릭터 생성 페이지 판단
    if(page == "characterGeneration"):
        if((len(cmdInput) > 0) and (len(cmdInput) < 13)):
            playerName = cmdInput
            print("앞으로 진행할 에이전트의 이름은 '%s'입니다." % (playerName))
            page = "prologue"
            funcLogic = 0
            return funcLogic, page

        else:
            funcLogic = 1
            return funcLogic, page

    # 프롤로그 페이지 판단
    if(page == "prologue"):
        if(cmdInput == "Y"):
            print(strLine)
            strOutputFunc(strPrologue)
            print(strLine)
            page = "inGame"
            funcLogic = 0
            return funcLogic, page

        elif(cmdInput == "N"):
            page = "inGame"
            funcLogic = 0
            return funcLogic, page

        else:
            funcLogic = 1
            return funcLogic, page

    # 인게임 페이지 판단
    if(page == "inGame"):
        # 스텟창
        if(cmdInput == "S"):
            print(strLine)
            page = statSpaceFunc(page)
            print(strLine)
        
        # 장비창
        elif(cmdInput == "E"):
            print(strLine)
            equipSpaceFunc()
            print(strLine)
        
        # 스킬창
        elif(cmdInput == "K"):
            print(strLine)
            skillSpaceFunction()
            print(strLine)

        # 아이템창
        elif(cmdInput == "I"):
            print(strLine)
            itemSpaceFunction()
            print(strLine)
        
        # 업적창
        elif(cmdInput == "A"):
            print(strLine)
            IllustratedGuideSpaceFunction()
            print(strLine)
    
        # 예외처리
        else:
            funcLogic = 1
            return funcLogic, page

        funcLogic = 0
        return funcLogic, page
    
    # 스텟창 판단
    if(page == "stat"):
        if(cmdInput == "Y"):
            print(strLine)
            print(strSetStat)
            print(strLine)
            page = "setStat"

        elif(cmdInput == "N"):
            page = "ingame"
        
        else:
            funcLogic = 1
            return funcLogic, page
        
        funcLogic = 0
        return funcLogic, page
    
    # 스텟 상승창 판단
    if(page == "setStat"):
        if(cmdInput == "1"):
            print("테스트 성공!")
            page = "ingame"
            funcLogic = 0
            return funcLogic, page
        
        elif(cmdInput == "2"):
            print("테스트 성공!")
            page = "ingame"
            funcLogic = 0
            return funcLogic, page
        
        elif(cmdInput == "3"):
            print("테스트 성공!")
            page = "ingame"
            funcLogic = 0
            return funcLogic, page
        
        elif(cmdInput == "4"):
            print("테스트 성공!")
            page = "ingame"
            funcLogic = 0
            return funcLogic, page
        
        elif(cmdInput == "5"):
            print("테스트 성공!")
            page = "ingame"
            funcLogic = 0
            return funcLogic, page
        
        elif(cmdInput == "6"):
            print("테스트 성공!")
            page = "ingame"
            funcLogic = 0
            return funcLogic, page

        elif(cmdInput == "0"):
            print("테스트 성공!")
            page = "ingame"
            funcLogic = 0
            return funcLogic, page
        
        # 예외처리
        else:
            funcLogic = 1
            return funcLogic, page

# 스텟창 함수
def statSpaceFunc(page):
    for key, value in dictPlayerStat.items():
        print(str(key) + ":", value)
    
    if(playerAP > 0):
        print(strLine)
        print("사용 가능한 스텟 포인트가 있습니다.")
        print("사용 하시겠습니까? (Y/N)")
        print(strLine)

        page = "stat"
        return page

# 장비창 함수
def equipSpaceFunc():
    print("착용중인 무기: ")

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
def strOutputFunc(strs):
    for i in strs:
        print(i, end="", flush=True)
        if(i == "."):
            time.sleep(timeDelay * 15)
        
        elif(i == ","):
            time.sleep(timeDelay * 7.5)

        else:
            time.sleep(timeDelay)

while True:
    # 메인 진행 부분
    if(page == "mainPage"):
        print(strLine)
        print("1. 게임시작")
        print("2. 세이브파일 불러오기")
        print("0. 게임종료")
        print(strLine)
        page = cmdInputFunc(page)

    # 캐릭터 생성 부분
    elif(page == "characterGeneration"):
        print(strLine)
        print("앞으로 모험을 시작할 에이전트의 닉네임을 입력해주세요. (1~12글자 공백 없는 영문)")
        print(strLine)
        page = cmdInputFunc(page)
    
    # 프롤로그 부분
    elif(page == "prologue"):
        print(strLine)
        print("프롤로그를 보시겠습니까? (Y/N)")
        print(strLine)
        page = cmdInputFunc(page)
    
    else:
        progress = 0
        dictPlayerStat = {"이름" : playerName, "직업" : playerJob, "공격력" : playerAtk, "방어력" : playerDef, "민첩성" : playerAgi, "정확도" : playerAcc, "체력" : playerHp, "스태미나" : playerStm, "데미지" : playerDmg, "회피율" : playerAvd, "선공확률" : playerFatk, "후퇴확률" : playerFlee}
        page = cmdInputFunc(page)
