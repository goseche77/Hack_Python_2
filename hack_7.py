"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    if len(s) == 1:
        return s
    result = []
    n = 1
    for num in range(len(s)):
        if num % 2 == 0:
            result.append(str(n))
            n += 1
        else:
            result.append(n)
            n += 1
    return result
