def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    num = 1
    row_start, row_end = 0, n - 1
    col_start, col_end = 0, n - 1
    
