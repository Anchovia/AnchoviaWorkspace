# 변수명 정리표

* ## 1. 기본 변수
    - ### 1. 시스템
      | 이름 | 변수명 | 타입 | 특이사항 |
      | :---: | :---: | :---: | :---: |
      | 명령어 입력 | commandInput | `str` | |
      | 함수 로직 판단 | functionLogic | `int` | |
      | 오류문 출력 | strError | `str` | |
      | 게임 페이지 | page | `str` | `mainPage` : 게임 첫 화면,  `characterGeneration` : 캐릭터 생성, `prologue` : 프롤로그, `inGame` : 인게임 |
      | 프롤로그 스토리 | strPrologue | `str` | |
      | 문자열 | strings | `str` | 문자열 출력 함수에 사용 |
      | 지연시간 | delayTime | `int` | 기본값: `0.07` |
      | 진행도 | progress | `int` | 메인 퀘스트 클리어 갯수 |

* ## 2. 플레이어 관련 변수
    - ### 1. 시스템
      | 이름 | 변수명 | 타입 | 특이사항 |
      | :---: | :---: | :---: | :---: |
      | 플레이어 이름 | playerName | `str` | 1 ~ 12 글자 영문 (공백 없음) |
      | 플레이어 직업 | playerJob | `str` | 시작 직업: `견습생` |
      | 플레이어 공격력 | playerAtk | `int` | |
      | 플레이어 방어력 | playerDef | `int` | |
      | 플레이어 민첩성 | playerAgi | `int` | |
      | 플레이어 정확도 | playerAcc | `int` | |
      | 플레이어 체력 | playerHp | `int` | |
      | 플레이어 스태미나 | playerStm | `int` | |
      | 플레이어 데미지 | playerDmg | `int` | |
      | 플레이어 회피율 | playerAvd | `int` | |
      | 플레이어 선공확률 | playerFatk | `int` | |
      | 플레이어 퇴각확률 | playerFlee | `int` | |
      | 플레이어 스텟 | dictionaryPlayerStatus | `dict` | |

* ## 3. 무기
    - ### 1. 권총
      | 이름 | 변수명 | 타입 |
      | :---: | :---: | :---: |
      | USP | dictionaryWeaponPistolUSP | `dict` |
      | Glock-19 | dictionaryWeaponPistolGloack19 | `dict` |
      | M1911 | dictionaryWeaponPistolM1911 | `dict` |
      | HK45 | dictionaryWeaponPistolHK45 | `dict` |
    - ### 2. 돌격소총
      | 이름 | 변수명 | 타입 |
      | :---: | :---: | :---: |
      | M16A4 | dictionaryWeaponRifleM16A4 | `dict` |
      | G36A3 | dictionaryWeaponRifleG36A3 | `dict` |
      | HK416 | dictionaryWeaponRifleHK416 | `dict` |
    - ### 3. 산탄총
      | 이름 | 변수명 | 타입 |
      | :---: | :---: | :---: |
      | Winchester M1897 | dictionaryWeaponShotgunWinchesterM1897 | `dict` |
      | Remington 870 | dictionaryWeaponShotgunRemington870 | `dict` |
      | Benelli M4 S90 Tectical	 | dictionaryWeaponShotgunBenelliM4S90Tectical | `dict` |
