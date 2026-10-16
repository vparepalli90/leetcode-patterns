# LeetCode Patterns

My interview prep, organized by **pattern** rather than by problem number. Each file has the solution, a short note on the approach and complexity, and its own `assert` tests.

## Run the tests

```bash
python run_all_tests.py          # every solution
python sliding_window/lc0209_min_size_subarray_sum.py   # one solution
```

## Progress

| Pattern | # | Problem | Difficulty | Time | Space |
|---|---|---|---|---|---|
| Hash map | 1 | [Two Sum](hash_map/lc0001_two_sum.py) | Easy | O(n) | O(n) |
| Hash map | 242 | [Valid Anagram](hash_map/lc0242_valid_anagram.py) | Easy | O(n) | O(1) |
| Hash map | 387 | [First Unique Character](hash_map/lc0387_first_unique_character.py) | Easy | O(n) | O(1) |
| Sliding window (fixed) | 643 | [Maximum Average Subarray I](sliding_window/lc0643_max_average_subarray.py) | Easy | O(n) | O(1) |
| Sliding window (variable) | 3 | [Longest Substring Without Repeating Characters](sliding_window/lc0003_longest_substring_no_repeat.py) | Medium | O(n) | O(k) |
| Sliding window (variable) | 209 | [Minimum Size Subarray Sum](sliding_window/lc0209_min_size_subarray_sum.py) | Medium | O(n) | O(1) |
| Sliding window (fixed) | 567 | [Permutation in String](sliding_window/lc0567_permutation_in_string.py) | Medium | O(n) | O(1) |
| Two pointers (opposite) | 344 | [Reverse String](two_pointers/lc0344_reverse_string.py) | Easy | O(n) | O(1) |
| Two pointers (opposite) | 125 | [Valid Palindrome](two_pointers/lc0125_valid_palindrome.py) | Easy | O(n) | O(1) |
| Two pointers (opposite) | 167 | [Two Sum II](two_pointers/lc0167_two_sum_ii_sorted.py) | Medium | O(n) | O(1) |
| Two pointers (fast/slow) | 26 | [Remove Duplicates from Sorted Array](two_pointers/lc0026_remove_duplicates_sorted.py) | Easy | O(n) | O(1) |
| Two pointers (fast/slow) | 283 | [Move Zeroes](two_pointers/lc0283_move_zeroes.py) | Easy | O(n) | O(1) |
| Stack | 20 | [Valid Parentheses](stack/lc0020_valid_parentheses.py) | Easy | O(n) | O(n) |

## How I pick a pattern

| If the problem says... | Reach for |
|---|---|
| count / frequency / "have I seen this?" | hash map |
| subarray / substring / consecutive + longest / shortest / max | sliding window |
| sorted + pair / target, or palindrome / reverse | two pointers, opposite ends |
| remove / move / filter **in place** | two pointers, fast/slow |
| matching pairs, most recent item first | stack |

## Sliding window questions I ask first

1. **Fixed or variable?** Is k given, or is there a condition?
2. **What's my state?** A running sum? Character counts?
3. **When is the window invalid?** That becomes the `while` condition.

## My bug checklist (from real mistakes)

- Is any `return` inside a loop that should come after it?
- Am I using an index where I need a value, or the reverse?
- Am I using the actual parameter name from the `def` line?
- Does `range(...)` reach the last element?
