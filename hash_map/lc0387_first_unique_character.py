"""
LC 387 - First Unique Character in a String (Easy)
https://leetcode.com/problems/first-unique-character-in-a-string/

Pattern: count first, then scan in order
Idea:    Pass 1 counts every character. Pass 2 walks the ORIGINAL string and returns
         the first index whose count is 1. (Sorting would destroy the original order.)
Time:    O(n)   Space: O(1) for a fixed alphabet
"""


def first_unique_char(s: str) -> int:
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for index, char in enumerate(s):
        if counts[char] == 1:
            return index
    return -1


if __name__ == "__main__":
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1
    assert first_unique_char("") == -1
    print("lc0387 first_unique_char: all tests passed")
