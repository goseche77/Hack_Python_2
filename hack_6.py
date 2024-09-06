"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = []
    for n, num in enumerate(s):
        if n % 2 == 0:
            result.append(str(n + 1))
        else:
            result.append("-")
    if not result:
        result.append("0")
    return result
