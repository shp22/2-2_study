def solution(schedules, timelogs, startday):
    # 출근 희망시간 schedules -> 리스트
    # 출근한 시각 timelog -> 2차원 리스트
    # 이벤트 시작한 요일 startday - > 정수형 변수
    
    # 출근 희망 시각 + 10분까지 인정
    # startday부터 일주일 동안 인정 되면 상품 
    # 토, 일 출근 시각은 이벤트에 영향 X
    # 상품 받는 총인원수 체크
    answer = 0
    
    for i in range(len(schedules)):

        # 인정 가능 시간
        plan = schedules[i]
        hour = plan//100
        minute = plan % 100 + 10
        
        if minute >= 60:
            hour += 1
            minute -= 60
        
        limit_time = hour * 100 + minute
        
        is_winner = True
        for j in range(7):
            current_day = (j + startday) % 7
            
            if current_day == 6 or current_day == 0:
                continue
                
            if timelogs[i][j] > limit_time:
                is_winner = False
                break
        
        if is_winner:
            answer+=1
    
    return answer
