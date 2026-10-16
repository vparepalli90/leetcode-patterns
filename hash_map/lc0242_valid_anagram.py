"""
LC 242 - Valid Anagram (Easy)
https://leetcode.com/problems/valid-anagram/

Pattern: hash map counting
Idea:    Count letters of s1, then subtract with s2. Exit early if a count would go negative.
         Returning True at the end is safe because the lengths match and no count went negative.
Time:    O(n)   Space: O(k), O(1) for a fixed alphabet
Alternatives: two dictionaries (same big-O), sorted(s1) == sorted(s2) (O(n log n)).
"""


def valid_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    counts = {}
    for char in s1:
        counts[char] = counts.get(char, 0) + 1
    for char in s2:
        if counts.get(char, 0) == 0:
            return False
        counts[char] -= 1
    return True


if __name__ == "__main__":
    assert valid_anagram("listen", "silent") is True
    assert valid_anagram("agent", "angle") is False
    assert valid_anagram("", "") is True
    assert valid_anagram("aab", "abb") is False
    print("lc0242 valid_anagram: all tests passed")
