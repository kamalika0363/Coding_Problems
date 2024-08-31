"""
There is a lottery with n coupons and n people take part in it. Each person picks exactly one coupon. Coupons are
numbered consecutively from 1 to n.
A lottery winner is any person who owns a coupon where the sum of the digits on the coupon is equal to s.
If there are multiple winners, the prize is split equally among them.
Determine how many values of s there are where there is at least one winner and the prize is split among the
largest group of people.
Example
n = 12
The list of coupon numbers generated from 1 to n is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].
The sums of the digits are [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3].
The largest number of winners is 2 which occurs for coupons
[1, 10], [2, 11], and [3, 12].
The maximum possible number of winners occurs for any of these 3 possible values of s,so 3 is the answer.
Function Description Complete the function lotteryCoupons in the editor.
lotteryCoupons has the following parameter(s): int n: the maximum coupon number
Returns int: the number of ways to choose s
"""


def lotteryCoupons(n):
    digit_sum = {}
    for i in range(1, n + 1):
        num = sum(int(digit) for digit in str(i))
        if num in digit_sum:
            digit_sum[num] += 1
        else:
            digit_sum[num] = 1

    max_winners = max(digit_sum.values())
    return sum(1 for count in digit_sum.values() if count == max_winners)


def main():
    n = int(input("Enter the maximum coupon number: "))
    result = lotteryCoupons(n)
    print("The number of ways to choose s is:", result)


if __name__ == "__main__":
    main()

# Test case:
# Enter the maximum coupon number: 12
# The number of ways to choose s is: 3
