import random


def insert_sort(sample):
    for i in range(1, len(sample)):
        while i > 0:
            if sample[i] < sample[i-1]:
                sample[i], sample[i-1] = sample[i-1], sample[i]
                i -= 1
            else:
                break


if __name__ == '__main__':
    ls = list(range(100))
    sample = random.sample(ls, 30)
    insert_sort(sample)
    assert sample == sorted(sample)
    print(sample)


# 工作原理
# 通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
#
# 复杂度
# 最坏时间复杂度 O(N^2)
# 最优时间复杂度 O(N)
# 平均时间复杂度 O(N^2)
# 额外空间复杂度 O(1)
# 稳定性 稳定
