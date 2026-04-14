def solution(wallet, bill):
    answer = 0
    wmin, wmax = min(wallet), max(wallet)
    bmin, bmax = min(bill), max(bill)
    
    while bmin>wmin or bmax>wmax:
        bmax = bmax//2
        answer += 1
        bmin, bmax = min([bmin, bmax]), max([bmin, bmax])
        
    return answer