def solution(s):
    answer = []
    for i, char in enumerate(s):
        if char not in s[:i]:
            answer.append(-1)
        else:
            answer.append(s[i-1::-1].index(char)+1)
    return answer

# ===================================
# 없는 경우 에러 대신 -1 반환
def solution(s):
    return [s[i::-1].find(s[i],1) for i in range(len(s))]

# ===================================
# 시간 복잡도 개선

def solution(s):
    answer = []
    last = {}

    for i, char in enumerate(s):
        if char in last:
            answer.append(i - last[char])
        else:
            answer.append(-1)
        last[char] = i

    return answer