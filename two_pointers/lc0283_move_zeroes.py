"""
LC 283 - Move Zeroes (Easy)
https://leetcode.com/problems/move-zeroes/

Pattern: two pointers, fast/slow (reader/writer)
Idea:    Keep rule: nums[fast] != 0. Both pointers start at 0 (the first element may be zero).
         Swap instead of copy so the zeros end up at the back in one pass.
         Follow-up: skip the swap when slow == fast to minimize writes.
Time:    O(n)   Space: O(1)
"""


def move_zeroes(nums: list[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            if slow != fast:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]; move_zeroes(nums); assert nums == [1, 3, 12, 0, 0]
    nums = [0];              move_zeroes(nums); assert nums == [0]
    nums = [1, 2, 3];        move_zeroes(nums); assert nums == [1, 2, 3]
    nums = [0, 1];           move_zeroes(nums); assert nums == [1, 0]
    print("lc0283 move_zeroes: all tests passed")
