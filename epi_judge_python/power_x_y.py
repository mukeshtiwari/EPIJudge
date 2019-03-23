from test_framework import generic_test
import hy
import hy_power_x_y

def power(x, y):
    # TODO - you fill in here.
    if y < 0 :
        return 1.0 / hy_power_x_y.power(x, -1 * y)
    else:
        return hy_power_x_y.power(x, y)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
