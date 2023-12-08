import math

def matrix_fibonacci(target: int) -> int:
    """
    Это самый быстрый способ вычисления числа Фибоначчи с использованием матричной математики.
    Он выполняется быстро.
    Математика подробно описана на странице википедии по адресу: https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
    >>> matrix_fibonacci(80)
    23416728348467685
    """
    v1, v2, v3 = (
        1,
        1,
        0,
    )
    for record in bin(
            target
    )[3:]: 
        calc = v2 * v2
        v1, v2 = v1 * v1 + calc, (v1 + v3) * v2
        v3 = calc + v3 * v3

        if record == "1":
            v1, v2, v3 = v1 + v2, v1, v2
    return int(v2)
    

def fibonacci_goldenratio(target):
    """
    This method works by calculating the golden ratio, and then
    raising the golden ration to the power of n, whereby n is the position of the fibonacci sequence.
    As we look for higher and higher values of n, rounding errors throw us off. This method works for values of n
    less than 72 or so.
    :param target:
    :return:
    >>> fibonacci_goldenratio(80)
    23416728348467685
    """
    import math

    if target < 2:
        return target

    if target > 71:
        return matrix_fibonacci(target)

    sqrt5 = math.sqrt(5)
    golden_ratio = (1 + sqrt5) / 2

    return math.floor(math.pow(golden_ratio, target) / sqrt5)

print(fibonacci_goldenratio(80))
