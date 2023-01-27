# == 백준 1439
# 현 소스코드는 주석 포함 버전
dasom_num = input()

start_num = dasom_num[0]
print(start_num)
check_num = ""
rslt_cnt = 0

for idx in range(1, len(dasom_num)):
  print(f"debug: {dasom_num[idx]}")
  # 첫 숫자와 다를 경우
  if dasom_num[idx] != start_num:
    print(f"debug: check_num: {check_num}")
    # 체크를 시작하지 않았을 경우
    if check_num == "":
      rslt_cnt += 1
      check_num = dasom_num[idx]
    # 체크를 시작한 경우는 계속 진행하면 됨
      
    # elif check_num != dasom_num[idx]:
    #   # 체크를 시작한 후 체크를 시작한 숫자와 다를 경우
    #   check_num = ""  # 체크 중단
    #   continue
    # else:
    # 체크를 시작한 후 체크를 시작한 숫자와 같을 경우: 안걸림
    # continue
    
  else: # 첫 숫자와 같을 경우
    if check_num != dasom_num[idx]:
      # 체크 중단 로직
      check_num = ""
  # continue

print(rslt_cnt)
