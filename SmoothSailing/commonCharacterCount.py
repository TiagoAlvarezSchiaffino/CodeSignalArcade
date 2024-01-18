"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""

"""
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string s1

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length < 15.

[input] string s2

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length < 15.

[output] integer
"""

def solution(s1, s2):
    common_characters = 0
    char_count_s1 = {}

    for char in s1:
        char_count_s1[char] = char_count_s1.get(char, 0) + 1

    for char in s2:
        if char in char_count_s1 and char_count_s1[char] > 0:
            common_characters += 1
            char_count_s1[char] -= 1

    return common_characters
