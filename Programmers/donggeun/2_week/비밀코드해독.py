# 1~n 까지의 숫자
# q 입력한 정수를 담은 2차원 정수 배열
# ans 시스템의 응답 1차원 정수 배열

from itertools import combinations

def solution(n, q, ans):
    answer = 0
    # 1. 1부터 n까지의 숫자 중 5개를 뽑는 모든 조합 생성
    all_cases = list(combinations(range(1, n + 1), 5))
    
    # 각 질문(q)의 리스트를 집합(set)으로 미리 변환하여 연산 속도 향상
    query_sets = [set(query) for query in q]
    
    # 2. 모든 후보 조합을 하나씩 검사
    for case in all_cases:
        case_set = set(case)
        is_possible = True
        
        # 3. 해당 후보가 모든 질문의 응답(ans)과 일치하는지 확인
        for i in range(len(q)):
            # 교집합의 개수가 시스템의 응답과 같아야 함
            if len(case_set & query_sets[i]) != ans[i]:
                is_possible = False
                break
        
        # 모든 조건을 만족하면 가능한 조합으로 판단
        if is_possible:
            answer += 1
            
    return answer