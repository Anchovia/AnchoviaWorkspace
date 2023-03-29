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
    monitor = peripheral.wrap(monitorDirection)
    monitor.setCursorPos(1, 1)
    monitor.clear()

    return monitor -- return: monitor
end

-- 모니터 출력 함수
function writeMonitorDrawerDataFunc(dataTable, tempMemoryTable, monitor)
    -- 형식에 맞게 출력
    for index, item in pairs(dataTable) do
        -- cursor setting
        monitor.setCursorPos(1, (index - 1) * 2 + 1)

        local itemName = sliceModName(item) -- 아이템 이름 변환

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
        monitor.setTextColor(color)
        monitor.write(("%s%2d: %d x %s"):format(symbol, index, item.count, itemName))
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

        -- timer event
        repeat
            _, id = os.pullEvent("timer")
        until id == timerId
        -- 프로그램 작동부
        monitor = monitorInitFunc(MONITOR_DIRECTION) -- monitor init

        -- drawer 데이터 생성 및 출력부
        dataTable = makeDrawerDataFunc(DRAWER_MODEM_DIRECTION, DRAWER_MODEM_PORT)
        writeMonitorDrawerDataFunc(dataTable, tempMemoryTable, monitor)

        tempMemoryTable = dataTable -- dataTable을 tempMemoryTable에 저장
    end
end

-- main
main()

-- 테스트용 코드
--[[
    mn = monitorInitFunc(MONITOR_DIRECTION)
    mn.write(test)
]]--
