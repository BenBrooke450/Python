

"""
Your friend is typing his name into a keyboard.
    Sometimes, when typing a character c, the key
     might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.
    Return True if it is possible that it was your
     friends name, with some characters (possibly none)
      being long pressed.



Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.


"""


def isLongPressedName(name: str, typed: str) -> bool:
    if not all(x in name for x in set(typed)) or name[0] != typed[0] or len(typed) < len(name) or name[-1] != typed[-1]:
        return False

    t = 0
    y = 0
    while t < len(name):
        print(name[:t + 1], typed[:y + 1])
        if name[t] == typed[y]:
            t = t + 1
            y = y + 1
        elif name[t - 1] == typed[y]:
            y = y + 1
            if y + 1 == len(typed) and t + 1 != len(name):
                return False
        else:
            return False

    if not all(x == name[t - 1] for x in typed[y:]):
        return False

    return True


print(isLongPressedName(name = "alexes", typed = "aaleexxx"))






