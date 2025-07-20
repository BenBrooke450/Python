




def isStrictlyPalindromic(n: int) -> bool:

    for x in range(2,n-2):
        print(x)
        x = n%x
        print(x)
        binary = bin(x)
        print(binary)
        stripped_binary = binary.lstrip('-0b')
        print(stripped_binary,"---------")

print(isStrictlyPalindromic(9))


