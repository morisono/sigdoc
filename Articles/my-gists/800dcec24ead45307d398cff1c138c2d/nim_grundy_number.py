def nim_grundy_number(piles):
    xor_sum = 0
    for pile in piles:
        xor_sum ^= pile
    return xor_sum
