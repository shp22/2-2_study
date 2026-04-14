def ms(time)
    return int(time[2])60 + int(time[3])

def solution(video_len, pos, op_start, op_end, commands)
    temp = ms(pos)
    end = ms(video_len)
    ops = ms(op_start)
    ope = ms(op_end)

    for c in commands
        if ops = temp = ope
            temp = ope
            
        if c == next 
            temp += 10
            if temp  end temp = end
        else 
            temp -= 10
            if temp  0 temp = 0
            
    if ops = temp = ope
            temp = ope
    
    return f{temp6002d}{temp%6002d}