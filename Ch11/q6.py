# 프로그래머스 lv4 문제임


def solution(food_times, k):
  answer = 0
  food_left = len(food_times)
  food_idx = 0

  times = 0
  while times <= k:
    print(answer)

    # 남은 음식이 없을때 반환
    if food_left <= 0:
      answer = -1
      break

    # 음식 인덱스가 길이를 넘어가면 되돌리기
    if food_idx > len(food_times) - 1:
      food_idx = 0
      answer = 1

    # 지금 인덱스에 음식이 없으면 다음으로 넘어가기
    if food_times[food_idx] == 0:
      food_idx += 1
      food_left -= 1
      continue
    else:  # 음식 있으면 먹기
      food_times[food_idx] -= 1
      answer = food_idx + 1
      food_idx += 1
      times += 1

  print(answer)
  return answer
