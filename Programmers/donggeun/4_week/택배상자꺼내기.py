def solution(n, w, num):
    # 0-based index로 변환
    target = num - 1
    
    # 타겟 상자의 행 계산
    target_row = target // w
    
    # 타겟 상자의 열 계산 (지그재그 규칙)
    if target_row % 2 == 0:
        target_col = target % w
    else:
        target_col = (w - 1) - (target % w)
        
    # 상자가 쌓인 가장 높은 층 계산
    top_row = (n - 1) // w
    
    # 최고 층에서 타겟 상자와 같은 열에 있는 상자의 인덱스 계산
    if top_row % 2 == 0:
        top_box_idx = top_row * w + target_col
    else:
        top_box_idx = top_row * w + (w - 1 - target_col)
        
    # 해당 위치에 실제로 상자가 존재하는지 확인
    if top_box_idx < n:
        return top_row - target_row + 1
    else:
        return top_row - target_row