"""
LC 1 - Two Sum (Easy)
https://leetcode.com/problems/two-sum/

Pattern: hash map lookup
Idea:    For each number, the partner we need is target - num.
         Check if we've already seen it (O(1) dict lookup); if not, store num -> index.
         Check BEFORE inserting so a number can't pair with itself.
Time:    O(n)   Space: O(n)   ("trading space for time")
Brute force: nested loops, O(n^2) time, O(1) space.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # number -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("lc0001 two_sum: all tests passed")
