import unittest

"""
--- Non adjacent sum ---
Write a function, non_adjacent_sum, that takes in a list of numbers as an argument. The function should return the maximum sum of non-adjacent items in the list. There is no limit on how many items can be taken into the sum as long as they are not adjacent.
"""


def non_adjacent_sum(nums):
    return calculate(nums, {})


def calculate(nums, memo):
    key = tuple(nums)
    if key in memo:
        return memo[key]
    if not nums:
        return 0

    cost = nums[0]
    left = nums[2:]
    right = nums[1:]

    left_result = calculate(left, memo)
    right_result = calculate(right, memo)

    memo[key] = max(cost + left_result, right_result)
    return memo[key]


class Test(unittest.TestCase):

    def test_00(self):
        nums = [2, 4, 5, 12, 7]
        non_adjacent_sum(nums) == 16

    def test_01(self):
        nums = [7, 5, 5, 12]
        non_adjacent_sum(nums) == 19

    def test_02(self):
        nums = [7, 5, 5, 12, 17, 29]
        non_adjacent_sum(nums) == 48

    def test_03(self):
        nums = [
            72, 62, 10, 6, 20, 19, 42,
            46, 24, 78, 30, 41, 75, 38,
            23, 28, 66, 55, 12, 17, 9,
            12, 3, 1, 19, 30, 50, 20
        ]
        non_adjacent_sum(nums) == 488

    def test_04(self):
        nums = [
            72, 62, 10, 6, 20, 19, 42, 46, 24, 78,
            30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
            83, 80, 56, 68, 6, 22, 56, 96, 77, 98,
            61, 20, 0, 76, 53, 74, 8, 22, 92, 37,
            30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
            72, 62, 10, 6, 20, 19, 42, 46, 24, 78,
            42
        ]
        non_adjacent_sum(nums) == 1465


if __name__ == "__main__":
    unittest.main()
