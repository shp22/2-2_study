def solution(schedules, timelogs, startday):
    answer = []
    for time, enter in zip(schedules, timelogs):
        hour, minute = time // 100, time % 100
        time = hour * 60 + minute + 10
        result = True
        day = startday

        for en in enter:
            if day in [6,7]: day = day % 7 + 1; continue
            hour, minute = en // 100, en % 100
            en = hour * 60 + minute
            if time < en: result = False; print(result); break
            day = day % 7 + 1

        answer.append(result)

    return sum(answer)