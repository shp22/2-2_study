def solution(n, w, num):
    moves = [[0,1], [-1,0], [0,-1], [-1,0]]
    rows = n//w+1
    boxes = [[None]*w for _ in range(rows)]
    x, y, m = 0, rows-1, -1

    if w == 1:
        return n - num + 1

    for i in range(1, n+1):
        if i == num: cy = y; cx = x
        boxes[y][x] = i
        if i % w == 0 or i % w == 1:
            m = (m + 1) % len(moves)
        y, x = y + moves[m][0], x + moves[m][1]

    print(boxes)    
    print(cy, cx)
    count = []
    for j in range(cy+1):
        if boxes[j][cx] == None: continue
        count.append(boxes[j][cx])
    print(count)

    return len(count)