"""
    https://leetcode.com/problems/minimum-common-value/

You are given an array age[] of N Age of Members and array member[] of M Name, LastName, Age of Members.
The task is to find the name of the youngest missing member from the array age.
Note: 1) If all ages are provided then return null
      2) ages might not be in ascending order
      3) If more than one youngest member is missing
then return first occurrence of youngest member

Input: N = 5 age[] = {1,2,3,4,5}; M = 10 member[] = {'Ram,D,1', 'Dev,B,2', 'Adam,Jobs,3', 'Adam,Jobs,4', 'Ema,K,5',
'Leena,Jack,7', 'Patric,Queen,8', 'Liam,Jones,9', 'Riya,N,10', 'Dilip,K,22'}

Output: Leena
Explain: Youngest member's age not mentioned in age[] is 7 and Leena's age is 7.
"""


def find_youngest_missing_member(age, member):
    age_set = set(age)
    youngest_missing_member = None
    youngest_missing_age = float('inf')

    for member_info in member:
        name, last_name, member_age = member_info.split(',')
        member_age = int(member_age)

        if member_age not in age_set:
            if member_age < youngest_missing_age:
                youngest_missing_age = member_age
                youngest_missing_member = f"{name},{last_name},{member_age}"

    if youngest_missing_member is None:
        return None

    return youngest_missing_member


# Test cases
age1 = [1, 2, 3, 4, 5]
member1 = ['Ram,D,1', 'Dev,B,2', 'Adam,Jobs,3', 'Adam,Jobs,4', 'Ema,K,5', 'Leena,Jack,7', 'Patric,Queen,8',
           'Liam,Jones,9', 'Riya,N,10', 'Dilip,K,22']
print(find_youngest_missing_member(age1, member1))  # Output: Leena,Jack,7

age2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
member2 = ['Ram,D,1', 'Dev,B,2', 'Adam,Jobs,3', 'Adam,Jobs,4', 'Ema,K,5', 'Leena,Jack,6', 'Patric,Queen,7',
           'Liam,Jones,8', 'Riya,N,9', 'Dilip,K,10']
print(find_youngest_missing_member(age2, member2))  # Output: None

age3 = [1, 2, 3, 4, 5]
member3 = ['Ram,D,1', 'Dev,B,2', 'Adam,Jobs,3', 'Adam,Jobs,4', 'Ema,K,5', 'Leena,Jack,6', 'Patric,Queen,7',
           'Liam,Jones,8', 'Riya,N,9', 'Dilip,K,10', 'John,Doe,6']
print(find_youngest_missing_member(age3, member3))  # Output: Leena,Jack,6
