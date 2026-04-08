def solution(n):
    answer = [[0]*n for _ in range(n)]
    num = 1
    r, c = 0, 0
    for i in range(n-1, 0, -2):
        for j in range(4):            
            if j == 0:
                for _ in range(i):
                    answer[r][c] = num 
                    c += 1; num += 1
                    
            elif j == 1:
                for _ in range(i):
                    answer[r][c] = num 
                    r += 1; num += 1
                    
            elif j == 2:
                for _ in range(i):
                    answer[r][c] = num 
                    c -= 1; num += 1
                    
            else:
                for _ in range(i):
                    answer[r][c] = num 
                    r -= 1; num += 1
                    
                c += 1
                r += 1
                if n % 2 == 1 and i == 2:
                    answer[r][c] = num
    if n == 1:
        answer = [[1]]
    return answer

# ============================
# 다른 풀이 방법

def solution(n):
    answer = [[None for j in range(n)] for i in range(n)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x, y, m = 0, 0, 0
    for i in range(1, n**2 + 1):
        answer[y][x] = i
        if y + move[m][0] >= n or x + move[m][1] >= n or answer[y + move[m][0]][x + move[m][1]]:
            m = (m + 1) % len(move)
        y, x = y + move[m][0], x + move[m][1]
    return answer

# 나선형 회전 -> move = [[0, 1], [1, 0], [0, -1], [-1, 0]] 과 같은 방향 벡터 사용 시 코드 반복 축약 가능