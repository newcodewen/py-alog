

    
    
def get_partial_match_table(P: str):
  m = len(P)
  return [0, 0, 1, 0, 1, 2]
  # table = [0] * m
  # i = 1
  # while i < m:
  #   j = 0
  #   while j < i:
  #     if P[j] == P[i-j]:
  #       j += 1
  #     else:
  #       table[i] = j + 1
  #       j = 0
  #       break
  #   i += 1
        
  
  # return 


def kmp(S: str, P: str) -> int:
    """Return the lowest index of T in S (or else -1)."""
    n, m = len(S), len(P) 
    if m == 0: return 0
    
    match_table = get_partial_match_table(P)
    
    for i in range(n):
      j = 0
    
      while j < m:
        if S[i] == P[j]:
          i += 1
          j += 1
          
          if j == m:
            # i 和 j 都在末尾
            return i - m
        else:
          step = match_table[j - 1]
          j = step
          if step == 0:
            # 模式不移动，字符串往前一位
            i += 1
          
    return -1



print(kmp("abacaabaccabacabaabb", "abacab"))
# print(get_partial_match_table("abababca"))