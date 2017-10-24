import parser
from math import *


def function(x, y, f):
    return eval(f)


def main():
    raw_f = input('expression (python format): ')
    x_0, y_0 = [float(x) for x in input('known x and y values: ').split()]
    step_cnt = int(input('number of steps: '))
    h = float(input('step size: '))

    f = parser.expr(raw_f).compile()

    x_tmp = x_0
    y_tmp = y_0

    print('x%d: %f, y%d: %f' % (0, x_tmp, 0, y_tmp))

    for step in range(step_cnt):
        slope = function(x_tmp, y_tmp, f)
        x_tmp += h
        y_tmp += h * slope
        print('x%d: %f, y%d: %f' % (step + 1, x_tmp, step + 1, y_tmp))


if __name__ == '__main__':
    main()
