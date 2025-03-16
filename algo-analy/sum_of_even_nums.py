# 对于任意正整数 n, 求 0 ～ 2n 范围内，所有偶数的和
def sum_of_even_nums1(n: int):
    sum = 0
    for i in range(2*n + 1):
      if i % 2 == 0:
        sum += i
        
    return sum
  
  
def sum_of_even_nums2(n: int):

    sum = 0
    for i in range(0, 2*n+1, 2):
      sum += i
      
    return sum
  
  
def sum_of_even_nums3(n: int):
    """利用等差数列计算公式，从 2 开始"""
    #return (2 + 2*n) * n / 2
    return (2 * 2 + (n - 1) * 2) * n / 2
    
    
# 测试

print(sum_of_even_nums1(10))
print(sum_of_even_nums2(10))
print(sum_of_even_nums3(10))


  