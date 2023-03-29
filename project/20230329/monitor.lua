-- https://tweaked.cc/

MONITOR_DIRECTION = "right" -- monitor direction
DRAWER_MODEM_DIRECTION = "left" -- drawer modem direction
DRAWER_MODEM_PORT = 1 -- drawer modem port
TIMER_SET_TIME = 10 -- set refresh seconds

-- : 이전에 있는 문자열을 제거하는 함수
function sliceModName(str)
    return string.match(str.name, ":(.+)$") or str.name
end

-- 모니터 초기화 함수
function monitorInitFunc(monitorDirection)
    -- variable init
    local monitorSize = {
        width = 0,
        height = 0
    }

    -- monitor init
    monitor = peripheral.wrap(monitorDirection)

    -- 모니터 초기화
    monitorSize["width"], monitorSize["height"] = monitor.getSize()
    monitor.setCursorPos(1, 1)
    monitor.clear()

    return monitor, monitorSize -- return: monitor, monitorSize
end

-- 모니터 출력 함수
function writeMonitorDrawerDataFunc(dataTable, tempMemoryTable, monitor, monitorSize)
    for index, item in pairs(dataTable) do
        -- tempMemoryTable에 새로운 아이템이 추가된 경우 처리
        local tempItem = tempMemoryTable[index]

        if not tempItem then
            tempMemoryTable[index] = {name = item.name, count = 0}
            tempItem = tempMemoryTable[index]
        end

        -- 아이템 이름 변환
        local itemName = sliceModName(item)

        -- 색깔 및 심볼 판단부
        local color, symbol
        local diff = item.count - tempMemoryTable[index].count

        if diff > 0 then
            color, symbol = colors.red, '+'
        elseif diff < 0 then
            color, symbol = colors.blue, '-'
        else
            color, symbol = colors.white, '='
        end

        -- 출력부
        monitor.setCursorPos(2, (index - 1) * 2 + 1) -- cursor setting
        monitor.setTextColor(color) -- color setting

        local maxLen = monitorSize.width - 8 -- 출력할 수 있는 최대 길이
        local str = ("%s %d x %s"):format(symbol, item.count, itemName) -- 출력할 문자열
        if #str > maxLen then -- 출력할 문자열이 최대 길이보다 길다면
            str = string.sub(str, 1, maxLen - 3) .. "..." -- 이전 3글자를 ...으로 대체
        end
        monitor.write(str) -- 수정된 문자열을 출력

        -- 뒤 쪽 증감량 출력
        monitor.setCursorPos(monitorSize.width - 5, (index - 1) * 2 + 1)
        monitor.write(("%s%4d"):format(symbol, math.abs(diff)))
    end
end

-- 서랍 데이터 생성 함수
function makeDrawerDataFunc(modemDirection, port)
    -- variable init
    local dataTable = {}

    -- modem init
    local modem = peripheral.wrap(modemDirection)
    modem.open(port)

    -- drawer 블럭 테이블 정보를 찾아오기 위한 코드
    local drawerInitTable = modem.getNamesRemote()

    -- 테이블 내용을 key와 name으로 각각 분리해 이용
    for _, name in pairs(drawerInitTable) do
        local data = modem.callRemote(name, "list")

        -- 데이터 테이블에 데이터 추가 작업
        for _, rawName in pairs(data) do
            if rawName then
                table.insert(dataTable, rawName)
            end
        end
    end

    return dataTable -- return: drawer data table
end

-- 메인함수
function main()
    -- 처음 실행시에는 tempMemoryTable을 생성
    local tempMemoryTable = makeDrawerDataFunc(DRAWER_MODEM_DIRECTION, DRAWER_MODEM_PORT)

    while true do
        -- timer init
        local timerId = os.startTimer(TIMER_SET_TIME)
        local id

        -- variable init
        local dataTable
        local monitor
        local monitorSize

        -- timer event
        repeat
            _, id = os.pullEvent("timer")
        until id == timerId
        -- 프로그램 작동부
        monitor, monitorSize = monitorInitFunc(MONITOR_DIRECTION) -- monitor init

        -- drawer 데이터 생성 및 출력부
        dataTable = makeDrawerDataFunc(DRAWER_MODEM_DIRECTION, DRAWER_MODEM_PORT)
        writeMonitorDrawerDataFunc(dataTable, tempMemoryTable, monitor, monitorSize)

        tempMemoryTable = dataTable -- dataTable을 tempMemoryTable에 저장
    end
end

-- main
main()
