def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    num = 1
    row_start, row_end = 0, n - 1
    col_start, col_end = 0, n - 1
    
    while num <= n * n:
        # 왼쪽 -> 오른쪽 
        for i in range(col_start, col_end + 1):
            answer[row_start][i] = num
            num += 1
        row_start += 1
        
        # 위쪽 -> 아래쪽 
        for i in range(row_start, row_end + 1):
            answer[i][col_end] = num
            num += 1
        col_end -= 1
        
        # 오른쪽 -> 왼쪽 (하단 행 채우기)
        for i in range(col_end, col_start - 1, -1):
            answer[row_end][i] = num
            num += 1
        row_end -= 1
        
        # 아래쪽 -> 위쪽 (왼쪽 열 채우기)
        for i in range(row_end, row_start - 1, -1):
            answer[i][col_start] = num
            num += 1
        col_start += 1
            
    return answer
