import random


def maopao(sample, reverse=False):
    for passnum in range(len(sample)-1, 0, -1):
        for i in range(passnum):
            if not reverse:
                if sample[i] > sample[i+1]:
                    sample[i], sample[i+1] = sample[i+1], sample[i]
            else:
                if sample[i] < sample[i+1]:
                    sample[i], sample[i+1] = sample[i+1], sample[i]
    return sample


if __name__ == '__main__':
    ls = list(range(100))
    sample = random.sample(ls, 30)
    print(sample)
    print(maopao(sample, reverse=True))
    print(sample)
    print(maopao(sample, reverse=False))
# 工作原理
# 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
# 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
# 针对所有的元素重复以上的步骤，除了最后一个。
# 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

# 复杂度
# 最坏时间复杂度 O(N^2)
# 最优时间复杂度 O(N)
# 平均时间复杂度 O(N^2)
# 额外空间复杂度 O(1)
# 稳定性 稳定
