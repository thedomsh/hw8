a = 7
b = 2
c = 8


def triangle_perimetr(a_1=a, b_1=b, c_1=c):
    return a_1 + b_1 + c_1


def triangle_area(a_1=a, b_1=b, c_1=c):
    p = (a_1 + b_1 + c_1) / 2
    return ((p - a_1) * (p - b_1) * (p - c_1)) ** 0.5
