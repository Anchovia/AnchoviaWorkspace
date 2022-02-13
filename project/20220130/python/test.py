import math

strLine = "============================================================================================================================================================="

playerName = "Carol"
playerSiteInfo = {"스텟 모음" : {"체력" : 100, "스태미나" :50}}
monster1 = {"이름" : "소형외계전투드론", "체력" : 60}
monster2 = {"이름" : "외계전투로봇", "체력" : 1500}
listMonster = [monster1, monster2]


# hpPrimePlayer = playerSiteInfo["스텟 모음"]["체력"]
# hpPrimeMonster1 = listMonster[0]["체력"]
# hpPrimeMonster2 = listMonster[1]["체력"]

hpPrimePlayer = 100
stmPrimePlayer = 50
hpPrimeMonster1 = 100
hpPrimeMonster2 = 1500

def healthBarOutputFunc(playerName, listMonster, playerSiteInfo):
    # 이름 문자열 길이 변수
    wordLenPlayer = 0
    wordLenMonster1 = 0
    wordLenMonster2 = 0

    hpSqrPlayer = 0
    hpSqrMonster1 = 0
    hpSqrMonster2 = 0

    hpSqrPlayer = playerSiteInfo["스텟 모음"]["체력"] / (hpPrimePlayer / 10)
    hpSqrMonster1 = listMonster[0]["체력"] / (hpPrimeMonster1 / 10)
    hpSqrMonster2 = listMonster[1]["체력"] / (hpPrimeMonster2 / 10)
    StmSqrPlayer = playerSiteInfo["스텟 모음"]["스태미나"] / (stmPrimePlayer / 10)

    hpSqrPlayer = int(hpSqrPlayer)
    hpSqrMonster1 = int(hpSqrMonster1)
    hpSqrMonster2 = int(hpSqrMonster2)
    StmSqrPlayer = int(StmSqrPlayer)

    for i in playerName:
        if(i.encode().isalpha() == True):
            wordLenPlayer += 1
        else:
            wordLenPlayer += 2
    
    for j in listMonster[0]["이름"]:
        if(j.encode().isalpha() == True):
            wordLenMonster1 += 1
        else:
            wordLenMonster1 += 2
    
    for k in listMonster[1]["이름"]:
        if(j.encode().isalpha() == True):
            wordLenMonster2 += 1
        else:
            wordLenMonster2 += 2
    
    print("\n" + strLine)
    print()

    # 1줄
    print("┌─[전투 상황]───────────────────────────────────┐")

    # 2줄
    print("│ ● %s" % playerName, end = "")
    for i in range(wordLenPlayer, 19, 1):
        print(" ", end = "")
    print(" ║ ○", end = "")
    print(" %s" % listMonster[0]["이름"], end = "")
    for i in range(wordLenMonster1, 19, 1):
        print(" ", end = "")
    print(" │")

    #3줄
    print("│ HP(%5d): " % playerSiteInfo["스텟 모음"]["체력"], end = "")
    print("■" * hpSqrPlayer, end = "")
    print("□" * (10 - hpSqrPlayer), end = "")
    print(" ║ ", end = "")
    print("HP(%5d): " % listMonster[0]["체력"], end = "")
    print("■" * hpSqrMonster1, end = "")
    print("□" * (10 - hpSqrMonster1), end = "")
    print(" │")

    # 4줄
    print("│ ST(%5d): " % playerSiteInfo["스텟 모음"]["스태미나"], end = "")
    print("■" * StmSqrPlayer, end = "")
    print("□" * (10 - StmSqrPlayer), end = "")
    print(" ║ ○", end = "")
    print(" %s" % listMonster[1]["이름"], end = "")
    for i in range(wordLenMonster2, 19, 1):
        print(" ", end = "")
    print(" │")

    # 5줄
    print("│ ", end = "")
    print(" " * 21, end = "")
    print(" ║ ", end = "")
    print("HP(%5d): " % listMonster[1]["체력"], end = "")
    print("■" * hpSqrMonster2, end = "")
    print("□" * (10 - hpSqrMonster2), end = "")
    print(" │")
    
    # 6줄
    print("└───────────────────────────────────────────────┘")

    print("\n" + strLine)

    return 0

healthBarOutputFunc(playerName, listMonster, playerSiteInfo)
