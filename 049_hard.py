from pprint import pprint
from collections import defaultdict
from itertools import product

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

def f(num_dice, sum_dice):
    sums = dice_sums(num_dice)
    return sums[sum_dice]

#for x in range(10):
    #print "=" * 30, x, "=" * 30
    #sums = dice_sums(x)
    #for key in sorted(sums.keys()):
        #print key, sums[key]

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

def fact(iterator):
    return 'blah'

print list(combos(5, 20))
