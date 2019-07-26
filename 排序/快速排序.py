import random


def quick_sort(sub):
    if len(sub) <= 1:
        if sub:
            final.append(sub[0])
        return
    l = 1
    r = len(sub) - 1
    while True:
        if sub[l] > sub[0]:
            while sub[r] >= sub[0]:
                if r == l: break
                r -= 1
            sub[l], sub[r] = sub[r], sub[l]
        if l < r: l += 1
        if l == r:
            if sub[l] > sub[0]:
                l -= 1
            sub[0], sub[l] = sub[l], sub[0]
            break
    quick_sort(sub[:l])
    final.append(sub[l])
    quick_sort(sub[l+1:])


if __name__ == '__main__':
    ls = list(range(1000))
    sample = random.sample(ls, 50)
    final = []
    quick_sort(sample)
    assert final == sorted(sample)
    print(final)
