def solution(X, Y):
    answer_list = []
    
    count_x = [0] * 10
    count_y = [0] * 10
    
    for char in X:
        count_x[int(char)] += 1
        
    for char in Y:
        count_y[int(char)] += 1
        
    for i in range(9, -1, -1):

        common_count = min(count_x[i], count_y[i])

        if common_count > 0:
            answer_list.append(str(i) * common_count)
            
    answer = "".join(answer_list)
    
    if not answer:
        return "-1"
    
    if answer[0] == "0":
        return "0"
        
    return answer