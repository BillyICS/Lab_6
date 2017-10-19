def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


def main():
    number = int(input("Enter a nonnegative integer: "))
    fact = factorial(number)
    print('The factorial of %d is %d' % (number, fact))

main()