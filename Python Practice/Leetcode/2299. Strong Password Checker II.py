
"""

A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.



Example 1:

Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.
Example 2:

Input: password = "Me+You--IsMyDream"
Output: false
Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.
Example 3:

Input: password = "1aB!"
Output: false
Explanation: The password does not meet the length requirement. Therefore, we return false.

"""



def strongPasswordCheckerII(self, password: str) -> bool:
    if len(password) < 8:
        return False
    elif not any(x.isupper() for x in password):
        return False
    elif not any(x.islower() for x in password):
        return False
    elif not any(x in ["0","1","2","3","4","5","6","7","8","9"] for x in password):
        return False
    elif not any(x in "!@#$%^&*()-+" for x in password):
        return False
    else:
        for x in range(len(password)-1):
            if password[x] == password[x+1]:
                return False
    return True


print(strongPasswordCheckerII("a1A!A!A!"))



