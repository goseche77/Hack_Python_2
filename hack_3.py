"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    replace_dict = str.maketrans({
        'a': '@',
        'e': '3',
        'i': '¡',
        'o': '0',
        'u': 'v'
    })
    
    hacked_string = s.translate(replace_dict)
    if len(hacked_string) > 0:
        hacked_string = hacked_string[0].upper() + hacked_string[1:]
    
    if len(hacked_string) > 1 and s[-1].lower() not in "aeiou":
        hacked_string = hacked_string[:-1] + hacked_string[-1].upper()

    return hacked_string
    
