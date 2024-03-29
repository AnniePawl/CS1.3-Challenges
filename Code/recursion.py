def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0, otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n is invalid input
    if not isinstance(n, int) or n < 0:
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # if input valid, call on factorial_iterative or factorial_recurssive to return product
    return factorial_iterative(n)
    return factorial_recursive(n)


def factorial_iterative(n):
    """factorial_iterative(n) returns product of the integers 1 thru n """
    factorial = 1
    for i in range(n):
        factorial = factorial * (i + 1)
    return factorial


def factorial_recursive(n):
    """factorial_recursive(n) calls on itself to return products of integers 1 thru n  """
    # check if n is one of the base cases
    if n == 0 or n == 1:
        return 1
    # check if n is an integer larger than base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    # main()
    print(factorial_iterative(5))
    print(factorial_recursive(5))
