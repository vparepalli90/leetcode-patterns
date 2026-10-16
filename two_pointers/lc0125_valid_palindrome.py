"""
LC 125 - Valid Palindrome (Easy)
https://leetcode.com/problems/valid-palindrome/

Pattern: two pointers, opposite ends
Idea:    4 situations each step:
           left is junk  -> move left only
           right is junk -> move right only
           real but different (lowercase) -> return False
           real and same -> move both inward
         Only `return False` lives inside the loop; `return True` only after it.
Time:    O(n)   Space: O(1)  (vs. O(n) for the cleaned-copy shortcut)
"""


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("0P") is False
    print("lc0125 is_palindrome: all tests passed")
