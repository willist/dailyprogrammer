def is_kaprekar(num):
    square = str(num * num)
    midpoint = len(square) / 2
    left = square[:midpoint] or 0
    right = square[midpoint:] or 0
    new_num = int(left) + int(right)
    return num == new_num

print filter(is_kaprekar, range(1000))
