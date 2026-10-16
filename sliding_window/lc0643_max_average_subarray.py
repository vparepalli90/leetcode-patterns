"""
LC 643 - Maximum Average Subarray I (Easy)
https://leetcode.com/problems/maximum-average-subarray-i/

Pattern: fixed-size sliding window
Idea:    Build the first window's SUM, then slide: add the entering element,
         subtract the leaving one (index right - k). Divide by k only once at the end,
         since the window with the biggest sum also has the biggest average.
Time:    O(n)   Space: O(1)
Brute force: re-sum every window, O(n * k).
"""


def find_max_average(nums: list[int], k: int) -> float:
    window_sum = sum(nums[:k])
    best = window_sum
    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]
        best = max(best, window_sum)
    return best / k


if __name__ == "__main__":
    assert find_max_average([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert find_max_average([5], 1) == 5.0
    assert find_max_average([-1, -2, -3], 2) == -1.5
    print("lc0643 find_max_average: all tests passed")
