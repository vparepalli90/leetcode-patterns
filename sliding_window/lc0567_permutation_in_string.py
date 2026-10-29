"""
LC 567 - Permutation in String (Medium)
https://leetcode.com/problems/permutation-in-string/

Pattern: fixed-size sliding window + hash map counts
Idea:    A permutation of s1 is an anagram of s1, always len(s1) long -> fixed window.
         Build, check, then slide: add the entering char, remove the leaving char
         (delete the key when its count hits 0 so dict equality works), check.
         Deleting and comparing are separate jobs: two `if`s, not `if/elif`.
Time:    O(n) - comparing dicts of at most 26 letters is constant
Space:   O(1)
"""


def check_inclusion(s1: str, s2: str) -> bool:
    k = len(s1)
    if k > len(s2):
        return False

    dic1 = {}
    for c in s1:
        dic1[c] = dic1.get(c, 0) + 1

    dic2 = {}
    for c in s2[:k]:
        dic2[c] = dic2.get(c, 0) + 1
    if dic2 == dic1:
        return True

    for i in range(k, len(s2)):
        entering = s2[i]
        dic2[entering] = dic2.get(entering, 0) + 1

        leaving = s2[i - k]
        dic2[leaving] -= 1
        if dic2[leaving] == 0:
            del dic2[leaving]

        if dic2 == dic1:
            return True

    return False


if __name__ == "__main__":
    assert check_inclusion("ab", "eidbaooo") is True
    assert check_inclusion("ab", "eidboaoo") is False
    assert check_inclusion("abc", "ab") is False
    assert check_inclusion("ab", "cab") is True
    print("lc0567 check_inclusion: all tests passed")
