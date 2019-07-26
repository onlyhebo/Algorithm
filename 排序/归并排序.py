import random


def merge(l,r):
    new = []
    while l and r:
        if l[0] <= r[0]:
            new.append(l.pop(0))
        else:
            new.append(r.pop(0))
    if l:
        new.extend(l)
    if r:
        new.extend(r)
    return new


def merge_sort(sample):
    if len(sample) == 1:
        return sample
    mid = len(sample) // 2
    left = merge_sort(sample[:mid])
    right = merge_sort(sample[mid:])
    return merge(left, right)


if __name__ == '__main__':
    ls = list(range(100))
    sample = random.sample(ls, 30)
    sample = merge_sort(sample)
    assert sample == sorted(sample)
    print(sample)
