def solution(message, spoiler_ranges):
    # 1. 메시지에서 단어 추출 (시작 인덱스, 끝 인덱스, 단어 문자열)
    words = []
    n = len(message)
    i = 0
    while i < n:
        if message[i] != ' ':
            start = i
            while i < n and message[i] != ' ':
                i += 1
            end = i - 1  # 끝 인덱스 포함
            words.append((start, end, message[start:i]))
        else:
            i += 1

    # 2. 스포 방지 구간을 왼쪽 -> 오른쪽(시작 인덱스 기준) 정렬하여 클릭 순서 확립
    sorted_ranges = sorted(spoiler_ranges, key=lambda x: x[0])

    non_spoiler_words = set()
    spoiler_words_info = [] # (완전 공개되는 클릭 스텝, 단어 시작 인덱스, 단어 문자열)

    # 3. 단어별 스포 방지 구간 겹침 여부 확인 및 완전 공개 시점 계산
    for w_start, w_end, w_str in words:
        overlapping_steps = []
        for step, (r_start, r_end) in enumerate(sorted_ranges):
            # 겹침 확인 (양끝 포함 기준: 단어 시작점이 구간 끝점보다 작거나 같고, 단어 끝점이 구간 시작점보다 크거나 같음)
            # ※ 주의: 만약 문제의 구간이 [start, end) 형태(끝점 미포함)라면, r_end 대신 (r_end - 1)로 변경하세요.
            if w_start <= r_end and w_end >= r_start:
                overlapping_steps.append(step)

        if not overlapping_steps:
            # 어떤 구간과도 겹치지 않는다면 완벽한 일반 구간 단어
            non_spoiler_words.add(w_str)
        else:
            # 걸쳐있는 구간 중 가장 늦게 클릭되는 스텝에서 단어가 완전히 공개됨
            reveal_step = max(overlapping_steps)
            spoiler_words_info.append((reveal_step, w_start, w_str))

    # 4. 공개 시점(스텝) 순으로 정렬하되, 동시 공개 시 왼쪽 단어(시작 인덱스)부터 처리
    spoiler_words_info.sort(key=lambda x: (x[0], x[1]))

    # 5. 중요한 단어 개수 판별
    important_count = 0
    seen_spoiler_words = set()

    for step, w_start, w_str in spoiler_words_info:
        # 조건 검사: 일반 구간에 등장한 적 없고, 이전에 스포 단어로 공개된 적도 없어야 함
        if w_str not in non_spoiler_words and w_str not in seen_spoiler_words:
            important_count += 1
            
        # 중요한 단어 여부와 무관하게, 한 번 공개된 스포 단어는 중복 처리용 기록
        seen_spoiler_words.add(w_str)

    return important_count