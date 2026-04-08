def solution(mats, park):
    mats.sort(reverse=True)
    
    for mat in mats:

        for y in range(len(park)):
            if len(park) - y < mat:
                continue
                
            for x in range(len(park[0])):
                if len(park[0]) - x < mat:
                    continue
                cy, cx = y, x

                state = True
                for n in range(mat**2):
                    if park[cy][cx] != '-1':
                        state = False
                        break
                        
                    cy = y + n % mat
                    cx = x + n // mat
                    
                if state == True:
                    return mat

    return -1