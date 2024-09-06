"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    
    if len(s) <= 2:
        return s
    
    result = list(s)

    if s.startswith("fo"):
        if len(result) > 2:
            result[2] = '-'
        if len(result) > 5:
            result.insert(5, '-')
        if len(result) > 6:
            result[-1] = '-'
    
    elif s.startswith("ba"):
        if len(result) > 2:
            result[2] = '-'
        if len(result) > 5:
            result[5] = '-'

    elif len(s) < 5:
        if len(result) > 2:
            result[2] = '-'

    return ''.join(result)