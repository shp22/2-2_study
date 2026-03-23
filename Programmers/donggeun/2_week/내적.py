import numpy as np

def solution(a, b):

    return int(np.dot(a,b))




# 리스트 컴프리헨션 사용
def solution(a, b):

    return sum([x*y for x, y in zip(a,b)])

# for문 사용
def solution(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return sum(c)
