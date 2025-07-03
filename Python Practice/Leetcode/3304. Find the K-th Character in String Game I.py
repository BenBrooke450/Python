






import string
def kthCharacter(k: int) -> str:
    lowercase_alphabet = string.ascii_lowercase
    string_a = "a"
    i = 0
    t = ""
    while k >= len(string_a):
        where_l = (lowercase_alphabet.find(string_a[i]) % 27) + 1
        t = t + lowercase_alphabet[where_l]
        print(lowercase_alphabet[where_l])
        print(string_a,t,len(string_a))
        if i == len(string_a) - 1:
            string_a = string_a + t
            t = ""
            i = 0
        else:
            i = i + 1
    return string_a[k-1]

print(kthCharacter(5))


