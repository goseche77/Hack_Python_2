"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = {}
    
    for foo, text in s.items():
        if text.endswith("ziman"):
            result[foo.capitalize()] = foo.capitalize() + "ziman"
            break
    return result


