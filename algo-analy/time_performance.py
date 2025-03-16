from prefix_avarage import prefix_average1, prefix_average2, prefix_average3

import time
import random
import matplotlib.pyplot as plt

def time_performance():
    """测试三个算法在不同输入规模下的性能"""
    sizes = range(100, 10000, 500)
    times = [[], [], []]  # 存储三个算法的耗时
    
    for n in sizes:
        S = [random.randint(1, 100) for _ in range(n)]
        
        # 测试算法1
        start = time.perf_counter()
        prefix_average1(S)
        times[0].append(time.perf_counter() - start)
        
        # 测试算法2
        start = time.perf_counter()
        prefix_average2(S)
        times[1].append(time.perf_counter() - start)
        
        # 测试算法3
        start = time.perf_counter()
        prefix_average3(S)
        times[2].append(time.perf_counter() - start)
    
    # 绘制双对数坐标图
    plt.figure(figsize=(10, 6))
    plt.loglog(sizes, times[0], 'ro-', label='O(n²) - Nested Loop')
    plt.loglog(sizes, times[1], 'bs-', label='O(n²) - Slice Sum')
    plt.loglog(sizes, times[2], 'g^-', label='O(n) - Cumulative')
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Algorithm Performance Comparison')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()

if __name__ == '__main__':
    time_performance()
