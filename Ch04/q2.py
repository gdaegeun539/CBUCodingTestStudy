n, m = map(int, list(input().split()))
now_x, now_y, sight = map(int, list(input().split()))

arr_map = [[] for _ in range(m)]
for idx in range(n):
  arr_map[idx] = list(map(int, list(input().split())))

print(f"DEBUG\n{arr_map}\n")

# 현재 칸은 이동에서 더해지지 않고, 다음 칸으로 갈때 마킹되어 돌아올 수 없음
rslt = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sight_change = [1, 2, 3, 0]
sight_cnt = 1

while True:
  sight = sight_change[sight]
  move_x = now_x + dx[sight]
  move_y = now_y + dy[sight]
  # sight_cnt = 1

  if move_x < 0 or move_x >= n or move_y < 0 or move_y >= n or arr_map[move_x][
      move_y] == 1:  # 바다 혹은 이미 간 곳 아니면 지도 영역이 아닌 곳
    if sight_cnt == 4:  # 방향 못돌릴 때 이미 간 곳(뒤)은 바다로 마킹 완료: 못 돌아감
      # but 이 경우는 도착 한 곳에 왼쪽과 오른쪽 두 곳만 길이 있을 때 한 쪽을 못감(결함)
      # move_x = now_x + dx[sight - 2]
      # move_y = now_y + dx[sight - 2]
      # if sight_change
      break
    else:  # 방향 돌릴 수 있을 때
      sight_cnt += 1
      continue
  else:  # 육지(안간 곳)
    arr_map[now_x][now_y] = 1
    now_x = move_x
    now_y = move_y
    sight_cnt = 1
    rslt += 1

print(rslt)
