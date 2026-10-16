"""
LC 344 - Reverse String (Easy)
https://leetcode.com/problems/reverse-string/

Pattern: two pointers, opposite ends
Idea:    Swap the ends and move both pointers toward the middle, in place.
Time:    O(n)   Space: O(1)
"""


def reverse_string(chars: list[str]) -> None:
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    chars = list("hello"); reverse_string(chars); assert chars == list("olleh")
    chars = list("ab");    reverse_string(chars); assert chars == list("ba")
    chars = [];            reverse_string(chars); assert chars == []
    print("lc0344 reverse_string: all tests passed")
