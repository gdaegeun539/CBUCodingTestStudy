"""
== 백준 14888
풀이시간초과
1차 풀이시간: 54분 19초 00
풀이 제출 통과
"""
import sys


def 연산하기(front, back, oper):
  rslt = 0
  if oper == 0:  # 합
    rslt = front + back
  elif oper == 1:  # 차
    rslt = front - back
  elif oper == 2:  # 곱
    rslt = front * back
  elif oper == 3:  # 분
    """
    사실 파이썬의 나누기 연산 방식은 규칙과 동일하여 별도의 처리가 필요하지 않음
    """
    if (front < 0 and back > 0) or (front > 0 and back < 0):  # 한쪽만 음수
      rslt = ((front * -1) // back) * -1  # 여기 편법인데 통과됐네
    else:
      rslt = front // back

  return rslt


def 재귀연산해보기(남은_연산항, 남은_연산자, 더해진값):
  global 최대값, 최소값

  기존_연산값 = 더해진값
  if sum(남은_연산자) == 1:
    # 마지막 연산만 남은 경우
    for idx in range(4):
      # 어떤 연산자가 남았는지 파악
      if 남은_연산자[idx] > 0:
        # 연산 후 최대/최소값 갱신
        기존_연산값 = 연산하기(기존_연산값, 남은_연산항[0], idx)
        최대값 = 기존_연산값 if 기존_연산값 > 최대값 else 최대값
        최소값 = 기존_연산값 if 기존_연산값 < 최소값 else 최소값
    return
  else:
    # 아직 연산자가 많이 남은 경우
    for 고른_연산자 in range(4):
      # 0~3(합/차/곱/분)을 돌면서 있는 연산자만 연산 및 dfs/재귀 호출 수행
      if 남은_연산자[고른_연산자] > 0:
        임시_연산값 = 연산하기(기존_연산값, 남은_연산항[0], 고른_연산자)
        # 연산자 배열을 deep-copy 하고 지금 쓴 연산자를 제거하고 dfs/재귀 호출 수행
        넘겨줄_연산자 = 남은_연산자[:]
        넘겨줄_연산자[고른_연산자] -= 1
        재귀연산해보기(남은_연산항[1:], 넘겨줄_연산자, 임시_연산값)


n = int(input())
연산항배열 = list(map(int, sys.stdin.readline().rstrip().split()))
연산자배열 = list(map(int, sys.stdin.readline().rstrip().split()))

최대값 = -1000000001
최소값 = 1000000001

재귀연산해보기(연산항배열[1:], 연산자배열, 연산항배열[0])

print(f"{최대값}\n{최소값}")
