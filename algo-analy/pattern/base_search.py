# 穷举法

def linear_search(str, pattern):
    for i in len(str):
        j = 0
        while str[i + j] == pattern[j] and j < len(pattern):
          j += 1
          if j == len(pattern):
             return i


# 显示回退

def linear_search2(str, pattern):
  n = len(str)
  m = len(pattern)
  
  i = 0
  j = 0
  
  while i < n and j < m:
    if str[i] == pattern[j]:
      i += 1
      j += 1  
    else:
      i = i - j + 1
      j = 0
      
  if j == m:
    return i - m
  else:
    return n
  
  