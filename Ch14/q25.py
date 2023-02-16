def solution(N, stages):
    """
    == 프로그래머스 42889
    풀이시간 초과
    1차제출 정확성 70%, 런타임에러 8개
    2차제출 정확성 30%, 런타임에러 많음 시간초과 많음
    3차제출 정확성 70%, 런타임에러 8개
    4차제출 정확성 70%, 런타임에러 8개
    """
    실패율 = []
    stages.sort()
    
    for now_stage in range(1, N+1):
        현스테이지실패유저 = stages.count(now_stage)

        실패율.append([현스테이지실패유저 / len(stages), now_stage])

        for _ in range(현스테이지실패유저):
            stages.pop(0)
        
    실패율.sort(key=lambda elem: -elem[0])
    
    return [elem[1] for elem in 실패율]
