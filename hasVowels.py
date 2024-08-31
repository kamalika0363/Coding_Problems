"""
Complete the hasVowels function in the editor below.
It must return an array of integers that represent the result of each query in the order given.
hasVowels has the following parameters.
strArr string[]: an array of n strings
query string[]: an array of q strings,
each of which describes an interval l-r using integers delimited by a dash
"""


def hasVowels(strArr, query):
    vowels = 'aeiou'
    result = []
    for q in query:
        l, r = map(int, q.split('-'))
        count = 0
        for i in range(l - 1, r):
            count += sum(1 for char in strArr[i] if char.lower() in vowels)
        result.append(count)
    return result


strArr = ["hello", "world", "python", "programming", "java"]
query = ["1-3", "2-4", "1-5"]
result = hasVowels(strArr, query)
print("Result: ", result)
