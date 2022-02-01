###################################################################### 라이브러리 파트 ######################################################################

# 라이브러리 선언
import time
import sys
import math

###################################################################### 변수 파트 ######################################################################

# 기본 변수
funcLogic = 0
page = "mainPage"
advPage = "homeTown"

listAdvPageHomeTown = ["homeTown"]
listAdvPageGunShop = ["gunShopPistol", "gunShopRifle", "gunShopShotGun", "gunShopSniper", "gunShopConsumable", "gunShopAmmo"]

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
# 권총 딕셔너리들
dictWeaponPistolNull = {"무기 이름" : "null", "공격력" : 0, "명중률" : 0, "탄창" : 0, "분류" : "권총", "가격" : 0}
dictWeaponPistolUSP = {"무기 이름" : "USP", "공격력" : 10, "명중률" : 60, "탄창" : 8, "분류" : "권총", "가격" : 10}
dictyWeaponPistolGlock19 = {"무기 이름" : "Glock-19", "공격력" : 0, "명중률" : 60, "탄창" : 17, "분류" : "권총", "가격" : 500}
dictWeaponPistolM1911 = {"무기 이름" : "M1911", "공격력" : 0, "명중률" : 65, "탄창" : 7, "분류" : "권총", "가격" : 5000}
dictWeaponPistolHK45 = {"무기 이름" : "HK45", "공격력" : 0, "명중률" : 70, "탄창" : 10, "분류" : "권총", "가격" : 20000}

# 돌격소총 딕셔너리들
dictWeaponRifleNull = {"무기 이름" : "null", "공격력" : 0, "명중률" : 0, "탄창" : 0, "분류" : "돌격소총", "가격" : 0}
dictWeaponRifleM16A4 = {"무기 이름" : "M16A4", "공격력" : 0, "명중률" : 75, "탄창" : 20, "분류" : "돌격소총", "가격" : 500}
dictWeaponRifleG36A3 = {"무기 이름" : "G36A3", "공격력" : 0, "명중률" : 75, "탄창" : 30, "분류" : "돌격소총", "가격" : 5000}
dictWeaponRifleHK416 = {"무기 이름" : "HK416", "공격력" : 0, "명중률" : 85, "탄창" : 30, "분류" : "돌격소총", "가격" : 20000}

# 산탄총 딕셔너리들
dictWeaponShotgunNull = {"무기 이름" : "null", "공격력" : 0, "명중률" : 0, "탄창" : 0, "분류" : "산탄총", "가격" : 0}
dictWeaponShotgunWinchesterM1897 = {"무기 이름" : "Winchester M1897", "공격력" : 0, "명중률" : 50, "탄창" : 24, "분류" : "산탄총", "가격" : 500}
dictWeaponShotgunRemington870 = {"무기 이름" : "Remington 870	", "공격력" : 0, "명중률" : 50, "탄창" : 16, "분류" : "산탄총", "가격" : 5000}
dictWeaponShotgunBenelliM4S90Tectical = {"무기 이름" : "Benelli M4 S90 Tectical	", "공격력" : 0, "명중률" : 60, "탄창" : 16, "분류" : "산탄총", "가격" : 20000}


# 저격소총 딕셔너리들
dictWeaponSniperNull = {"무기 이름" : "null", "공격력" : 0, "명중률" : 0, "탄창" : 0, "분류" : "저격소총", "가격" : 0}
dictWeaponSniperM40 = {"무기 이름" : "M40", "공격력" : 0, "명중률" : 0, "탄창" : 0, "분류" : "저격소총", "가격" : 500}
dictWeaponSniperK14 = {"무기 이름" : "K14", "공격력" : 0, "명중률" : 0, "탄창" : 0, "분류" : "저격소총", "가격" : 5000}
dictWeaponSniperM82 = {"무기 이름" : "M82", "공격력" : 0, "명중률" : 0, "탄창" : 0, "분류" : "저격소총", "가격" : 20000}

# 방어구 관련 함수
dictHelmetNull = {"헬멧 이름" : "null", "방어력" : 0}
dictVestNull = {"방탄복 이름" : "null", "방어력" : 0}
dictBootsNull = {"부츠 이름" : "null", "방어력" : 0}

# 플레이어 장비 관련 변수
playerWeapon = dictWeaponPistolUSP # 플레이어 무기
playerHelmet = dictHelmetNull # 플레이어 헬멧
playerVest = dictVestNull # 플레이어 방탄복
playerBoots = dictBootsNull # 플레이어 부츠
playerAmmo = 0 # 플레이어 탄약

# 플레이어 장비 딕셔너리
dictPlayerEquip = {"무기" : playerWeapon, "헬멧" : playerHelmet, "부츠" : playerBoots, "방탄복" : playerVest, "탄약" : playerAmmo}

# 플레이어 아이템 리스트
listPlayerItemSpace = []

# 플레이어 달러 변수
playerDollar = 100

# 스킬 관련 함수
# 견습생 스킬
dictSkillNoviceDoubleFire = {"직업" : "견습생", "스킬 이름" : "더블 파이어", "데미지" : 100, "명중률" : 90, "탄약 사용량" : 2, "스태미나 사용량" : 25}

# 소총수 스킬
dictSkillRiflemanBulletSpray = {"직업" : "소총수", "스킬 이름" : "소총 난사", "데미지" : 100, "명중률" : 75, "탄약 사용량" : 5, "스태미나 사용량" : 0}

# 돌격병 스킬
dictSkillStormtrooperDoubleShot = {"직업" : "돌격병", "스킬 이름" : "산탄총 연사", "데미지" : 100, "명중률" : 65, "탄약 사용량" : 2, "스태미나 사용량" : 0}

# 플레이어 스킬
listPlayerSkillSpace = []

# 총포상 관련 변수
gunShopSelect = 0 # 총포상 기본 선택지
gunShopAdvSelect = 0 # 총포상 세부 선택지
gunShopUseDollar = 0 # 총포상 사용 달러


# 총포상 물품 리스트
listGunShopGoodsPistol = [dictWeaponPistolUSP, dictyWeaponPistolGlock19, dictWeaponPistolM1911, dictWeaponPistolHK45]
listGunShopGoodsRifle = [dictWeaponRifleM16A4, dictWeaponRifleG36A3, dictWeaponRifleHK416]
listGunShopGoodsShotGun = [dictWeaponShotgunWinchesterM1897, dictWeaponShotgunRemington870, dictWeaponShotgunBenelliM4S90Tectical]
listGunShopGoodsSniper = [dictWeaponSniperM40, dictWeaponSniperK14, dictWeaponSniperM82]
listGunShopGoodsConsumable = []
listGunShopAllGoods = [listGunShopGoodsPistol, listGunShopGoodsRifle, listGunShopGoodsShotGun, listGunShopGoodsSniper, listGunShopGoodsConsumable]

# 기타 출력문
strError = "다시 입력해주세요."
strLine = "============================================================================================================================================================="

# 홈 타운 출력문
strHomeTownLocation = '''[가능한 이동]
1. 총포상
2. 약국
3. 부트 캠프
4. 제작 공방
5. 터미널'''

# 총포상 출력문
# 전체 판매 물품
strGunShopAll = '''[판매 물품]
1. 권총
2. 돌격소총
3. 산탄총
4. 저격소총
5. 공격용 소모품
6. 탄약 (2$)
0. 나가기'''

# 권총 판매 물품
strGunShopPistol = '''[판매 물품]
1. USP (10$)
2. Glock-19 (500$)
3. M1911 (5000$)
4. HK45 (20000$)
0. 뒤로가기'''

# 돌격소총 판매 물품
strGunShopRifle = '''[판매 물품]
1. M16A4 (500$)
2. G36A3 (5000$)
3. HK416 (20000$)
0. 뒤로가기'''

# 산탄총 판매 물품
strGunShopShotGun = '''[판매 물품]
1. Winchester M1897 (500$)
2. Remington 870 (5000$)
3. Benelli M4 S90 Tectical (20000$)
0. 뒤로가기'''

# 저격소총 판매 물품
strGunShopSniper = '''[판매 물품]
1. M40 (500$)
2. K14 (5000$)
3. M82 (20000$)
0. 뒤로가기'''

# 공격용 소모품 판매 물품
strGunShopConsumable = '''[판매 물품]
1. 수류탄 (100$)
2. 연막탄 (100$)
3. 소이 수류탄 (200$)
0. 뒤로가기'''

# 탄약 구매 출력문
strGunShopAmmo = "구매하고 싶은 탄약의 갯수를 입력해주세요. 구매를 원하지 않으면 '0'을 입력해주세요."
strGunShopExit = "총포상을 나갑니다."

# 스텟 상승 출력문
strSetStat = '''[증가시킬 수 있는 스텟]
1. 공격력 (1AP당 플레이어 기본 공격력 1% 증가)
2. 방어력 (1AP당 플레이어 기본 방어력 1% 증가)
3. 민첩성 (1AP당 플레이어 기본 민첩성 1% 증가)
4. 정확도 (1AP당 플레이어 기본 정확도 0.5% 증가)
5. 체력 (1AP당 플레이어 기본 체력 1% 증가)
6. 스태미나 (1AP당 플레이어 기본 스태미나 1% 증가)
0. 취소'''

# 총포상 출력문 리스트
listStrGunShopAllGoods = [strGunShopPistol, strGunShopRifle, strGunShopShotGun, strGunShopSniper, strGunShopConsumable]

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

###################################################################### 함수 파트 ######################################################################

# 명령어 입력 함수
def cmdInputFunc(page):
    if(page == "characterGeneration"):
        cmdInput = input("입력: ")

    else:
        cmdInput = input("입력: ")
        cmdInput = cmdInput.upper()
    
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
    global dictPlayerEquip
    global listPlayerItemSpace
    global listPlayerSkillSpace
    global advPage
    global playerDollar

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
    elif(page == "characterGeneration"):
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
    elif(page == "prologue"):
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
    
    # 총포상 판단
    elif(page == "gunShop"):
        if(cmdInput.isdigit() == True):
            if(float(cmdInput) == int(cmdInput)):
                # 권총 구매하기
                if(advPage == "gunShopPistol"):
                    if(int(cmdInput) > 0 and int(cmdInput) < 5):
                        gunShopSelect = 1 # 권총 구매 선택
                        gunShopAdvSelect = int(cmdInput) # 세부 선택
                        gunShopAmount = 1 # 구매 갯수
                        playerDollar, dictPlayerEquip = gunShopFunc(gunShopSelect, gunShopAdvSelect, gunShopAmount, playerDollar, dictPlayerEquip)

                        print(strLine)
                        print(strGunShopAll)
                        print(strLine)

                        page = "gunShop"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page
                    
                    # 권총 구매 나가기
                    elif(cmdInput == "0"):
                        print(strLine)
                        print(strGunShopAll)
                        print(strLine)

                        page = "gunShop"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page
                    
                    # 예외 처리 (비정상 반환)
                    else:
                        page = "gunShop"
                        advPage = "gunShopPistol"
                        funcLogic = 1
                        return funcLogic, page
                
                # 돌격소총 구매하기
                elif(advPage == "gunShopRifle"):
                    if(int(cmdInput) > 0 and int(cmdInput) < 4):
                        gunShopSelect = 2 # 돌격소총 구매 선택
                        gunShopAdvSelect = int(cmdInput) # 세부 선택
                        gunShopAmount = 1 # 구매 갯수
                        playerDollar, dictPlayerEquip = gunShopFunc(gunShopSelect, gunShopAdvSelect, gunShopAmount, playerDollar, dictPlayerEquip)

                        print(strLine)
                        print(strGunShopAll)
                        print(strLine)

                        page = "gunShop"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page
                    
                    # 돌격소총 구매 나가기
                    elif(cmdInput == "0"):
                        print(strLine)
                        print(strGunShopAll)
                        print(strLine)

                        page = "gunShop"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page

                    # 예외 처리 (비정상 반환)
                    else:
                        page = "gunShop"
                        advPage = "gunShopRifle"
                        funcLogic = 1
                        return funcLogic, page
                
                # 산탄총 구매하기
                elif(advPage == "gunShopShotGun"):
                    if(int(cmdInput) > 0 and int(cmdInput) < 4):
                        gunShopSelect = 3 # 산탄총 구매 선택
                        gunShopAdvSelect = int(cmdInput) # 세부 선택
                        gunShopAmount = 1 # 구매 갯수
                        playerDollar, dictPlayerEquip = gunShopFunc(gunShopSelect, gunShopAdvSelect, gunShopAmount, playerDollar, dictPlayerEquip)

                        print(strLine)
                        print(strGunShopAll)
                        print(strLine)

                        page = "gunShop"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page
                    
                    # 산탄총 구매 나가기
                    elif(cmdInput == "0"):
                        print(strLine)
                        print(strGunShopAll)
                        print(strLine)

                        page = "gunShop"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page

                    # 예외 처리 (비정상 반환)
                    else:
                        page = "gunShop"
                        advPage = "gunShopShotGun"
                        funcLogic = 1
                        return funcLogic, page

                # 저격소총 구매하기
                elif(advPage == "gunShopSniper"):
                    if(int(cmdInput) > 0 and int(cmdInput) < 4):
                        gunShopSelect = 4 # 저격소총 구매 선택
                        gunShopAdvSelect = int(cmdInput) # 세부 선택
                        gunShopAmount = 1 # 구매 갯수
                        playerDollar, dictPlayerEquip = gunShopFunc(gunShopSelect, gunShopAdvSelect, gunShopAmount, playerDollar, dictPlayerEquip)

                        print(strLine)
                        print(strGunShopAll)
                        print(strLine)

                        page = "gunShop"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page
                        
                    
                    # 저격소총 구매 나가기
                    elif(cmdInput == "0"):
                        print(strLine)
                        print(strGunShopAll)
                        print(strLine)

                        page = "gunShop"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page

                    # 예외 처리 (비정상 반환)
                    else:
                        page = "gunShop"
                        advPage = "gunShopSniper"
                        funcLogic = 1
                        return funcLogic, page
                
                # 공격용 소모품 구매하기
                elif(advPage == "gunShopConsumable"):
                    print("아직 구현되지 않은 시스템입니다.")

                    page = "gunShop"
                    advPage = "homeTown"
                    funcLogic = 1
                    return funcLogic, page
                
                # 탄약 구매하기
                elif(advPage == "gunShopAmmo"):
                    if(int(cmdInput) > 0):
                        gunShopSelect = 6 # 탄약 구매 선택
                        gunShopAdvSelect = 0 # 선택 안함
                        gunShopAmount = int(cmdInput) # 구매 갯수
                        playerDollar, dictPlayerEquip = gunShopFunc(gunShopSelect, gunShopAdvSelect, gunShopAmount, playerDollar, dictPlayerEquip)

                        print(strLine)
                        print(strGunShopAll)
                        print(strLine)

                        page = "gunShop"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page
                
                    # 탄약 구매 나가기
                    elif(cmdInput == "0"):
                        print(strLine)
                        print(strGunShopAll)
                        print(strLine)

                        page = "gunShop"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page
                    
                    # 예외 처리 (비정상 반환)
                    else:
                        page = "gunShop"
                        advPage = "gunShopAmmo"
                        funcLogic = 1
                        return funcLogic, page

                # 총포상 나가기
                elif(cmdInput == "0"):
                    print(strGunShopExit)

                    page = "inGame"
                    advPage = "homeTown"
                    funcLogic = 0
                    return funcLogic, page
                
                # 총포상 1~5번 선택
                elif(int(cmdInput) > 0 and int(cmdInput) < 6):
                    print(strLine)
                    print(listStrGunShopAllGoods[int(cmdInput) - 1])
                    print(strLine)

                    page = "gunShop"
                    advPage = listAdvPageGunShop[int(cmdInput) - 1]
                    funcLogic = 0
                    return funcLogic, page

                # 탄약 구매하기
                elif(cmdInput == "6"):
                    print(strLine)
                    print(strGunShopAmmo)
                    print(strLine)

                    page = "gunShop"
                    advPage = "gunShopAmmo"
                    funcLogic = 0
                    return funcLogic, page

                # 예외 처리 (비정상 반환)
                else:
                    funcLogic = 1
                    page = "gunShop"
                    return funcLogic, page

            # 예외 처리 (비정상 반환)    
            else:
                funcLogic = 1
                page = "gunShop"
                return funcLogic, page

        # 예외 처리 (비정상 반환)    
        else:
            funcLogic = 1
            page = "gunShop"
            return funcLogic, page

        # 정상 반환
        funcLogic = 0
        page = "gunShop"
        return funcLogic, page

    # 인게임 페이지 판단
    elif(page == "inGame"):
        # 플레이어 정보창
        if(cmdInput == "P"):
            print(strLine)
            playerInfoFunc(playerName, dictPlayerLv)
            print(strLine)

        # 스텟창
        elif(cmdInput == "S"):
            print(strLine)
            page = statSpaceFunc(dictPlayerStat, dictPlayerPoint, page)
            print(strLine)

            funcLogic = 0
            return funcLogic, page
        
        # 장비창
        elif(cmdInput == "E"):
            print(strLine)
            equipSpaceFunc(dictPlayerEquip)
            print(strLine)
        
        # 스킬창
        elif(cmdInput == "K"):
            print(strLine)
            skillSpaceFunction(listPlayerSkillSpace)
            print(strLine)

        # 아이템창
        elif(cmdInput == "I"):
            print(strLine)
            itemSpaceFunction(listPlayerItemSpace, playerDollar)
            print(strLine)
        
        # 업적창
        elif(cmdInput == "A"):
            print(strLine)
            IllustratedGuideSpaceFunction()
            print(strLine)

        elif(advPage == "homeTown"):
            if(cmdInput == "1"):
                # 총포상 물품 출력
                print(strLine)
                print(strGunShopAll)
                print(strLine)

                page = "gunShop"
                funcLogic = 0
                return funcLogic, page
            
            elif(cmdInput == "2"):
                print("아직 구현되지 않은 시스템입니다.")
            
            elif(cmdInput == "3"):
                print("아직 구현되지 않은 시스템입니다.")

            elif(cmdInput == "4"):
                print("아직 구현되지 않은 시스템입니다.")

            elif(cmdInput == "5"):
                print("아직 구현되지 않은 시스템입니다.")
            
            # 예외 처리 (비정상 반환)
            else:
                funcLogic = 1
                page = "inGame"
                advPage = "homeTown"
                return funcLogic, page

            page = "inGame"
            advPage = "homeTown"
            funcLogic = 0
            return funcLogic, page

        # 예외 처리 (비정상 반환)
        else:
            funcLogic = 1
            page = "inGame"
            return funcLogic, page
            
        # 정상 반환
        funcLogic = 0
        page = "inGame"
        return funcLogic, page
    
    # 스텟창 판단
    elif(page == "stat"):
        # 응답이 Y 일 때
        if(cmdInput == "Y"):
            print(strLine)
            print(strSetStat)
            print(strLine)

            page = "setStat"
        
        # 응답이 N 일 떄
        elif(cmdInput == "N"):
            print("남은 AP: %d" % dictPlayerPoint["AP"])
            print(strLine)

            page = "inGame"
        
        # 예외 처리 (비정상 반환)
        else:
            page = "stat"
            funcLogic = 1
            return funcLogic, page
        
        funcLogic = 0
        return funcLogic, page
    
    # 스텟 상승창 판단
    elif(page == "setStat"):
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
        print(strLine)
        
        page = "inGame"
        funcLogic = 0
        return funcLogic, page
    
    # 예외 처리 (오류 발생)
    else:
        return -1, -1

# 스텟 상승 함수
def setStatFunc(dictPlayerStatAP, dictPlayerPoint, cmdInput):
    print(strLine)
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
def statSpaceFunc(dictPlayerStat, dictPlayerPoint, page):
    print("[스텟 정보]")
    for key, value in dictPlayerStat.items():
        if(key == "민첩성" or key == "정확도" or key == "회피율" or key == "선공확률" or key == "후퇴확률"):
            if(float(value) == int(value)):
                print("●", str(key) + ":", str(int(value)) + "%")
            else:
                print("●", str(key) + ":", str(value) + "%")

        else:
            if(float(value) == int(value)):
                print("●", str(key) + ":", int(value))
            else:
                print("●", str(key) + ":", value)
    
    if(dictPlayerPoint["AP"] > 0):
        print(strLine)
        print("사용 가능한 스텟 포인트가 있습니다.")
        print("사용 하시겠습니까? (Y/N)")

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
def equipSpaceFunc(dictPlayerEquip):
    print("[무기]")
    if(dictPlayerEquip["무기"]["무기 이름"] == "null"):
        print("● 무기를 착용중이지 않습니다.\n")

    else:
        print("● 착용중인 무기: %s\n" % dictPlayerEquip["무기"]["무기 이름"])
    
    print("[방어구]")
    if(dictPlayerEquip["헬멧"]["헬멧 이름"] == "null"):
        print("● 헬멧을 착용중이지 않습니다.")

    else:
        print("● 착용중인 헬멧: %s" % dictPlayerEquip["헬멧"]["헬멧 이름"])

    if(dictPlayerEquip["방탄복"]["방탄복 이름"] == "null"):
        print("● 방탄복을 착용중이지 않습니다.")

    else:
        print("● 착용중인 방탄복: %s" % dictPlayerEquip["방탄복"]["방탄복 이름"])

    if(dictPlayerEquip["부츠"]["부츠 이름"] == "null"):
        print("● 부츠를 착용중이지 않습니다.")

    else:
        print("착용중인 부츠: %s" % dictPlayerEquip["부츠"]["부츠 이름"])

    print("탄약 개수: %d" % dictPlayerEquip["탄약"])

# 스킬창 함수
def skillSpaceFunction(listPlayerSkillSpace):
    print("[에이전트가 소유한 스킬 목록]")
    if(not listPlayerSkillSpace):
        print("에이전트가 습득한 스킬이 존재하지 않습니다.")
        
    else:
        j = 1
        for i in listPlayerSkillSpace:
            print("● %i. %s" % (j, i))
            j += 1

# 아이템창 함수
def itemSpaceFunction(listPlayerItemSpace, playerDollar):
    print("[에이전트가 소유한 아이템 목록]")
    if(not listPlayerItemSpace):
        print("에이전트가 아이템을 소유하고 있지 않습니다.")
        
    else:
        j = 1
        for i in listPlayerItemSpace:
            print("● %i. %s" % (j, i))
            j += 1
    
    print("플레이어가 소유한 달러: %d$" % playerDollar)
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
def statCalculFunc(dictPlayerBasicStat, dictPlayerStatAP, dictPlayerEquip):
    # 플레이어 최종 공격력 계산식
    playerTotalAtk = dictPlayerBasicStat["기본 공격력"] * ((100 + dictPlayerStatAP["공격력 증가량"]) / 100) + dictPlayerEquip["무기"]["공격력"]

    # 플레이어 최종 방어력 계산식
    playerTotalDef = dictPlayerBasicStat["기본 방어력"] * ((100 + dictPlayerStatAP["방어력 증가량"]) / 100) + dictPlayerEquip["헬멧"]["방어력"] + dictPlayerEquip["부츠"]["방어력"] + dictPlayerEquip["방탄복"]["방어력"]

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

# 총포상 함수
def gunShopFunc(gunShopSelect, gunShopAdvSelect, gunShopAmount, playerDollar, dictPlayerEquip):
    if(gunShopSelect > 0 and gunShopSelect < 5):
        # 계산 부분
        gunShopUseDollar = listGunShopAllGoods[gunShopSelect - 1][gunShopAdvSelect - 1]["가격"] # 가격 책정
        if(playerDollar >= gunShopUseDollar):
            playerDollar -= gunShopUseDollar # 무기의 가격 만큼 플레이어 달러 차감
            dictPlayerEquip["무기"] = listGunShopAllGoods[gunShopSelect - 1][gunShopAdvSelect - 1]
            print("%d 달러를 사용하여 %s %s (을)를 구매한 후 장착하였습니다." % (gunShopUseDollar, listGunShopAllGoods[gunShopSelect - 1][gunShopAdvSelect - 1]["분류"], listGunShopAllGoods[gunShopSelect - 1][gunShopAdvSelect - 1]["무기 이름"]))

            return playerDollar, dictPlayerEquip

        else:
            print("돈이 부족합니다.")

            return playerDollar, dictPlayerEquip

    elif(gunShopSelect == 5):
        return playerDollar, dictPlayerEquip

    elif(gunShopSelect == 6):
        # 계산 부분
        gunShopUseDollar = gunShopAmount * 2 # 가격 책정
        if(playerDollar >= gunShopUseDollar):
            playerDollar -= gunShopUseDollar # 플레이어 달러 총알 구매 갯수 만큼 차감
            dictPlayerEquip["탄약"] += gunShopAmount # 플레이어 장비의 탄약 갯수 보충
            print("탄약 %d발을 %d$를 사용해 구매하였습니다." % (gunShopAmount, gunShopUseDollar))

            return playerDollar, dictPlayerEquip

        else:
            print("돈이 부족합니다.")

            return playerDollar, dictPlayerEquip
    
    else:
        print("에러 발생")

        return playerDollar, dictPlayerEquip
        
###################################################################### 프로그램 실행 파트 ######################################################################

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
        if(page == "inGame" and advPage == "homeTown"):
            print(strLine)
            print(strHomeTownLocation)
            print(strLine)

        dictPlayerStat = statCalculFunc(dictPlayerBasicStat, dictPlayerStatAP, dictPlayerEquip)
        page = cmdInputFunc(page)
