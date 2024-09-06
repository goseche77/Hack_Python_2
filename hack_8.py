"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = []
    text_num = len(s)
    for i in range(text_num):
        if text_num % 2 != 0:
            result.append(f"{s[text_num - i - 1]}-{text_num - i}")
        else:
            result.append(f"{text_num - i}")
    
    return result
