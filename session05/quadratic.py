import math


def quadratic(a, b, c):
    """Simple version of quadratic equation solver
    a: float
    b: float
    c: float

    Return two roots of the quadratic equation"""
    discriminant = b**2 - 4 * a * c  # calculate the discriminant

    x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return x_1, x_2


# print(quadratic(1, 2, 1))

# aa = float(input("Enter a number: >>> "))
# bb = float(input("Enter a number: >>> "))
# cc = float(input("Enter a number: >>> "))

# print(quadratic(aa, bb, cc))




















def quadratic(a, b, c):
    """Solve quadratic function and return two roots.
    a*x**2 + b*x + c = 0

    a: float
    b: float
    c: float

    Return None if there is no real number solution"""
    if a == 0 and b == 0:
        print('Hey, this is not a quadratic equation!')
        return None
    if a == 0:
        print('This is a linear function.')
        return -c / b

    discriminant = b**2 - 4 * a * c  # calculate the discriminant

    if discriminant >= 0:  # equation has solutions
        x_1 = (-b + math.sqrt(discriminant)) / 2 * a
        x_2 = (-b - math.sqrt(discriminant)) / 2 * a
        return x_1, x_2
    else:
        # raise Exception('No real number solution.')
        print('No real number solution.')
        return None
        raise ValueError('No real number solution!')


def main():
    print(quadratic(2, 2, 2))
    print(quadratic(1, 4, 1))

    a = float(input('please enter a number:'))
    b = float(input('please enter a number:'))
    c = float(input('please enter a number:'))
    
    result = quadratic(a, b, c)

    if result is not None:
        if isinstance(result, float):
            print(f'The solution is {result}.')
        else:
            print(f'Two roots are {result[0]} and {result[1]}.')
    else:
        print('Sorry 😎')


if __name__ == "__main__":
    main()
