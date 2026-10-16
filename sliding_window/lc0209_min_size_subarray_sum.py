"""
LC 209 - Minimum Size Subarray Sum (Medium)
https://leetcode.com/problems/minimum-size-subarray-sum/

Pattern: variable-size sliding window (shortest)
Idea:    Expand right. WHILE window_sum >= target the window is valid:
         RECORD its length first, THEN shrink from the left.
         Start best at infinity (looking for a min); if it never changes, return 0.
Time:    O(n)   Space: O(1)
"""


def min_sub_array_len(target: int, nums: list[int]) -> int:
    window_sum = 0
    best = float("inf")
    left = 0
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            best = min(best, right - left + 1)   # record while valid...
            window_sum -= nums[left]             # ...then shrink
            left += 1
    return 0 if best == float("inf") else best


if __name__ == "__main__":
    assert min_sub_array_len(7, [2, 3, 1, 2, 4, 3]) == 2
    assert min_sub_array_len(4, [1, 4, 4]) == 1
    assert min_sub_array_len(11, [1, 1, 1, 1]) == 0
    print("lc0209 min_sub_array_len: all tests passed")
