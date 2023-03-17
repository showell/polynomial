from numpy.polynomial.polynomial import Polynomial
from polynomial.poly import Poly


def assert_equal(m, n):
    if m != n:
        raise AssertionError(f"{m} != {n}")


def numpy_eval(p, x):
    assert type(p) == Poly
    assert type(x) == int
    vector = p.numpy_vector()
    return int(Polynomial(vector)(x))


x = Poly.var("x")
p = (2 * x + 1) * (2 * x - 1)
vector = p.numpy_vector()
assert vector == [-1, 0, 4]

assert p.eval(x=7) == 195
assert numpy_eval(p, x=7) == 195

for i in range(1000):
    assert_equal(p.eval(x=i), numpy_eval(p, i))

"""
We can use a slightly more complicated polynomial to
confirm that Poly and Polynomial produce the same results.
"""
q = (x + 1) * (x - 2) * (x + 3) * (x - 4) + (x + 5)

for i in range(1000):
    assert_equal(q.eval(x=i), numpy_eval(q, i))

"""
Note that for large degree polynomials, the Poly class gives more
precise answers than numpy, because numpy is presumably using
floats under the hood and getting rounding errors.
"""

p = x**30
assert_equal(p.eval(x=10), 10**30)
# Python and Poly are correct.
assert (10**30) == 1000000000000000000000000000000

# numpy has a bit of an error
assert_equal(numpy_eval(p, 10), 999999999999999879147136483328)
