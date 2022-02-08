###################################################################### 라이브러리 파트 ######################################################################

# 라이브러리 선언
import time
import sys
import math
import random

###################################################################### 변수 파트 ######################################################################
########## 수치 변경 가능 변수 ##########
# 문자 출력 속도 조절
timeDelay = 0.045 # 글자 당 출력 속도 (단위: '초')

# 레벨 관련 변수
playerLv = 1 # 플레이어 레벨
playerExp = 0 # 플레이어 경험치
reqExp = 14 # 필요 경험치

# 플레이어 스텟 관련 변수
playerBasicAtk = 5 # 플레이어 기본 공격력
playerBasicDef = 5 # 플레이어 기본 방어력
playerBasicAgi = 50 # 플레이어 기본 민첩성
playerBasicAcc = 50 # 플레이어 기본 정확도
playerBasicHP = 100 # 플레이어 기본 체력
playerBasicStm = 50 # 플레이어 기본 스태미나

playerAddAtk = 0 # 플레이어 추가 공격력 %

# 스텟 포인트, 스킬 포인트 관련 변수
playerAP = 2 # 플레이어 스텟 포인트
playerSP = 0 # 플레이어 스킬 포인트

# 플레이어 달러 변수
playerDollar = 100

########## 수치 변경 불가능 변수 ##########
# 기본 변수들
# 기본 변수
funcLogic = 0 # 정상 종료 판단 함수
page = "mainPage" # 페이지 함수
advPage = "homeTown" # 세부 페이지 함수
situation = "null"

# 세부 페이지 관련 리스트
listAdvPageHomeTown = ["homeTown"] 
listAdvPageGunShop = ["gunShopPistol", "gunShopRifle", "gunShopShotGun", "gunShopSniper", "gunShopConsumable", "gunShopAmmo"]
listAdvPagePharmacy = ["pharmacyBandage", "pharmacyPainkiller", "pharmacyMedicalKit", "pharmacyStimulant"]

gameProgress = 1 # 게임 진행도

# 플레이어 레벨 관련 딕셔너리
dictPlayerLv = {"플레이어 레벨" : playerLv, "플레이어 경험치" : playerExp, "필요 경험치" : reqExp}

# 플레이어 기본 정보 관련 변수
playerName = "" # 플레이어 이름
playerJob = "견습생" # 플레이어 직업

# 플레이어 스텟 관련 변수
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

# 플레이어 기본 스텟 관련 딕셔너리
dictPlayerBasicStat = {"기본 공격력" : playerBasicAtk, "기본 방어력" : playerBasicDef, "기본 민첩성" : playerBasicAgi, "기본 정확도" : playerBasicAcc, "기본 체력" : playerBasicHP, "기본 스태미나" : playerBasicStm}

# 플레이어 최종 스텟 관련 딕셔너리
dictPlayerStat = {"공격력" : playerTotalAtk, "데미지" : playerTotalDmg, "방어력" : playerTotalDef, "민첩성" : playerTotalAgi, "정확도" : playerTotalAcc, "체력" : playerTotalHP, "스태미나" : playerTotalStm, "회피율" : playerTotalAvd, "선공확률" : playerTotalFatk, "후퇴확률" : playerTotalFlee}

# 스텟 포인트, 스킬 포인트 관련 딕셔너리
dictPlayerPoint = {"AP" : playerAP, "SP" : playerSP}

# 스텟 포인트, 스킬 포인트 관련 변수
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

# 방어구 관련 변수
dictHelmetNull = {"헬멧 이름" : "null", "방어력" : 0}
dictVestNull = {"방탄복 이름" : "null", "방어력" : 0}
dictBootsNull = {"부츠 이름" : "null", "방어력" : 0}

# 플레이어 장비 관련 변수
playerWeapon = dictWeaponPistolNull # 플레이어 무기
playerHelmet = dictHelmetNull # 플레이어 헬멧
playerVest = dictVestNull # 플레이어 방탄복
playerBoots = dictBootsNull # 플레이어 부츠
playerAmmo = 0 # 플레이어 탄약

# 소모품 관련 변수
# 회복용 소모품 관련 변수
dictConsumableRestorativeBandage = {"이름" : "밴드", "회복량" : 25, "가격" : 10, "지속 시간" : 1}
dictConsumableRestorativePainkiller = {"이름" : "진통제", "회복량" : 50, "가격" : 100, "지속 시간" : 1}
dictConsumableRestorativeMedicalKit = {"이름" : "의료키트", "회복량" : 75, "가격" : 500, "지속 시간" : 1}
dictConsumableRestorativeStimulant = {"이름" : "전투 자극제", "회복량" : 0, "가격" : 500, "지속 시간" : 3}

# 플레이어 장비 딕셔너리
dictPlayerEquip = {"무기" : playerWeapon, "헬멧" : playerHelmet, "부츠" : playerBoots, "방탄복" : playerVest, "탄약" : playerAmmo}

# 플레이어 아이템 리스트
listPlayerItemSpace = []

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
#기본 변수
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

# 약국 관련 변수
# 기본 변수
pharmacyShopSelect = 0 # 약국 기본 선택지
pharmacyUseDollar = 0 # 약국 사용 달러

# 약국 물품 리스트
listPharmacyShopAllGoods = [dictConsumableRestorativeBandage, dictConsumableRestorativePainkiller, dictConsumableRestorativeMedicalKit, dictConsumableRestorativeStimulant]

# 몬스터 관련 변수
# 몬스터 관련 딕셔너리
monsterTrainingDummyBot = {"이름" : "훈련용 더미봇", "체력": 10, "데미지" : 0, "방어력" : 0, "회피율" : 0, "정확도" : 0, "드랍 테이블" : {"경험치" : 1, "달러" : 0, "부품" : "null"}}
monsterSmallAlienCombatDrone = {"이름" : "소형 외계 전투 드론", "체력" : 100, "데미지" : 10, "방어력" : 5, "회피율" : 25, "정확도" : 75, "드랍 테이블" : {"경험치" : 10, "달러" : 10, "부품" : "null"}}


# 터미널 관련 변수
# 경로 딕셔너리
dictTerminalRange = {"이름" : "사격장", "필요 진행도" : 1, "등장 몬스터" : [monsterTrainingDummyBot]}
dictTerminalAvenuePark = {"이름" : "에버뉴 공원", "필요 진행도" : 2, "등장 몬스터" : [monsterSmallAlienCombatDrone]}

# 모든 경로 리스트
listTerminalAllLocation = [dictTerminalRange, dictTerminalAvenuePark]

# 이동 가능한 경로 리스트
listPlayerTerminalPossibleLocation = [dictTerminalAvenuePark]

# 문자열 관련 변수
# 메인 화면 출력문
strMainPage = '''● 1. 게임 시작
● 2. 세이브 파일 불러오기
● 0. 게임 종료'''

# 캐릭터 생성 화면 출력문
strCharacterGeneration = "[SYSTEM] 앞으로 모험을 시작할 에이전트의 닉네임을 입력해주세요 (1~12글자)."

# 프롤로그 관련 출력문
strPrologueJudg = "[SYSTEM] 프롤로그를 보시겠습니까 (Y/N)?"

# 기타 출력문
strError = "[SYSTEM] 다시 입력해주세요."
strFatalError = "[SYSTEM] 치명적인 에러가 발생하여 게임을 종료합니다."
strLine = "============================================================================================================================================================="
strDummy = "[SYSTEM] 아직 구현되지 않은 시스템입니다."
strProgramExit = "[SYSTEM] 프로그램을 종료합니다."
strNoMoney = "[SYSTEM] 돈이 부족합니다."
# 홈 타운 출력문
strHomeTownLocation = '''현재 위치: 홈타운

■ [가능한 이동]
├─● 1. 총포상
├─● 2. 약국
├─● 3. 부트 캠프
├─● 4. 제작 공방
├─● 5. 터미널
└─● 0. 게임 종료'''

# 스텟창 
strStatJudg1 = "[SYSTEM] 사용 가능한 스텟 포인트가 있습니다."
strStatJudg2 = "[SYSTEM] 사용 하시겠습니까 (Y/N)?"
listStrStatJudg = [strStatJudg1, strStatJudg2]

# 스텟창 스텟 문자열 리스트
listStrStats = ["공격력", "방어력", "민첩성", "정확도", "체력", "스태미나"] # 스텟들
listStrStatIncrease = ["공격력 증가량", "방어력 증가량", "민첩성 증가량", "정확도 증가량", "체력 증가량", "스태미나 증가량"] # 스텟 증가량들

# 아이템창 관련 출력문
strPlayerOwnItem = "[에이전트가 소유한 아이템 목록]"
strPlayerItemSpaceEmpty = "● 에이전트가 아이템을 소유하고 있지 않습니다."

# 총포상 출력문
# 전체 판매 물품
strGunShopAll = '''■ [판매 물품]
├─● 1. 권총
├─● 2. 돌격소총
├─● 3. 산탄총
├─● 4. 저격소총
├─● 5. 공격용 소모품
├─● 6. 탄약 (2$)
└─● 0. 나가기'''

# 권총 판매 물품
strGunShopPistol = '''■ [판매 물품]
├─● 1. USP (10$)
├─● 2. Glock-19 (500$)
├─● 3. M1911 (5000$)
├─● 4. HK45 (20000$)
└─● 0. 뒤로가기'''

# 돌격소총 판매 물품
strGunShopRifle = '''■ [판매 물품]
├─● 1. M16A4 (500$)
├─● 2. G36A3 (5000$)
├─● 3. HK416 (20000$)
└─● 0. 뒤로가기'''

# 산탄총 판매 물품
strGunShopShotGun = '''■ [판매 물품]
├─● 1. Winchester M1897 (500$)
├─● 2. Remington 870 (5000$)
├─● 3. Benelli M4 S90 Tectical (20000$)
└─● 0. 뒤로가기'''

# 저격소총 판매 물품
strGunShopSniper = '''■ [판매 물품]
├─● 1. M40 (500$)
├─● 2. K14 (5000$)
├─● 3. M82 (20000$)
└─● 0. 뒤로가기'''

# 공격용 소모품 판매 물품
strGunShopConsumable = '''■ [판매 물품]
├─● 1. 수류탄 (100$)
├─● 2. 연막탄 (100$)
├─● 3. 소이 수류탄 (200$)
└─● 0. 뒤로가기'''

# 탄약 구매 출력문
strGunShopAmmo = "[SYSTEM] 구매하고 싶은 탄약의 갯수를 입력해주세요. 구매를 원하지 않으면 '0' 을 입력해주세요."
strGunShopExit = "[SYSTEM] 총포상을 나갑니다."

# 약국 관련 문자열
# 전체 판매 물품
strPharmacyAll = '''■ [판매 물품]
├─● 1. 붕대 (10$)
├─● 2. 진통제 (100$)
├─● 3. 의료키트 (500$)
├─● 4. 전투 자극제 (500$)
└─● 0. 나가기'''

strPharmacyExit = "[SYSTEM] 약국을 나갑니다."

# 터미널 관련 문자열
strTerminalLocationNone = "[SYSTEM] 이동 가능한 경로가 존재하지 않습니다."

# 스텟 상승 출력문
strSetStat = '''■ [증가시킬 수 있는 스텟]
├─● 1. 공격력 (1AP당 플레이어 기본 공격력 1% 증가)
├─● 2. 방어력 (1AP당 플레이어 기본 방어력 1% 증가)
├─● 3. 민첩성 (1AP당 플레이어 기본 민첩성 1% 증가)
├─● 4. 정확도 (1AP당 플레이어 기본 정확도 0.5% 증가)
├─● 5. 체력 (1AP당 플레이어 기본 체력 1% 증가)
├─● 6. 스태미나 (1AP당 플레이어 기본 스태미나 1% 증가)
└─● 0. 취소'''

# 총포상 출력문 리스트
listStrGunShopAllGoods = [strGunShopPistol, strGunShopRifle, strGunShopShotGun, strGunShopSniper, strGunShopConsumable]

# 스토리 관련 출력문
# 프롤로그 출력문
strPrologueStory = '''
 [프롤로그]
 203X 년 저녁.
 그 여느 때와 같이 평화롭던 지구 상공에 정체불명의 우주선이 갑작스럽게 등장하게 된다.
 인류가 대책을 세울 틈도 없이 우주선에서 밝은 빛이 뿜어져 나오게 되고, 그 빛을 따라 외계 우주선들이 튀어나오게 된다.
 외계인들은 놀라 도망치는 인간들을 공격하기 시작하였고, 인류는 속수무책으로 당하기 시작하며, 주요 도시들이 함락되기에 이른다.
 하지만, 그 와중에 인류는 끝까지 항전하며 일부 우주선들을 파괴하였고, 특수한 약품이 들은 우주선 한 대를 나포하게 되었다.
 인류는 이 우주선을 수색하게 되고, 우주선의 화물칸 속에는 미지의 약품이 들어있었다.
 해당 약품들을 획득한 정부는 소수의 인간을 데려와 인체실험을 벌이게 되고, 해당 약품을 인간 동맥에 투약하면, 강력한 신체 능력을 갖출 수 있음을 알아내게 된다.
 이에 정부는 이러한 인간들에게 ‘에이전트’라는 이름을 붙이고, 이들을 불러 모아 외계인들과 대적할 군대를 양성하기 시작하였다.
 또한, 해당 약품을 제작해내기 위해 정부는 비밀리에 연구를 시작하게 된다.'''

strMainStory1 = "[???] 어이 신병! 거기서 꾸물대며 뭘 하고 있나! 얼른 배낭 챙기고 부트 캠프로 튀어오게!"

# 게임 설명 관련 출력문
# 홈타운 이동 관련 출력문
strSystemHelpHomeTown1 = "[SYSTEM] 현재 에이전트가 있는 곳은 게임 내에서 마을과도 같은 역할을 하는 '홈타운' 입니다."
strSystemHelpHomeTown2 = "[SYSTEM] 1 ~ 5의 숫자를 입력하여 다양한 공간으로 이동할 수 있으며, 다양한 단축키들을 입력해 캐릭터의 정보들을 확인해볼 수 있습니다."
strSystemHelpHomeTown3 = "[SYSTEM] 일단은, NPC가 시키는 대로 '3'을 입력하여 '부트 캠프'로 이동하여보시길 바랍니다."
# 홈타운 이동 관련 출력문 리스트
listStrSystemHelpHomeTown = [strSystemHelpHomeTown1, strSystemHelpHomeTown2, strSystemHelpHomeTown3]

# 사이트 행동 출력문
strSiteAll = '''■ [가능한 행동]
├─● 1. 탐색하기
├─● 2. 상호작용
├─● 3. 아이템 사용
└─● 4. 탈출하기'''

# 전투 행동 출력문
strFightAll = '''■ [가능한 행동]
├─● 1. 일반 공격
├─● 2. 스킬 사용
├─● 3. 아이템 사용
└─● 4. 퇴각 하기'''

# 퀘스트 관련 출력문

# 메인 퀘스트 딕셔너리
dictQuestMain1 = {"이름" : "훈련 교관과의 첫 조우", "퀘스트 수주 NPC" : "훈련교관 A", "퀘스트 진행 단계" : 1, "퀘스트 보상" : {"경험치" : 0, "달러" : 0, "아이템" : {"탄약" : 30, "무기" : dictWeaponPistolUSP, "방어구" : "null", "고유 아이템" : "null"}, "스킬" : "null"}}
dictQuestMain2 = {"이름" : "훈련용 더미봇 처치하기", "퀘스트 수주 NPC" : "훈련교관 A", "퀘스트 진행 단계" : 1, "퀘스트 보상" : {"경험치" : 10, "달러" : 10, "아이템" : {"탄약" : 10, "무기" : "null", "방어구" : "null", "고유 아이템" : "null"}, "스킬" : "null"}}
dictQuestMain3 = {"이름" : "첫 임무", "퀘스트 수주 NPC" : "훈련교관 A", "퀘스트 진행 단계" : 1, "퀘스트 보상" : {"경험치" : 75, "달러" : 50, "아이템" : {"탄약" : 15, "무기" : "null", "방어구" : "null", "고유 아이템" : "null"}, "스킬" : "null"}}

# 서브 퀘스트 딕셔너리
dictQuestSub1 = {"이름" : "누락된 지원 물품", "퀘스트 수주 NPC" : "행정 보급관", "퀘스트 진행 단계" : 1, "퀘스트 보상" : {"경험치" : 10, "달러" : 20, "아이템" : "null"}, "스킬" : "null"}

# 모든 메인 퀘스트 리스트
listQuestAllMain = []

# 모든 서브 퀘스트 리스트
listQuestAllSub = []

playerSiteInfo = {"플레이어 이름" : playerName, "장비 모음" : dictPlayerEquip, "스텟 모음" : dictPlayerStat, "아이템 모음" : listPlayerItemSpace, "레벨 모음" : dictPlayerLv, "달러" : playerDollar}

# 연결 리스트 변수들
listPageMain = ["mainPage", ""]
listPageInGame = ["P", ""]

# 연결 딕셔너리 변수들
dictPageAll = ["mainPage", "characterGeneration", "prologue", "inGame"]

###################################################################### 함수 파트 ######################################################################

# 명령어 입력 함수
def cmdInputFunc(page):
    # 전역변수 선언
    # 문자열 전역변수
    global strError, strFatalError, timeDelay

    cmdInput = input("입력: ")

    if(page == "characterGeneration"):
        pass

    else:
        cmdInput = cmdInput.upper()
    
    funcLogic, page = cmdJudgFunc(cmdInput, page)

    if(funcLogic == 0):
        return page

    elif(funcLogic == 1):
        strSeqOutputFunc(strError, timeDelay)
        return page
    
    else:
        print(strFatalError)
        sys.exit()

# 명령어 판단 함수
def cmdJudgFunc(cmdInput, page):
    # 전역변수 선언
    # 기본 변수
    global playerName
    global dictPlayerStat
    global dictPlayerStatAP
    global dictPlayerPoint
    global dictPlayerLv
    global dictPlayerEquip
    global listPlayerItemSpace
    global listPlayerSkillSpace
    global advPage
    global playerDollar

    # 문자열 변수
    global strDummy, timeDelay

    # 메인 페이지 판단
    if(page == "mainPage"):
        if(succInputJudgFunc(cmdInput) == True):
            cmdInput = int(cmdInput)
            if(cmdInput == 1):
                page = "characterGeneration"
                funcLogic = 0
            
            elif(cmdInput == 2):
                page = "mainPage"
                strSeqOutputFunc(strDummy, timeDelay)
                funcLogic = 1
            
            elif(cmdInput == 0):
                strSeqOutputFunc(strProgramExit, timeDelay)
                sys.exit()
            
            else:
                page = "mainPage"
                funcLogic = 1
        
        # 예외 처리 (비정상 반환)
        else:
            page = "mainPage"
            funcLogic = 1
        
        return funcLogic, page

    # 캐릭터 생성 페이지 판단
    elif(page == "characterGeneration"):
        if((len(cmdInput) > 0) and (len(cmdInput) < 13)):
            playerName = cmdInput
            strSeqOutputFunc("[SYSTEM] 앞으로 여정을 함께 진행할 에이전트의 이름은 '%s' 입니다." % playerName, timeDelay)

            page = "prologue"
            funcLogic = 0

        # 예외 처리 (비정상 반환)
        else:
            page = "characterGeneration"
            funcLogic = 1

        return funcLogic, page

    # 프롤로그 페이지 판단
    elif(page == "prologue"):
        # 응답이 Y 일 때
        if(cmdInput == "Y"):
            strSeqOutputFunc(strPrologueStory, timeDelay)

            page = "inGame"
            funcLogic = 0

        # 응답이 N 일 때
        elif(cmdInput == "N"):
            page = "inGame"
            funcLogic = 0

        # 예외 처리 (비정상 반환)
        else:
            page = "prologue"
            funcLogic = 1
        
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

                        strOutputFunc(strGunShopAll)

                        page = "gunShop"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page
                    
                    # 권총 구매 나가기
                    elif(cmdInput == "0"):
                        strOutputFunc(strGunShopAll)

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

                        strOutputFunc(strGunShopAll)

                        page = "gunShop"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page
                    
                    # 돌격소총 구매 나가기
                    elif(cmdInput == "0"):
                        strOutputFunc(strGunShopAll)

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

                        strOutputFunc(strGunShopAll)

                        page = "gunShop"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page
                    
                    # 산탄총 구매 나가기
                    elif(cmdInput == "0"):
                        strOutputFunc(strGunShopAll)

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

                        strOutputFunc(strGunShopAll)

                        page = "gunShop"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page
                        
                    
                    # 저격소총 구매 나가기
                    elif(cmdInput == "0"):
                        strOutputFunc(strGunShopAll)

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
                    strSeqOutputFunc(strDummy, timeDelay)

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

                        strOutputFunc(strGunShopAll)

                        page = "gunShop"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page
                
                    # 탄약 구매 나가기
                    elif(cmdInput == "0"):
                        strOutputFunc(strGunShopAll)

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
                    strSeqOutputFunc(strGunShopExit, timeDelay)

                    page = "inGame"
                    advPage = "homeTown"
                    funcLogic = 0
                    return funcLogic, page
                
                # 총포상 1~5번 선택
                elif(int(cmdInput) > 0 and int(cmdInput) < 6):
                    strOutputFunc(listStrGunShopAllGoods[int(cmdInput) - 1])

                    page = "gunShop"
                    advPage = listAdvPageGunShop[int(cmdInput) - 1]
                    funcLogic = 0
                    return funcLogic, page

                # 탄약 구매하기
                elif(cmdInput == "6"):
                    strSeqOutputFunc(strGunShopAmmo, timeDelay)

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
    
    # 약국 판단
    elif(page == "pharmacy"):
        if(cmdInput.isdigit() == True):
            if(float(cmdInput) == int(cmdInput)):
                # 약국 물품 구매하기
                if(advPage == "pharmacyBandage" or advPage == "pharmacyPainkiller" or advPage == "pharmacyMedicalKit" or advPage == "pharmacyStimulant"):
                    if(int(cmdInput) > 0):
                        pharmacySelect = listAdvPagePharmacy.index(advPage) + 1 # 구매 선택
                        pharmacyAmount = int(cmdInput) # 구매 갯수
                        playerDollar, listPlayerItemSpace = pharmacyFunc(pharmacySelect, pharmacyAmount, playerDollar, listPlayerItemSpace)

                        strOutputFunc(strPharmacyAll)

                        page = "pharmacy"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page
                    
                    elif(cmdInput == "0"):
                        strOutputFunc(strPharmacyAll)

                        page = "pharmacy"
                        advPage = "homeTown"
                        funcLogic = 0
                        return funcLogic, page
                    
                    # 예외 처리 (비정상 반환)
                    else:
                        page = "pharmacy"
                        funcLogic = 1
                        return funcLogic, page

                # 약국 나가기
                elif(cmdInput == "0"):
                    strSeqOutputFunc(strPharmacyExit, timeDelay)

                    page = "inGame"
                    advPage = "homeTown"
                    funcLogic = 0
                    return funcLogic, page
                
                # 약국 물품 구매하기
                elif(int(cmdInput) > 0 and int(cmdInput) < 5):
                    strSeqOutputFunc("[SYSTEM] 구매하고 싶은 %s의 갯수를 입력해주세요. 구매를 원하지 않으면 '0'을 입력해주세요." % listPharmacyShopAllGoods[int(cmdInput) - 1]["이름"], timeDelay)

                    page = "pharmacy"
                    advPage = listAdvPagePharmacy[int(cmdInput) - 1]
                    funcLogic = 0
                    return funcLogic, page

                # 예외 처리 (비정상 반환)
                else:
                    funcLogic = 1
                    page = "pharmacy"
                    return funcLogic, page

            # 예외 처리 (비정상 반환)
            else:
                funcLogic = 1
                page = "pharmacy"
                return funcLogic, page

        # 예외 처리 (비정상 반환)
        else:
            funcLogic = 1
            page = "pharmacy"
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

            funcLogic = 0
            return funcLogic, page
        
        # 장비창
        elif(cmdInput == "E"):
            print(strLine)
            equipSpaceFunc(dictPlayerEquip)
        
        # 스킬창
        elif(cmdInput == "K"):
            print(strLine)
            skillSpaceFunction(listPlayerSkillSpace)
            print(strLine)

        # 아이템창
        elif(cmdInput == "I"):
            print(strLine)
            itemSpaceFunction(listPlayerItemSpace, playerDollar)
        
        # 업적창
        elif(cmdInput == "A"):
            print(strLine)
            IllustratedGuideSpaceFunction()
            print(strLine)

        # 홈타운 판단
        elif(advPage == "homeTown"):
            # 게임 종료
            if(cmdInput == "0"):
                strSeqOutputFunc(strProgramExit, timeDelay)
                sys.exit()

            # 총포상 이동
            elif(cmdInput == "1"):
                strSeqOutputFunc("[SYSTEM] 총포상으로 이동합니다.", timeDelay)
                # 총포상 물품 출력
                strOutputFunc(strGunShopAll)

                page = "gunShop"
                funcLogic = 0
                return funcLogic, page
            
            # 약국 이동
            elif(cmdInput == "2"):
                strSeqOutputFunc("[SYSTEM] 약국으로 이동합니다.", timeDelay)
                # 약국 물품 출력
                strOutputFunc(strPharmacyAll)

                page = "pharmacy"
                funcLogic = 0
                return funcLogic, page
            
            # 부트 캠프 이동
            elif(cmdInput == "3"):
                strSeqOutputFunc("[SYSTEM] 부트 캠프로 이동합니다.", timeDelay)
                strSeqOutputFunc(strDummy, timeDelay)
            
            # 제작 공방 이동
            elif(cmdInput == "4"):
                strSeqOutputFunc("[SYSTEM] 제작 공방으로 이동합니다.", timeDelay)
                strSeqOutputFunc(strDummy, timeDelay)
            
            # 터미널 이동
            elif(cmdInput == "5"):
                strSeqOutputFunc("[SYSTEM] 터미널로 이동합니다.", timeDelay)
                if(not listPlayerTerminalPossibleLocation):
                    strSeqOutputFunc(strTerminalLocationNone, timeDelay)

                    page = "inGame"
                    funcLogic = 0
                    return funcLogic, page

                else:
                    print("\n■ [이동 가능한 경로]")

                    i = 0

                    while(i < len(listPlayerTerminalPossibleLocation)):
                        print("├─● %d. %s" % (i + 1, listPlayerTerminalPossibleLocation[i]["이름"]))
                        i += 1
                    print("└─● 0. 마을로 돌아가기")
                    print("\n" + strLine)

                    page = "terminal"
                    funcLogic = 0
                    return funcLogic, page
            
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

        # 에버뉴 파크 판단
        elif(advPage == "avenuePark"):
            global dictTerminalAvenuePark
            global situation
            global playerSiteInfo

            # 탐색하기
            if(cmdInput == "1" and situation == "null"):
                strSeqOutputFunc("[SYSTEM] 탐색 활동을 진행합니다.", timeDelay)
                situation = scoutFunc(situation)

                page = "inGame"
                advPage = "avenuePark"
            
            # 상호작용
            elif(cmdInput == "2" and situation == "null"):
                strSeqOutputFunc("[SYSTEM] 할 수 있는 행동이 없습니다.", timeDelay)

                page = "inGame"
                advPage = "avenuePark"

            # 아이템 사용
            elif(cmdInput == "3" and situation == "null"):
                strSeqOutputFunc(strDummy, timeDelay)
                
                page = "inGame"
                advPage = "avenuePark"
            
            # 탈출하기
            elif(cmdInput == "4" and situation == "null"):
                strSeqOutputFunc("[SYSTEM] 에버뉴 공원에서 탈출합니다.", timeDelay)
                
                page = "inGame"
                advPage = "homeTown"

                funcLogic = 0
                return funcLogic, page

            # 적과 조우
            if(situation == "fight" or situation == "doubleFight"):
                strSeqOutputFunc("[%s] 적과 조우하였다!" % playerName, timeDelay)

                fightFunc(dictTerminalAvenuePark["등장 몬스터"], playerSiteInfo, situation)

                strSeqOutputFunc("[SYSTEM] 전투가 종료되었습니다.", timeDelay)

                print(strLine + "\n")
                print(strSiteAll)
                print("\n" + strLine)

                page = "inGame"
                advPage = "avenuePark"
                situation = "null"
            
            # 아무 일 없음
            elif(situation == "noting"):
                strSeqOutputFunc("[%s] 아무것도 발견할 수 없었다." % playerName, timeDelay)

                print(strLine + "\n")
                print(strSiteAll)
                print("\n" + strLine)

                page = "inGame"
                advPage = "avenuePark"
                situation = "null"
            
            # 함정 밟음
            elif(situation == "trap"):
                strSeqOutputFunc("[%s] 함정을 밟았다!" % playerName, timeDelay)

                # 사이트 내 플레이어 체력을 전체 체력 스텟의 10% 만큼 감소
                playerSiteInfo["스텟 모음"]["체력"] -= dictPlayerStat["체력"] * 0.1

                print(strLine + "\n")
                print(strSiteAll)
                print("\n" + strLine)

                page = "inGame"
                advPage = "avenuePark"
                situation = "null"
            
            # 아이템 발견
            elif(situation == "lucky"):
                strSeqOutputFunc("[%s] 아이템을 발견하였다!" % playerName, timeDelay)

                print(strLine + "\n")
                print(strSiteAll)
                print("\n" + strLine)

                page = "inGame"
                advPage = "avenuePark"
                situation = "null"
            
            else:
                print(strLine + "\n")
                print(strSiteAll)
                print("\n" + strLine)

                funcLogic = 1
                page = "inGame"
                advPage = "avenuePark"
                return funcLogic, page
    
            # 정상 반환
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
            strOutputFunc(strSetStat)

            page = "setStat"
        
        # 응답이 N 일 떄
        elif(cmdInput == "N"):
            strSeqOutputFunc("[SYSTEM] 스텟 올리기를 취소합니다.", timeDelay)
            strSeqOutputFunc("[SYSTEM] 남은 AP: %d" % dictPlayerPoint["AP"], timeDelay)

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
        if(cmdInput.isdigit() == True):
            if(float(cmdInput) == int(cmdInput)):
                if(int(cmdInput) > 0 and int(cmdInput) < 7):
                    dictPlayerStatAP, dictPlayerPoint = setStatFunc(dictPlayerStatAP, dictPlayerPoint, cmdInput)
                
                elif(cmdInput == "0"):
                    strSeqOutputFunc("[SYSTEM] 스텟 올리기를 취소합니다.", timeDelay)
                    pass
                
                else:
                    funcLogic = 1
                    return funcLogic, page
            
            else:
                funcLogic = 1
                return funcLogic, page
        
        else:
            funcLogic = 1
            return funcLogic, page

        
        strSeqOutputFunc("[SYSTEM] 남은 AP: %d" % dictPlayerPoint["AP"], timeDelay)
        
        page = "inGame"
        funcLogic = 0
        return funcLogic, page
    
    # 터미널 판단
    elif(page == "terminal"):
        if(cmdInput.isdigit() == True):
            if(float(cmdInput) == int(cmdInput)):
                if(cmdInput == "1"):
                    strSeqOutputFunc("[SYSTEM] 에버뉴 공원으로 이동합니다.", timeDelay)
                    playerSiteInfo = {"플레이어 이름" : playerName, "장비 모음" : dictPlayerEquip, "스텟 모음" : dictPlayerStat, "아이템 모음" : listPlayerItemSpace, "레벨 모음" : dictPlayerLv, "달러" : playerDollar}

                    print(strLine + "\n")
                    print(strSiteAll)
                    print("\n" + strLine)

                    page = "inGame"
                    advPage = "avenuePark"
                    funcLogic = 0
                    return funcLogic, page
                
                elif(cmdInput == "0"):
                    strSeqOutputFunc("[SYSTEM] 마을로 돌아갑니다.", timeDelay)
                    page = "inGame"
                    advPage == "homeTown"
                    funcLogic = 0
                    return funcLogic, page

                else:
                    funcLogic = 1
                    return funcLogic, page

            else:
                funcLogic = 1
                return funcLogic, page

        else:
            funcLogic = 1
            return funcLogic, page

    # 예외 처리 (오류 발생)
    else:
        return -1, -1

# 스텟 상승 함수
def setStatFunc(dictPlayerStatAP, dictPlayerPoint, cmdInput):
    # 전역 변수 설정
    global listStrStatIncrease, listStrStats, timeDelay # 문자열 전역변수들

    print(strLine)

    if(int(cmdInput) > 0 and int(cmdInput) < 7):
        dictPlayerPoint["AP"] -= 1
        dictPlayerStatAP[listStrStatIncrease[int(cmdInput) - 1]] += 1

        strSeqOutputFunc("[SYSTEM] '%s' 스텟에 1만큼의 AP를 투자하였습니다." % listStrStats[int(cmdInput) - 1], timeDelay)
    
    else:
        print(strFatalError)
        return dictPlayerStatAP, dictPlayerPoint

    return dictPlayerStatAP, dictPlayerPoint

# 스텟창 함수
def statSpaceFunc(dictPlayerStat, dictPlayerPoint, page):
    global timeDelay

    print(strLine)
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
        strSeqOutputFunc(listStrStatJudg, timeDelay)

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
        print("● 무기를 착용중이지 않습니다.")

    else:
        print("● 착용중인 무기: %s" % dictPlayerEquip["무기"]["무기 이름"])
    
    print("\n[방어구]")
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
        print("● 착용중인 부츠: %s" % dictPlayerEquip["부츠"]["부츠 이름"])
    
    print("\n[탄약]")
    print("● 탄약 개수: %d" % dictPlayerEquip["탄약"])

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
    print(strPlayerOwnItem)
    if(not listPlayerItemSpace):
        print(strPlayerItemSpaceEmpty)
        
    else:
        j = 1
        for i in listPlayerItemSpace:
            print("● %i. %s" % (j, i["이름"]))
            j += 1
    
    print("\n[달러]")
    print("● 플레이어가 소유한 달러: %d$" % playerDollar)

# 도감창 함수
def IllustratedGuideSpaceFunction():
    123

# 문자열 순차 출력 함수
def strSeqOutputFunc(strs, timeDelay):
    global strLine
    global playerName

    print(strLine)
    if(type(strs) == str):
        if("[SYSTEM]" in strs):
            timeDelay = timeDelay * 1.35
            print("\n [SYSTEM]", end="")
            strs = strs[8:]
        
        elif("[???]" in strs):
            print("\n [???]", end="")
            strs = strs[5:]
        
        elif("[%s]" % playerName in strs):
            timeDelay = timeDelay * 1.35
            print("\n [%s]" % playerName, end="")
            strs = strs[2 + len(playerName):]

        for i in strs:
            print(i, end="", flush=True)
            if(i == "." or i == "!" or i == "?"):
                time.sleep(timeDelay * 15)
            
            elif(i == "," or i == "'" or i == "(" or i == ")"):
                time.sleep(timeDelay * 7.5)

            else:
                time.sleep(timeDelay)

    else:
        seq = 0
        for j in strs:
            if("[SYSTEM]" in j):
                timeDelay = delayCalculFunc(timeDelay, seq)
                print("\n [SYSTEM]", end="")
                j = j[8:]
                seq += 1
            
            elif("[???]" in j):
                print("\n [???]", end="")
                j = j[5:]

            for k in j:
                print(k, end="", flush=True)
                if(k == "." or k == "!" or k == "?"):
                    time.sleep(timeDelay * 15)
                
                elif(k == "," or k == "'" or k == "(" or k == ")"):
                    time.sleep(timeDelay * 7.5)

                else:
                    time.sleep(timeDelay)

    print("\n\n" + strLine)

    time.sleep(timeDelay * 7.5)

# 딜레이 계산 함수
def delayCalculFunc(timeDelay, seq):
    if(seq == 0):
        timeDelay = timeDelay * 1.35
        return timeDelay

    else:
        return timeDelay

# 문자열 일반 출력 함수
def strOutputFunc(strs):
    global strLine
    
    print(strLine + "\n")
    print(strs)
    print("\n" + strLine)

    time.sleep(timeDelay * 7.5)

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
    global listGunShopAllGoods, timeDelay

    if(gunShopSelect > 0 and gunShopSelect < 5):
        # 계산 부분
        gunShopUseDollar = listGunShopAllGoods[gunShopSelect - 1][gunShopAdvSelect - 1]["가격"] # 가격 책정
        if(playerDollar >= gunShopUseDollar):
            playerDollar -= gunShopUseDollar # 무기의 가격 만큼 플레이어 달러 차감
            dictPlayerEquip["무기"] = listGunShopAllGoods[gunShopSelect - 1][gunShopAdvSelect - 1]
            strSeqOutputFunc("[SYSTEM] %d 달러를 사용하여 %s %s(을)를 구매한 후 장착하였습니다." % (gunShopUseDollar, listGunShopAllGoods[gunShopSelect - 1][gunShopAdvSelect - 1]["분류"], listGunShopAllGoods[gunShopSelect - 1][gunShopAdvSelect - 1]["무기 이름"]), timeDelay)

            return playerDollar, dictPlayerEquip

        else:
            strSeqOutputFunc(strNoMoney, timeDelay)

            return playerDollar, dictPlayerEquip

    elif(gunShopSelect == 5):
        return playerDollar, dictPlayerEquip

    elif(gunShopSelect == 6):
        # 계산 부분
        gunShopUseDollar = gunShopAmount * 2 # 가격 책정
        if(playerDollar >= gunShopUseDollar):

            playerDollar -= gunShopUseDollar # 탄약 구매 갯수 만큼 플레이어의 달러 차감
            dictPlayerEquip["탄약"] += gunShopAmount # 플레이어 장비의 탄약 갯수 보충
            strSeqOutputFunc("[SYSTEM] 탄약 %d발을 %d$를 사용해 구매하였습니다." % (gunShopAmount, gunShopUseDollar), timeDelay)

            return playerDollar, dictPlayerEquip

        else:
            strSeqOutputFunc(strNoMoney, timeDelay)

            return playerDollar, dictPlayerEquip
    
    else:
        print("에러 발생")

        return playerDollar, dictPlayerEquip

# 약국 함수        
def pharmacyFunc(pharmacySelect, pharmacyAmount, playerDollar, listPlayerItemSpace):
    global listPharmacyShopAllGoods, timeDelay

    pharmacyUseDollar = listPharmacyShopAllGoods[pharmacySelect - 1]["가격"] * pharmacyAmount # 가격 책정

    if(playerDollar >= pharmacyUseDollar):
        playerDollar -= pharmacyUseDollar # 물품의 가격 만큼 플레이어의 달러 차감
        i = 0
        while(i < pharmacyAmount):
            listPlayerItemSpace.append((listPharmacyShopAllGoods[pharmacySelect - 1]))
            i += 1

        strSeqOutputFunc("[SYSTEM] %d$를 사용하여 %s %d개를 구매한 후 인벤토리에 보관하였습니다." % (pharmacyUseDollar, listPharmacyShopAllGoods[pharmacySelect - 1]["이름"], pharmacyAmount), timeDelay)

        return playerDollar, listPlayerItemSpace

    else:
        strSeqOutputFunc(strNoMoney, timeDelay)

        return playerDollar, listPlayerItemSpace

# 탐색 함수
def scoutFunc(situation):
    i = random.randint(1,100)
    # 45%의 확률로 적과 전투
    if(i <= 45):
        if(i <= 15):
            situation = "doubleFight"

        else:
            situation = "fight"
    
    # 25%의 확률로 아무 일도 일어나지 않음
    elif(i <= 70):
        situation = "noting"
    
    # 20%의 확률로 함정 밟음
    elif(i <= 90):
        situation = "trap"
    
    # 10%의 확률로 아이템 발견
    else:
        situation = "lucky"

    return situation

def fightFunc(listMonsterAll, playerSiteInfo, situation):
    global timeDelay

    listMonster = []

    # 전투 할 몬스터 선별
    # 1 vs 1 전투일 때
    if(situation == "fight"):
        listMonster.append(random.choice(listMonsterAll))
        strSeqOutputFunc("[SYSTEM] 적 %s(와)과 조우하였다!" % listMonster[0]["이름"], timeDelay)
    
    # 1 vs 2 전투일 때
    else:
        for i in range(0, 2, 1):
            listMonster.append(random.choice(listMonsterAll))
        
        strSeqOutputFunc("[SYSTEM] 적 %s, %s(와)과 조우하였다!" % (listMonster[0]["이름"], listMonster[1]["이름"]), timeDelay)

    # 무한 반복
    while True:
        # 플레이어 정보 불러오기
        playerSiteInfo = {"플레이어 이름" : playerName, "장비 모음" : dictPlayerEquip, "스텟 모음" : dictPlayerStat, "아이템 모음" : listPlayerItemSpace, "레벨 모음" : dictPlayerLv, "달러" : playerDollar}
        
        # 1 vs 1 전투일 때
        if(situation == "fight"):
            if(listMonster[0]["체력"] <= 0):
                listMonster.remove(listMonster[0])
                strSeqOutputFunc("[SYSTEM] %s를 처치하였다!" % listMonster[0]["이름"], timeDelay)
                
        
        # 1 vs 2 전투일 떄
        else:
            if(listMonster[len(listMonster) - 2]["체력"] <= 0):
                listMonster.remove(listMonster[len(listMonster) - 2])
                strSeqOutputFunc("[SYSTEM] %s를 처치하였다!" % listMonster[len(listMonster) - 2]["이름"], timeDelay)

            elif(listMonster[len(listMonster) - 1]["체력"] <= 0):
                listMonster.remove(listMonster[len(listMonster) - 1])
                strSeqOutputFunc("[SYSTEM] %s를 처치하였다!" % listMonster[len(listMonster) - 1]["이름"], timeDelay)
        
        # 전투할 상대가 없을때
        if(len(listMonster) == 0):
            if(situation == "fight"):
                strSeqOutputFunc("[SYSTEM] %s(와)과의 전투에서 승리하였다!" % listMonster[0]["이름"], timeDelay)
                break

            else:
                strSeqOutputFunc("[SYSTEM] %s(와)과 %s(와)과의 전투에서 승리하였다!" % (listMonster[0]["이름"], listMonster[1]["이름"]), timeDelay)
                break

        # 플레이어의 체력이 0 이하로 떨어졌을 때
        elif(playerSiteInfo["스텟 모음"]["체력"] <= 0):
            strSeqOutputFunc("[SYSTEM] 눈 앞이 깜깜해졌다.....", timeDelay)
            break

        # 전투시
        else:
            # 플레이어 턴
            strOutputFunc("상대의 체력: %d" % listMonster[0]["체력"])

            strOutputFunc(strFightAll) # 상호작용 출력


            cmdInput = input("입력: ") # 입력 받음

            if(cmdInput.isdigit() == True):
                if(float(cmdInput) == int(cmdInput)):
                    # 일반 공격
                    if(cmdInput == "1"):
                        strSeqOutputFunc("\n[SYSTEM] 공격할 상대를 고르세요.", timeDelay) # 상호작용 출력

                        print("\n[공격할 상대]")
                        for i in range(1, len(listMonster) + 1, 1):
                            print("%d. %s" % (i, listMonster[i - 1]["이름"]))
                        
                        print()
                        print(strLine)

                        cmdInput = input("입력: ") # 입력 받음

                        if(cmdInput.isdigit() == True):
                            if(float(cmdInput) == int(cmdInput)):
                                if(int(cmdInput) > 0 and int(cmdInput) <= len(listMonster)):
                                    strSeqOutputFunc("[SYSTEM] %s의 일반 공격!" % playerName, timeDelay)
                                    
                                    # 플레이어의 명중 확률 계산
                                    playerFightAcc = random.uniform(0, 100) # 0~100 사이의 실수 반환
                                    playerFightAcc = round(playerFightAcc, 2) # 소숫점 둘째 자리에서 반올림

                                    if((playerSiteInfo["스텟 모음"]["정확도"]) >= playerFightAcc):
                                        strSeqOutputFunc("[SYSTEM] %s의 공격이 빗나갔습니다!" % playerName, timeDelay)
                                    
                                    else:
                                        monsterFightFlee = random.uniform(0,100)
                                        monsterFightFlee = round(monsterFightFlee, 2)

                                        if(listMonster[int(cmdInput) - 1]["회피율"] >= monsterFightFlee):
                                            strSeqOutputFunc("[SYSTEM] %s이 %s의 공격을 피했습니다!" % (listMonster[int(cmdInput) - 1]["이름"], playerName), timeDelay)
                                        
                                        # 공격 맞춤
                                        else:
                                            # 플레이어 최종 데미지 불러옴
                                            attackDamage = playerSiteInfo["스텟 모음"]["데미지"]

                                            # 가능한 최대 최솟값
                                            attackDamageMin = attackDamage * 0.95
                                            attackDamageMax = attackDamage * 1.05

                                            # 두 발 공격
                                            if(playerSiteInfo["장비 모음"]["무기"]["분류"] == "산탄총"):
                                                # 최대, 최소 사잇값 선택
                                                123
                                            
                                            # 한 발 공격
                                            else:
                                                # 최대, 최소 사잇값 선택
                                                attackDamageChoice = random.uniform(attackDamageMin, attackDamageMax)
                                                
                                                # 최종 데미지 = 데미지 선택값 - 몬스터 방어력
                                                attackDamageFinal = int(attackDamageChoice) - listMonster[i - 1]["방어력"]
                                                
                                                # 만약 최종 데미지가 0 혹은 음수일 때
                                                if(attackDamageFinal <= 0):
                                                    # 데미지 1로 고정
                                                    attackDamageFinal = 1
                                                
                                                # 몬스터 체력 수정
                                                listMonster[int(cmdInput) - 1]["체력"] -= attackDamageFinal
                                                strSeqOutputFunc("[SYSTEM] %s에게 %d의 데미지를 입혔다!" % (listMonster[int(cmdInput) - 1]["이름"], attackDamageFinal),timeDelay)
                                else:
                                    strSeqOutputFunc(strError, timeDelay)
                            
                            else:
                                strSeqOutputFunc(strError, timeDelay)

                        else:
                            strSeqOutputFunc(strError, timeDelay)

                    # 스킬 공격
                    elif(cmdInput == "2"):
                        123
                    
                    # 아이템 사용
                    elif(cmdInput == "3"):
                        123
                    
                    # 퇴각 하기
                    elif(cmdInput == "4"):
                        playerFightFlee = random.uniform(1, 100)
                        playerFightFlee = round(playerFightFlee, 2)

                        if((playerSiteInfo["스텟 모음"]["후퇴확률"]) > playerFightFlee):
                            strSeqOutputFunc("[SYSTEM] 퇴각에 성공하였습니다!", timeDelay)

                            return 0
                        
                        else:
                            strSeqOutputFunc("[SYSTEM] 퇴각에 실패하였습니다!", timeDelay)
                    
                    else:
                        strSeqOutputFunc(strError, timeDelay)

                # 예외처리
                else:
                    strSeqOutputFunc(strError, timeDelay)

            # 예외처리
            else:
                strSeqOutputFunc(strError, timeDelay)

    return 0

# 정상 입력 판단 함수
def succInputJudgFunc(cmdInput):
    global timeDelay

    if(cmdInput.isdigit() == True):
        if(float(cmdInput) == int(cmdInput)):
            return True
        
        else:
            return False
    
    else:
        return False

###################################################################### 프로그램 실행 파트 ######################################################################

while True:
    # 메인 진행 부분
    if(page == "mainPage"):
        strOutputFunc(strMainPage)
        page = cmdInputFunc(page)

    # 캐릭터 생성 부분
    elif(page == "characterGeneration"):
        strSeqOutputFunc(strCharacterGeneration, timeDelay)
        page = cmdInputFunc(page)
    
    # 프롤로그 부분
    elif(page == "prologue"):
        strSeqOutputFunc(strPrologueJudg, timeDelay)
        page = cmdInputFunc(page)
    
    # 게임 진행 부분
    else:
        if(page == "inGame" and advPage == "homeTown"):
            if(gameProgress == 0):
                strSeqOutputFunc(strMainStory1, timeDelay)
                strSeqOutputFunc(listStrSystemHelpHomeTown, timeDelay)
            strOutputFunc(strHomeTownLocation)

        dictPlayerStat = statCalculFunc(dictPlayerBasicStat, dictPlayerStatAP, dictPlayerEquip)
        page = cmdInputFunc(page)
