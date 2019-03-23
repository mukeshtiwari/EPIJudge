from test_framework import generic_test
import hy
import hy_gcd

def gcd(x, y):
    return hy_gcd.gcd (x, y)

if __name__ == '__main__':
    exit(generic_test.generic_test_main("gcd.py", 'gcd.tsv', gcd))
