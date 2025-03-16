# 8nlog(n) 和 2n^2 ， 找出 n0
import math
def get_n0 (func1, func2):
    n0 = 1
    while func1(n0) > func2(n0):
      n0 += 1
    return n0 + 1
  
# 原代码保持不变...
print(get_n0(lambda n: 8 if n == 1 else 8*n*math.log(n, 2), lambda n: 2*n*n))  # 添加n=1的特殊处理
print(get_n0(lambda n: 40*n*n, lambda n: 2*n*n*n))