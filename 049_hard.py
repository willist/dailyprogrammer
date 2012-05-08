import sys
from collections import defaultdict
from contextlib import contextmanager
from itertools import product
from math import factorial

def dice_iter(n):
    for item in range(n):
        yield range(1,7)

def count_sums(iterator):
    counter = defaultdict(int)
    for item in iterator:
        if sum(item) == 5:
            print item
        counter[sum(item)] += 1
    return counter

def dice_sums(n):
    return count_sums(product(*dice_iter(n)))

@contextmanager
def no_recursion_limit():
    limit = sys.getrecursionlimit()
    sys.setrecursionlimit(100000)
    yield
    sys.setrecursionlimit(limit)

def combos(num_dice, target_sum, prev_die=None):
    if num_dice == 1 and prev_die <= target_sum <= 6:
        yield [target_sum]
    else:
        start = 1 if prev_die is None else prev_die
        end = 7
        for head in range(start, end):
            remaining_sum = target_sum - head
            remaining_dice = num_dice - 1
            if remaining_dice <= remaining_sum <= (remaining_dice * 6):
                for tail in combos(remaining_dice, remaining_sum, head):
                    yield [head] + tail

def counter(iterator):
    counter = defaultdict(int)
    for item in iterator:
        counter[item] += 1
    return counter

def j(num_dice, sum_dice):
    total = 0
    top = factorial(num_dice)
    with no_recursion_limit():
        for index, combo in enumerate(combos(num_dice, sum_dice)):
            count = counter(combo)
            bottoms = [factorial(c) for c in count.values()]
            bottom = reduce(lambda x,y: x*y, bottoms)
            sub_total = top/bottom
            if not index % 100000:
                print combo, sub_total
            total += sub_total
    return total
        

if __name__ == "__main__":
    assert j(02, 07) == 6
    assert j(02, 10) == 3
    assert j(02, 12) == 1
    assert j(03, 10) == 27
    assert j(05, 20) == 651
    assert j(07, 30) == 12117
    assert j(10, 50) == 85228
    print j(20, 100)
    print j(1100, 5000) % pow(10,7)
