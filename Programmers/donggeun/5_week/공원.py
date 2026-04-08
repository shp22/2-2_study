def solution(mats, park):
    mats.sort(reverse=True)
    
    H = len(park)    # 공원의 세로
    W = len(park[0]) 

    for size in mats:
        for i in range(H - size + 1):
            for j in range(W - size + 1):
                
                is_possible = True
                for r in range(i, i + size):
                    for c in range(j, j + size):
                        if park[r][c] != "-1":
                            is_possible = False 
                            break
                    if not is_possible: break

                if is_possible:
                    return size
    
    return -1