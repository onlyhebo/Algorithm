import random


def quick_sort(sample, left, right):
    start = left
    last = right
    if left < right:
        left += 1
        while True:
            while left <= right and sample[left] <= sample[start]:
                left += 1
            while left <= right and sample[right] >= sample[start]:
                right -= 1
            if right < left:
                break
            sample[left], sample[right] = sample[right], sample[left]
        sample[start], sample[right] = sample[right], sample[start]
        quick_sort(sample, start, right-1)
        quick_sort(sample, right+1, last)


if __name__ == '__main__':
    ls = list(range(100))
    sample = random.sample(ls, 30)
    quick_sort(sample, left=0, right=len(sample)-1)
    assert sample == sorted(sample)
    print(sample)

# 快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。步骤如下：
#
# 从数列中挑出一个元素，称为“基准”（pivot）；
# 重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。在这个分割结束之后，该基准就处于数列的中间位置。这个称为分割（partition）操作；
# 递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。
# 递归到最底部时，数列的大小是零或一，也就是已经排序好了。这个算法一定会结束，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。
#
# 复杂度
# 最坏时间复杂度 O(N^2)
# 最优时间复杂度 O(NlogN)
# 平均时间复杂度 O(NlogN)
# 额外空间复杂度 O(logN)
# 稳定性 不稳定
