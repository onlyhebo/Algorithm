import random


def select_sort(sample):
    print(sample)
    for i in range(len(sample)-1):
        min_idx = i
        for j in range(i, len(sample)):
            if sample[j] < sample[min_idx]:
                min_idx = j
        sample[i], sample[min_idx] = sample[min_idx], sample[i]
    return sample


if __name__ == '__main__':
    ls = list(range(100))
    sample = random.sample(ls, 20)
    print(select_sort(sample))


# 每次找出最小的元素放在当前未排序序列的第一位
# 复杂度
# 最坏时间复杂度 O(N^2)
# 最优时间复杂度 O(N^2)
# 平均时间复杂度 O(N^2)
# 额外空间复杂度 O(1)
# 稳定性 稳定
