# 라이브러리 선언
import time
import sys
import math

# 기본 변수
funcLogic = 0
page = "mainPage"
progress = 1

# 문자 출력 속도 조절
timeDelay = 0.045 # 글자 당 출력 속도 (단위: '초')

# 레벨 관련 변수
playerLv = 1 # 플레이어 레벨
playerExp = 0 # 플레이어 경험치
reqExp = 14 # 필요 경험치

# 플레이어 레벨 관련 딕셔너리
dictPlayerLv = {"플레이어 레벨" : playerLv, "플레이어 경험치" : playerExp, "필요 경험치" : reqExp}

# 플레이어 기본 정보 관련 변수
playerName = "" # 플레이어 이름
playerJob = "견습생" # 플레이어 직업

# 플레이어 스텟 관련 변수
playerBasicAtk = 5 # 플레이어 기본 공격력
playerBasicDef = 5 # 플레이어 기본 방어력
playerBasicAgi = 50 # 플레이어 기본 민첩성
playerBasicAcc = 50 # 플레이어 기본 정확도
playerBasicHP = 100 # 플레이어 기본 체력
playerBasicStm = 50 # 플레이어 기본 스태미나

playerTotalAtk = 0 # 플레이어 최종 공격력
playerTotalDef = 0 # 플레이어 최종 방어력
playerTotalAgi = 0 # 플레이어 최종 민첩성
playerTotalAcc = 0 # 플레이어 최종 정확도
playerTotalHP = 0 # 플레이어 최종 체력
playerTotalStm = 0 # 플레이어 최종 스태미나
playerTotalDmg = 0 # 플레이어 최종 데미지
playerTotalAvd = 0 # 플레이어 최종 회피율
playerTotalFatk = 0 # 플레이어 최종 선공확률
playerTotalFlee = 0 # 플레이어 최종 후퇴확률

playerAddAtk = 0 # 플레이어 추가 공격력 %

# 플레이어 기본 스텟 관련 딕셔너리
dictPlayerBasicStat = {"기본 공격력" : playerBasicAtk, "기본 방어력" : playerBasicDef, "기본 민첩성" : playerBasicAgi, "기본 정확도" : playerBasicAcc, "기본 체력" : playerBasicHP, "기본 스태미나" : playerBasicStm}

# 플레이어 최종 스텟 관련 딕셔너리
dictPlayerStat = {"공격력" : playerTotalAtk, "데미지" : playerTotalDmg, "방어력" : playerTotalDef, "민첩성" : playerTotalAgi, "정확도" : playerTotalAcc, "체력" : playerTotalHP, "스태미나" : playerTotalStm, "회피율" : playerTotalAvd, "선공확률" : playerTotalFatk, "후퇴확률" : playerTotalFlee}

# 스텟 포인트, 스킬 포인트 관련 변수
playerAP = 2 # 플레이어 스텟 포인트
playerSP = 0 # 플레이어 스킬 포인트

# 스텟 포인트, 스킬 포인트 관련 딕셔너리
dictPlayerPoint = {"AP" : playerAP, "SP" : playerSP}

# 스텟 포인트로 증가한 포인트
playerAtkAP = 0 # 플레이어 공격력 증가량
playerDefAP = 0 # 플레이어 방어력 증가량
playerAgiAP = 0 # 플레이어 민첩성 증가량
playerAccAP = 0 # 플레이어 정확도 증가량
playerHPAP = 0 # 플레이어 체력 증가량
playerStmAP = 0 # 플레이어 스태미나 증가량

# 플레이어 스탯 포인트 관련 딕셔너리
dictPlayerStatAP = {"공격력 증가량" : playerAtkAP, "방어력 증가량" : playerDefAP, "민첩성 증가량" : playerAgiAP, "정확도 증가량" : playerAccAP, "체력 증가량" : playerHPAP, "스태미나 증가량" : playerStmAP}

# 무기 관련 함수
dictWeaponNull = {"무기 이름" : "null", "공격력" : 0, "명중률" : 0, "탄창" : 0}
dictWeaponPistolUSP = {"무기 이름" : "USP", "공격력" : 10, "명중률" : 60, "탄창" : 8}

# 방어구 관련 함수
dictHelmetNull = {"헬멧 이름" : "null", "방어력" : 0}
dictBootsNull = {"부츠 이름" : "null", "방어력" : 0}
dictVestNull = {"방탄복 이름" : "null", "방어력" : 0}

# 플레이어 장비 관련 변수
playerWeapon = dictWeaponNull
playerHelmet = dictHelmetNull
playerBoots = dictBootsNull
playerVest = dictVestNull
playerAmmo = 0
dictPlayerEquip = {"무기" : playerWeapon["무기 이름"], "헬멧" : playerHelmet["헬멧 이름"], "부츠" : playerBoots["부츠 이름"], "방탄복" : playerVest["방탄복 이름"], "탄약" : playerAmmo}

# 기타 출력문
strError = "다시 입력해주세요."
strLine = "============================================================================================================================================================="

strSetStat = '''[증가시킬 수 있는 스텟]
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

    if(funcLogic == 0):
        return page

    elif(funcLogic == 1):
        print(strError)
        return page
    
    else:
        print("치명적인 에러가 발생하여 게임을 종료합니다.")
        sys.exit()

# 명령어 판단 함수
def cmdJudgFunc(cmdInput, page):
    # 전역변수 선언
    global playerName
    global dictPlayerStatAP
    global dictPlayerPoint
    global dictPlayerLv

    # 메인 페이지 판단
    if(page == "mainPage"):
        if(cmdInput == "1"):
            page = "characterGeneration"
            funcLogic = 0
            return funcLogic, page

        elif(cmdInput == "2"):
            print("아직 구현되지 않은 시스템입니다.")

            funcLogic = 1
            page = "mainPage"
            return funcLogic, page

        elif(cmdInput == "0"):
            print("프로그램을 종료합니다.")
            sys.exit()
        
        # 예외 처리 (비정상 반환)
        else:
            page = "mainPage"
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

        # 예외 처리 (비정상 반환)
        else:
            funcLogic = 1
            page = "characterGeneration"
            return funcLogic, page

    # 프롤로그 페이지 판단
    if(page == "prologue"):
        # 응답이 Y 일 때
        if(cmdInput == "Y"):
            print(strLine)
            strOutputFunc(strPrologue)
            print(strLine)

        # 응답이 N 일 때
        elif(cmdInput == "N"):
            pass

        # 예외 처리 (비정상 반환)
        else:
            funcLogic = 1
            page = "prologue"
            return funcLogic, page
        
        page = "inGame"
        funcLogic = 0
        return funcLogic, page

    # 인게임 페이지 판단
    if(page == "inGame"):
        # 플레이어 정보창
        if(cmdInput == "P"):
            print(strLine)
            playerInfoFunc(playerName, dictPlayerLv)
            print(strLine)

        # 스텟창
        elif(cmdInput == "S"):
            print(strLine)
            page = statSpaceFunc(dictPlayerPoint, page)
            print(strLine)

            funcLogic = 0
            return funcLogic, page
        
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
    
        # 예외 처리 (비정상 반환)
        else:
            funcLogic = 1
            page = "inGame"
            return funcLogic, page
        
        funcLogic = 0
        page = "inGame"
        return funcLogic, page
    
    # 스텟창 판단
    if(page == "stat"):
        # 응답이 Y 일 때
        if(cmdInput == "Y"):
            print(strLine)
            print(strSetStat)
            print(strLine)

            page = "setStat"
        
        # 응답이 N 일 떄
        elif(cmdInput == "N"):
            page = "inGame"
        
        # 예외 처리 (비정상 반환)
        else:
            page = "stat"
            funcLogic = 1
            return funcLogic, page
        
        funcLogic = 0
        return funcLogic, page
    
    # 스텟 상승창 판단
    if(page == "setStat"):
        if(cmdInput == "1"):
            dictPlayerStatAP, dictPlayerPoint = setStatFunc(dictPlayerStatAP, dictPlayerPoint, cmdInput)
        
        elif(cmdInput == "2"):
            dictPlayerStatAP, dictPlayerPoint = setStatFunc(dictPlayerStatAP, dictPlayerPoint, cmdInput)
        
        elif(cmdInput == "3"):
            dictPlayerStatAP, dictPlayerPoint = setStatFunc(dictPlayerStatAP, dictPlayerPoint, cmdInput)
        
        elif(cmdInput == "4"):
            dictPlayerStatAP, dictPlayerPoint = setStatFunc(dictPlayerStatAP, dictPlayerPoint, cmdInput)
        
        elif(cmdInput == "5"):
            dictPlayerStatAP, dictPlayerPoint = setStatFunc(dictPlayerStatAP, dictPlayerPoint, cmdInput)
        
        elif(cmdInput == "6"):
            dictPlayerStatAP, dictPlayerPoint = setStatFunc(dictPlayerStatAP, dictPlayerPoint, cmdInput)

        elif(cmdInput == "0"):
            pass
        
        # 예외처리
        else:
            funcLogic = 1
            return funcLogic, page
        
        print("남은 AP: %d" % dictPlayerPoint["AP"])
        page = "inGame"
        funcLogic = 0
        return funcLogic, page

    # 예외 처리 (오류 발생)
    return -1, -1

# 스텟 상승 함수
def setStatFunc(dictPlayerStatAP, dictPlayerPoint, cmdInput):
    if(cmdInput == "1"):
        print("'공격력'에 1스텟 투자하였습니다.")
        dictPlayerPoint["AP"] -= 1
        dictPlayerStatAP["공격력 증가량"] += 1
        
    elif(cmdInput == "2"):
        print("'방어력'에 1스텟 투자하였습니다.")
        dictPlayerPoint["AP"] -= 1
        dictPlayerStatAP["방어력 증가량"] += 1
        
    elif(cmdInput == "3"):
        print("'민첩성'에 1스텟 투자하였습니다.")
        dictPlayerPoint["AP"] -= 1
        dictPlayerStatAP["민첩성 증가량"] += 1
        
    elif(cmdInput == "4"):
        print("'정확도'에 1스텟 투자하였습니다.")
        dictPlayerPoint["AP"] -= 1
        dictPlayerStatAP["정확도 증가량"] += 1

    elif(cmdInput == "5"):
        print("'체력'에 1스텟 투자하였습니다.")
        dictPlayerPoint["AP"] -= 1
        dictPlayerStatAP["체력 증가량"] += 1

    elif(cmdInput == "6"):
        print("'스태미나'에 1스텟 투자하였습니다.")
        dictPlayerPoint["AP"] -= 1
        dictPlayerStatAP["스태미나 증가량"] += 1
    
    return dictPlayerStatAP, dictPlayerPoint

# 스텟창 함수
def statSpaceFunc(dictPlayerStatAP, page):
    print("[스텟 정보]")
    for key, value in dictPlayerStat.items():
        if(key == "민첩성" or key == "정확도" or key == "회피율" or key == "선공확률" or key == "후퇴확률"):
            print("●", str(key) + ":", str(int(value)) + "%")

        else:
            print("●", str(key) + ":", value)
    
    if(dictPlayerPoint["AP"] > 0):
        print(strLine)
        print("사용 가능한 스텟 포인트가 있습니다.")
        print("사용 하시겠습니까? (Y/N)")
        print(strLine)

        page = "stat"
        return page

    else:
        page = "inGame"
        return page

# 플레이어 정보 함수
def playerInfoFunc(playerName, dictPlayerLv):
    print("[에이전트 정보]")
    print("● 에이전트 이름: %s" % playerName)
    print("● 에이전트 레벨: Lv.%d" % dictPlayerLv["플레이어 레벨"])
    print("● 에이전트의 경험치: %dExp" % dictPlayerLv["플레이어 경험치"])
    print("● 레벨업까지의 필요 경험치: %dExp" % (dictPlayerLv["필요 경험치"] - dictPlayerLv["플레이어 경험치"]))

    return 0

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

# 레벨업 함수
def lvManageFunc(dictPlayerLv, dictPlayerPoint):
    # 연속 레벨업을 위한 무한 반복
    while True:
    # 필요 경험치 계산식
        dictPlayerLv["필요 경험치"] = (((math.log((dictPlayerLv["플레이어 레벨"] ** (1 / 2)) + 1) ** 3) * dictPlayerLv["플레이어 레벨"]) * 10) + 10 + dictPlayerLv["플레이어 레벨"] ** 3
        int(dictPlayerLv["필요 경험치"]) # 정수형으로 변환

        # 레벨업 조건
        if(dictPlayerLv["플레이어 경험치"] >= dictPlayerLv["필요 경험치"]):
            print("레벨업 !!!")
            # 경험치 제거
            dictPlayerLv["플레이어 경험치"] -= dictPlayerLv["필요 경험치"]

            dictPlayerLv["플레이어 레벨"] += 1 # 레벨 증가
            dictPlayerPoint["SP"] += 1 # SP 지급
            dictPlayerPoint["AP"] += 2 # AP 지급
            
        else:
            # 함수 종료 및 반환
            return dictPlayerLv, dictPlayerPoint

# 스텟 계산 함수
def statCalculFunc(dictPlayerBasicStat, dictPlayerStatAP):
    # 플레이어 최종 공격력 계산식
    playerTotalAtk = dictPlayerBasicStat["기본 공격력"] * ((100 + dictPlayerStatAP["공격력 증가량"]) / 100)

    # 플레이어 최종 방어력 계산식
    playerTotalDef = dictPlayerBasicStat["기본 방어력"] * ((100 + dictPlayerStatAP["방어력 증가량"]) / 100)

    # 플레이어 최종 민첩성 계산식
    playerTotalAgi = dictPlayerBasicStat["기본 민첩성"] * ((100 + dictPlayerStatAP["민첩성 증가량"]) / 100)

    # 플레이어 최종 정확도 계산식
    playerTotalAcc = (dictPlayerBasicStat["기본 정확도"] + playerWeapon["명중률"]) / 2 + dictPlayerStatAP["정확도 증가량"] / 2

    # 플레이어 최종 체력 계산식
    playerTotalHp = dictPlayerBasicStat["기본 체력"] * ((100 + dictPlayerStatAP["체력 증가량"]) / 100)

    # 플레이어 최종 스태미나 계산식
    playerTotalStm = dictPlayerBasicStat["기본 스태미나"] * ((100 + dictPlayerStatAP["스태미나 증가량"]) / 100)

    # 플레이어 최종 데미지 계산식
    playerTotalDmg = playerTotalAtk * ((100 + playerAddAtk) / 100)

    # 플레이어 최종 회피율 계산식
    playerTotalAvd = playerTotalAgi / 2

    # 플레이어 최종 선공 확률 계산식
    playerTotalFatk = playerTotalAgi

    # 플레이어 최종 퇴각 확률 계산식
    playerTotalFlee = 50 + playerTotalAgi / 2

    # 딕셔너리에 저장
    dictPlayerStat = {"공격력" : playerTotalAtk, "데미지" : playerTotalDmg, "방어력" : playerTotalDef, "민첩성" : playerTotalAgi, "정확도" : playerTotalAcc, "체력" : playerTotalHp, "스태미나" : playerTotalStm, "회피율" : playerTotalAvd, "선공확률" : playerTotalFatk, "후퇴확률" : playerTotalFlee}

    # 딕셔너리 반환
    return dictPlayerStat

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
    
    # 게임 진행 부분
    else:
        dictPlayerStat = statCalculFunc(dictPlayerBasicStat, dictPlayerStatAP)
        page = cmdInputFunc(page)
