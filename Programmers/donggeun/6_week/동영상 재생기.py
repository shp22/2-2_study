def solution(video_len, pos, op_start, op_end, commands):
    def to_sec(time_str):
        m, s = map(int, time_str.split(':'))
        return m * 60 + s
    
    V, P, S, E = to_sec(video_len), to_sec(pos), to_sec(op_start), to_sec(op_end)
    
    if S <= P <= E: P = E
        
    for cmd in commands:
        if cmd == "prev":
            P = max(0, P - 10) # 0초 밑으로 안 내려가게 방어
        else:
            P = min(V, P + 10) # 영상 길이 밖으로 안 나가게 방어
            
        if S <= P <= E: P = E
            
    return f"{P//60:02d}:{P%60:02d}"