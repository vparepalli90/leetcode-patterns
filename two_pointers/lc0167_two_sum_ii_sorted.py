"""
LC 167 - Two Sum II - Input Array Is Sorted (Medium)
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Pattern: two pointers, opposite ends
Idea:    Sorted input tells us which way to move:
         sum too small -> left += 1; too big -> right -= 1; equal -> found.
         Answer is 1-indexed.
Time:    O(n)   Space: O(1)
vs. LC 1: sorting lets two pointers replace the O(n) hash map.
"""


def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []


if __name__ == "__main__":
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_sorted([2, 3, 4], 6) == [1, 3]
    assert two_sum_sorted([-1, 0], -1) == [1, 2]
    print("lc0167 two_sum_sorted: all tests passed")
