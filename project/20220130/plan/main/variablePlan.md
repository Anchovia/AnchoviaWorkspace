# 변수명 정리표

* ## 1. 기본 변수
    - ### 1. 시스템
      | 이름 | 변수명 | 타입 | 특이사항 |
      | :---: | :---: | :---: | :---: |
      | 명령어 입력 | cmdInput | `str` | |
      | 함수 로직 판단 | funcLogic | `int` | |
      | 오류문 출력 | strError | `str` | |
      | 게임 페이지 | page | `str` | `mainPage` : 게임 첫 화면,  `characterGeneration` : 캐릭터 생성, `prologue` : 프롤로그, `inGame` : 인게임 |
      | 프롤로그 스토리 | strPrologue | `str` | |
      | 문자열 | strs | `str` | 문자열 출력 함수에 사용 |
      | 지연시간 | timeDelay | `int` | 기본값: `0.045` |
      | 진행도 | progress | `int` | 메인 퀘스트 클리어 갯수 |

* ## 2. 플레이어 관련 변수
    - ### 1. 스텟 관련
        + #### 1. 기본 스텟 관련
          | 이름 | 변수명 | 타입 | 특이사항 |
          | :---: | :---: | :---: | :---: |
          | 플레이어 기본 공격력 | playerBasicAtk | `int` | |
          | 플레이어 기본 방어력 | playerBasicDef | `int` | |
          | 플레이어 기본 민첩성 | playerBasicAgi | `int` | |
          | 플레이어 기본 정확도 | playerBasicAcc | `int` | |
          | 플레이어 기본 체력 | playerBasicHP | `int` | |
          | 플레이어 기본 스태미나 | playerBasicStm | `int` | |
          | 플레이어 기본 스텟 관련 딕셔너리 | dictPlayerBasicStat | `dict` | |
          
        + #### 2. 기본 최종 스텟 관련
          | 이름 | 변수명 | 타입 | 특이사항 |
          | :---: | :---: | :---: | :---: |
          | 플레이어 최종 공격력 | playerTotalAtk | `int` | |
          | 플레이어 최종 방어력 | playerTotalDef | `int` | |
          | 플레이어 최종 민첩성 | playerTotalAgi | `int` | |
          | 플레이어 최종 정확도 | playerTotalAcc | `int` | |
          | 플레이어 최종 체력 | playerTotalHP | `int` | |
          | 플레이어 최종 스태미나 | playerTotalStm | `int` | |
          | 플레이어 최종 데미지 | playerTotalDmg | `int` | |
          | 플레이어 최종 회피율 | playerTotalAvd | `int` | |
          | 플레이어 최종 선공확률 | playerTotalFatk | `int` | |
          | 플레이어 최종 퇴각확률 | playerTotalFlee | `int` | |
          | 플레이어 최종 스텟 관련 딕셔너리 | dictPlayerStat | `
      
    - ### 2. 레벨 관련
      | 이름 | 변수명 | 타입 | 특이사항 |
      | :---: | :---: | :---: | :---: |
      | 플레이어 이름 | playerName | `str` | 1 ~ 12 글자 영문 (공백 없음) |
      | 플레이어 직업 | playerJob | `str` | 시작 직업: `견습생` |
    
    - ### 3. 기본 정보 관련
      | 이름 | 변수명 | 타입 | 특이사항 |
      | :---: | :---: | :---: | :---: |
      | 플레이어 레벨 | playerName | `int` | 초기값: `1` |
      | 플레이어 경험치 | playerExp | `int` | |
      | 필요 경험치 | reqExp | `int` | 초기값: `14` |
      | 플레이어 레벨 관련 딕셔너리 | dictPlayerLv | `dict` | |

* ## 3. 무기
    - ### 1. 권총
      | 이름 | 변수명 | 타입 |
      | :---: | :---: | :---: |
      | USP | dictWeaponPistolUSP | `dict` |
      | Glock-19 | dictyWeaponPistolGlock19 | `dict` |
      | M1911 | dictWeaponPistolM1911 | `dict` |
      | HK45 | dictWeaponPistolHK45 | `dict` |
    - ### 2. 돌격소총
      | 이름 | 변수명 | 타입 |
      | :---: | :---: | :---: |
      | M16A4 | dictWeaponRifleM16A4 | `dict` |
      | G36A3 | dictWeaponRifleG36A3 | `dict` |
      | HK416 | dictWeaponRifleHK416 | `dict` |
    - ### 3. 산탄총
      | 이름 | 변수명 | 타입 |
      | :---: | :---: | :---: |
      | Winchester M1897 | dictWeaponShotgunWinchesterM1897 | `dict` |
      | Remington 870 | dictWeaponShotgunRemington870 | `dict` |
      | Benelli M4 S90 Tectical	 | dictWeaponShotgunBenelliM4S90Tectical | `dict` |
