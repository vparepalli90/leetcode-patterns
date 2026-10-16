"""
LC 3 - Longest Substring Without Repeating Characters (Medium)
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Pattern: variable-size sliding window (longest)
Idea:    Expand right every step. WHILE the new char is duplicated, shrink from the left.
         Then the window is valid: record its length (right - left + 1).
Time:    O(n) - each char enters once and leaves at most once
Space:   O(k) distinct characters
Variant: store each char's last-seen index and jump `left` past the duplicate
         (must check that the old index is still inside the window, e.g. "abba").
"""


def length_of_longest_substring(s: str) -> int:
    left = 0
    counts = {}
    best = 0
    for right in range(len(s)):
        char = s[right]
        counts[char] = counts.get(char, 0) + 1
        while counts[char] > 1:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("abba") == 2
    print("lc0003 length_of_longest_substring: all tests passed")
