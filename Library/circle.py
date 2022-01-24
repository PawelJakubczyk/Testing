from math import pi


def circle_area(r: [int, float]):
    if type(r) != float and type(r) != int:
        raise ValueError('Wrong data type')
    elif r < 0:
        raise ValueError('The radius cannot be negative')
    else:
        return pi*(r**2)

