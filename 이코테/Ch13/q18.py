"""
== 프로그래머스 60058(lv2)
풀이 통과
1회차 풀이 시간: 37분 41초 40
"""


def 올바름체크(p):
  chk = [0, 0]  # 0번 (, 1번 )
  for elem in p:  # 올바른 괄호 문자열 검사
    if elem == "(":
      chk[0] += 1
    else:
      chk[1] += 1

    if chk[1] > chk[0]:
      return False  # 올바른 괄호 문자열이 아님

  return True


def u후처리(u):
  list_u = list(u)
  list_u.pop(0)
  list_u.pop(-1)

  retn_u = ""
  for elem in list_u:
    if elem == "(":
      retn_u += ")"
    else:
      retn_u += "("

  return retn_u


def v_dfs(p):
  chk = [0, 0]  # 0번 (, 1번 )
  u = ""
  v = ""

  if len(p) == 0:  #1번
    return ""

  for idx, elem in enumerate(p):  # 2번 u,v 나누기
    # print(f"idx:{idx}")
    if elem == "(":
      chk[0] += 1
    else:
      chk[1] += 1

    if chk[0] == chk[1]:
      # print(idx)
      u = p[0:idx + 1]
      v = p[idx + 1:len(p)]
      break

  v = v_dfs(v)  # v 재수행

  retn_str = ""
  if 올바름체크(u):  # 3번
    retn_str = u + v
  else:  # 4번
    retn_str = "(" + v + ")" + u후처리(u)
    # retn_str = "(" + v + ")"

  return retn_str


def solution(p):
  answer = ''

  if 올바름체크(p):
    answer = p
  else:
    answer = v_dfs(p)

  return answer
