def find_gcd(a: int, b: int) -> int:
    max_common_divisor = max([
        num
        for num in range(1, min(a, b) + 1)
        if a % num == b % num == 0
    ])

    return max_common_divisor
