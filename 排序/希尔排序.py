import random


def shell_sort(sample):
    gap = len(sample) // 2
    while gap > 0:
        for i in range(gap, len(sample)):
            while sample[i] < sample[i-gap] and i - gap >= 0:
                sample[i], sample[i-gap] = sample[i-gap], sample[i]
                i -= gap
        gap //= 2


if __name__ == '__main__':
    ls = list(range(100))
    sample = random.sample(ls, 30)
    shell_sort(sample)
    assert sample == sorted(sample)
    print(sample)

# 工作原理
# 希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。希尔排序是非稳定排序算法。
#
# 希尔排序是基于插入排序的以下两点性质而提出改进方法的：
#
# 插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率；
# 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位。
# 复杂度
# 最坏时间复杂度 O(Nlog^2N)
# 最优时间复杂度 O(N)
# 平均时间复杂度 -
# 额外空间复杂度 O(1)
# 稳定性 不稳定

