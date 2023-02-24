"""
== 백준 10825
풀이시간초과
내장메소드 사용법 헷갈림
1차 풀이시간: 약 22분
풀이 제출 통과

비 pythonic한 코드
"""
import sys

n = int(input())

학생들 = []
for _ in range(n):
  # 입력받기
  temp_list = list(sys.stdin.readline().rstrip().split())
  for idx in range(1, 4):
    # 점수 데이터 형태에 맞게 정렬하기
    temp_list[idx] = int(temp_list[idx])
  학생들.append(tuple(temp_list))

# 주어진 조건에 맞게 정렬하라 시키고 정렬하기
# https://infinitt.tistory.com/122 다중조건정렬 참고
학생들.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for 학생 in 학생들:
  print(학생[0])
