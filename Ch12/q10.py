# 비효율적 풀이(38개중 4개 통과)
def rotate_right90(key):
    m = len(key) # 처음에 길이 구하기
    new_key = [[0] * m for _ in range(m)] # 회전용 키를 위한 공간
    m -= 1 # 인덱스 접근을 위해 길이 하나 줄이기
    
    for key_row in key: # 행에 있는 배열 접근
        for idx, element in enumerate(key_row): # 배열에서 요소랑 열 인덱스 빼오기
            new_key[idx][m] = element # 90도 회전시킨 인덱스에 대입
        m -= 1 # 90도 회전 인덱스를 위해 m값 하나 줄이기
    
    return new_key # 회전시킨 키 반환

def solution(key, lock):
    n = len(lock) # n값 가져오기
    rslt_find = [[0] * n for _ in range(n)] # 결과값 판단을 위한 배열 초기화
    
    for rotate in range(0,4): # 회전 수 만큼 내부 수행
        for row_start in range(n): # lock의 행 판단 시작점을 1~n까지 반복
            # print(f"row_start: {row_start}")
            for col_start in range(n): # lock의 열 판단 시작점을 1~n까지 반복
                rslt_find = [elem.copy() for elem in lock] # 판단 시작하기 전에 lock 배열을 deep-copy 하기(key가 안들어가는 부분을 초기화 하기 위함)
                # print(f"col_start: {col_start}")
                
                for key_row, row in enumerate(range(row_start, n)): # lock의 행 시작점부터 행 끝까지
                    for key_col, col in enumerate(range(col_start, n)): # lock의 열 시작점부터 열 끝까지
                        rslt_find[row][col] = key[key_row][key_col] ^ lock[row][col] # 행/열 = 키_행/키_열 xor 자물쇠_행/자물쇠_열
                # print(rslt_find)
                answer = True # 배열 대입이 끝날 때마다 배열 요소가 맞는지 보기
                for row in rslt_find: # 각 열마다 보기
                    if 0 in row: # 열에 하나라도 빈 데가 있으면
                        answer = False
                        break # 다시 하라 하기
                if answer:
                    return answer
                print(answer)
            
        key = rotate_right90(key) # 한 방향에서 판단 다 끝났으면 키 돌려주기
        print("rotated")
                
        # for row_idx, lock_row in enumerate(lock):
        #     for col_idx, lock_elem in enumerate(lock_row):
        #         rslt_find[row_idx][col_idx] = key[row_idx][col_idx] ^ lock_elem
        
#         print("---")
#         print(rslt_find)
    
    # print(key)
    # key = rotate_right90(key)
    # print(key)
    
    # return True