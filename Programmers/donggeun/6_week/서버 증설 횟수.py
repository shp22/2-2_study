def solution(players, m, k):
    answer = 0
    active_servers = [0] * 24
    
    for i in range(24):
        required = players[i] // m
        
        if required > active_servers[i]:
            add_cnt = required - active_servers[i]
            answer += add_cnt
            
            for j in range(i, min(24, i + k)):
                active_servers[j] += add_cnt
                
    return answer