import parser
from math import *


def function(x, f):
    return eval(f)


def main():
    raw_f = input('expression (python format): ')
    x_max = float(input('max value: '))
    x_min = float(input('min value: '))

    f = parser.expr(raw_f).compile()

    sub_count = int(input('rectangle count: '))
    approx_type = input('type (left/right/trape): ')

    if not (approx_type == 'left' or approx_type == 'right' or approx_type == 'trape'):
        raise ValueError

    delta_x = (x_max - x_min) / sub_count
    area = 0
    for i in range(sub_count):
        x_val_l = x_min + delta_x * i
        x_val_r = x_min + delta_x * (i + 1)
        if approx_type == 'left':
            area += function(x_val_l, f) * delta_x
        elif approx_type == 'right':
            area += function(x_val_r, f) * delta_x
        else:
            area += (function(x_val_l, f) + function(x_val_r, f)) * delta_x / 2
        # elif approx_type == 'upper':
        #     area += max(function(x_val_l, f), function(x_val_r, f)) * delta_x
        # else:
        #     area += min(function(x_val_l, f), function(x_val_r, f)) * delta_x

    print('answer: ', area)


if __name__ == '__main__':
    main()
