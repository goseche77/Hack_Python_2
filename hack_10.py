"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = []
    text = 1
    for item in s:
        dictionary = {}
        for key in item:
            dictionary[str(text)] = str(text + 1)
            text += 2
        result.append(dictionary)

    return result
