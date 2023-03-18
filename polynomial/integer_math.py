class IntegerMath:
    zero = 0
    one = 1
    value_type = int

    @staticmethod
    def add(a, b):
        assert type(a) == int
        assert type(b) == int
        return a + b

    @staticmethod
    def coeff_str(c):
        """
        Put our constants in parentheses if they are negative.
        """
        assert type(c) == int
        return str(c) if c > 0 else f"({c})"

    @staticmethod
    def mul(a, b):
        assert type(a) == int
        assert type(b) == int
        return a * b

    @staticmethod
    def negate(n):
        assert type(n) == int
        return -n

    @staticmethod
    def power(n, exp):
        assert type(n) == int
        assert type(exp) == int
        return n**exp
