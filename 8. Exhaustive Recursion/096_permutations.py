"""
--- Permutations ---
Write a function, permutations, that takes in a list an argument. The function should return a 2D list where each sublist represents one of the possible permutations of the list.

The sublists may be returned in any order.

You may assume that the input list contains unique items.
"""
import unittest

# recursive
def permutations1(items):
    if not items:
        return [[]]

    first = items[0]
    remaining = items[1:]
    perms = permutations(remaining)

    result = []
    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + [first] + perm[i:])

    return result

def permutations(items):
    result = []
    if not items:
        return [[]]
    if len(items) == 1:
        return [items[:]]
    
    for i in range(len(items)):
        n = items.pop(0)
        res = permutations(items)
        for r in res:
            r.append(n)
        result.extend(res)
        items.append(n)
    return result


# non recursive
def permutations3(items):
    result = [[]]
    for item in items: # add one element and one element
        perms = []
        for perm in result:
            for i in range(len(perm) + 1):
                perms.append(perm[:i] + [item] + perm[i:])
        result = perms
    return result

print(permutations(['a', 'b', 'c']))
print(permutations(['red', 'blue']))
print(permutations([8, 2, 1, 4]))
exit()
class Test(unittest.TestCase):
    def test_00(self):
        print()
        assert permutations(['a', 'b', 'c']) == [
            ['a', 'b', 'c'],
            ['b', 'a', 'c'],
            ['b', 'c', 'a'],
            ['a', 'c', 'b'],
            ['c', 'a', 'b'],
            ['c', 'b', 'a']
        ]

    def test_01(self):
        assert permutations(['red', 'blue']) == [
            ['red', 'blue'],
            ['blue', 'red']
        ]

    def test_02(self):
        assert permutations([8, 2, 1, 4]) == [
            [8, 2, 1, 4], [2, 8, 1, 4],
            [2, 1, 8, 4], [2, 1, 4, 8],
            [8, 1, 2, 4], [1, 8, 2, 4],
            [1, 2, 8, 4], [1, 2, 4, 8],
            [8, 1, 4, 2], [1, 8, 4, 2],
            [1, 4, 8, 2], [1, 4, 2, 8],
            [8, 2, 4, 1], [2, 8, 4, 1],
            [2, 4, 8, 1], [2, 4, 1, 8],
            [8, 4, 2, 1], [4, 8, 2, 1],
            [4, 2, 8, 1], [4, 2, 1, 8],
            [8, 4, 1, 2], [4, 8, 1, 2],
            [4, 1, 8, 2], [4, 1, 2, 8]
        ]

    def test_03(self):
        assert permutations([]) == [[]]


if __name__ == "__main__":
    unittest.main()
