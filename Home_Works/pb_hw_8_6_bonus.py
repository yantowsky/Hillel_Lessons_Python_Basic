def sum_of_digits(number: int) -> int:
    sum_list_digits = sum([
        int(num)
        for num in str(number)
        if num.isdigit()
    ])

    return sum_list_digits
