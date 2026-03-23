import math

def solution(signals):
    # 1. 각 신호등의 주기와 노란불 구간 미리 계산
    light_info = []
    periods = []
    
    for g, y, r in signals:
        total_period = g + y + r
        periods.append(total_period)
        # 노란불 시작 시각(초)과 끝 시각(초) 저장
        # t초일 때, g < (t % total_period) <= g + y 이면 노란불 (단, % 결과가 0인 경우 예외처리 필요)
        light_info.append((g, g + y, total_period))

    # 2. 탐색 범위 설정 (모든 주기의 최소공배수)
    # 파이썬 3.9 이상은 math.lcm(*periods) 가능, 이하는 직접 구현
    def get_lcm(a, b):
        return abs(a * b) // math.gcd(a, b)
    
    current_lcm = periods[0]
    for p in periods[1:]:
        current_lcm = get_lcm(current_lcm, p)
        # 만약 LCM이 너무 커지면 현실적인 제한(예: 1,000,000)을 두거나 
        # 문제의 제약사항에 따라 조절해야 합니다.
        if current_lcm > 1000000: # 예시 제한값
            current_lcm = 1000000
            break

    # 3. 1초부터 LCM까지 시뮬레이션
    for t in range(1, current_lcm + 1):
        all_yellow = True
        for g_end, y_end, p in light_info:
            remain = t % p
            if remain == 0: remain = p # 0초는 주기의 마지막 초와 같음
            
            # 노란불 구간에 있는지 확인
            if not (g_end < remain <= y_end):
                all_yellow = False
                break
        
        if all_yellow:
            return t
            
    return -1