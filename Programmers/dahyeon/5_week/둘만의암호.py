def solution(s, skip, index):
    alpha = [chr(i) for i in range(ord('a'), ord('z') + 1) 
                if chr(i) not in skip]
    
    answer = []
    for c in s:
        pos = alpha.index(c)
        new_pos = (pos + index) % len(alpha)
        answer.append(alpha[new_pos])
    
    return ''.join(answer)