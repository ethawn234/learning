
Problem statement:
    Given a string `s`, find the length of the longest substring without repeating characters.

    Example 1:

        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

    Example 2:

        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

    Example 3:

        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    

    Constraints:

        0 <= s.length <= 5 * 104
        s consists of English letters, digits, symbols and spaces.


---


Initial Thoughts

    For unique constraints, the item in question must be compared against other items in the collection.
    Instead of a brute force approach (probably resulting in O(n^2)), I can immediately see that if I
    can keep a hash map of all unique values, and return that hash map.

    Hash Map approach:

        1. Like `Find Max Sub-Array`, I can keep a running count of the substring, re-starting the
            substring as needed.
            
        2. return substring length

    Takeaway(s):

        1. Since I see no big difference from finding the max subarray, I assume this problem has the same
            algorithmic approach.