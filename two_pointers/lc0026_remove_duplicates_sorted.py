"""
LC 26 - Remove Duplicates from Sorted Array (Easy)
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Pattern: two pointers, fast/slow (reader/writer)
Idea:    fast reads every element; slow is the next write spot.
         The first element is always kept, so slow starts at 1.
         Keep nums[fast] if it differs from the last kept value, nums[slow - 1].
         Return k = slow; the judge checks the first k slots of nums.
Time:    O(n)   Space: O(1)
Edge:    assumes len(nums) >= 1 (LeetCode guarantees it).
"""


def remove_duplicates(nums: list[int]) -> int:
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow


if __name__ == "__main__":
    nums = [1, 1, 2]
    k = remove_duplicates(nums)
    assert k == 2 and nums[:k] == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    assert k == 5 and nums[:k] == [0, 1, 2, 3, 4]
    print("lc0026 remove_duplicates: all tests passed")
