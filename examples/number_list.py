def arr_get(lst, i):
    return lst[i] if i < len(lst) else 0

class NumberList:
    def __init__(self, lst):
        self.lst = lst

    def __add__(self, other):
        return NumberList.add(self.lst, other.lst)

    def __mul__(self, other):
        return NumberList.mul(self.lst, other.lst)

    def __eq__(self, other):
        return self.lst == other.lst

    @staticmethod
    def add(lst1, lst2):
        new_size = max(len(lst1), len(lst2))
        return NumberList([arr_get(lst1, i) + arr_get(lst2, i) for i in range(new_size)])

    @staticmethod
    def mul(lst1, lst2):
        # do the analog of elementary school arithmic
        result = NumberList([])
        for i, elem in enumerate(lst1):
            result += NumberList.mul_constant(elem, [0] * i + lst2)
        return result

    @staticmethod
    def mul_constant(c, lst):
        return NumberList([c * elem for elem in lst])

if __name__ == "__main__":
    assert NumberList([1, 0, 3]) + NumberList([2, 4, 7, 13]) == NumberList([3, 4, 10, 13])
    assert NumberList([1, 2]) * NumberList([1, 3]) == NumberList([1, 5, 6])
