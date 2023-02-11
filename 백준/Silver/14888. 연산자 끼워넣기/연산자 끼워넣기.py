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
    if (front < 0 and back > 0) or (front > 0 and back < 0):  # 한쪽만 음수
      rslt = ((front * -1) // back) * -1
    else:
      rslt = front // back

  return rslt


def 재귀연산해보기(남은_연산항, 남은_연산자, 더해진값):
  global 최대값
  global 최소값

  기존_연산값 = 더해진값
  if sum(남은_연산자) == 1:
    for idx in range(4):
      if 남은_연산자[idx] > 0:
        기존_연산값 = 연산하기(기존_연산값, 남은_연산항[0], idx)
        최대값 = 기존_연산값 if 기존_연산값 > 최대값 else 최대값
        최소값 = 기존_연산값 if 기존_연산값 < 최소값 else 최소값
    return
  else:
    for 고른_연산자 in range(4):
      if 남은_연산자[고른_연산자] > 0:
        임시_연산값 = 연산하기(기존_연산값, 남은_연산항[0], 고른_연산자)
        넘겨줄_연산자 = 남은_연산자[:]
        넘겨줄_연산자[고른_연산자] -= 1
        재귀연산해보기(남은_연산항[1:], 넘겨줄_연산자, 임시_연산값)


n = int(input())
연산항배열 = list(map(int, sys.stdin.readline().rstrip().split()))
연산자배열 = list(map(int, sys.stdin.readline().rstrip().split()))

global 최대값
최대값 = -1000000001
global 최소값
최소값 = 1000000001

재귀연산해보기(연산항배열[1:], 연산자배열, 연산항배열[0])

print(f"{최대값}\n{최소값}")
