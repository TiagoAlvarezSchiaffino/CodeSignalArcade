"""
Ticket numbers usually consist of an even number of digits.
A ticket number is considered lucky if the sum of the first half of the digits
is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
"""

"""
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

A ticket number represented as a positive integer with an even number of digits.

Guaranteed constraints:
10 ≤ n < 106.

[output] boolean

true if n is a lucky ticket number, false otherwise.
"""

def solution(n):
    str_n = str(n)

    length = len(str_n)

    if length % 2 != 0:
        return False

    half_length = length // 2
    first_half = str_n[:half_length]
    second_half = str_n[half_length:]

    sum_first_half = sum(int(digit) for digit in first_half)
    sum_second_half = sum(int(digit) for digit in second_half)

    return sum_first_half == sum_second_half
