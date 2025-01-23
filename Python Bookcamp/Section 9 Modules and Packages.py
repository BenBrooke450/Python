


####################################################################
#                      __name__ and "__main__"
####################################################################

#one.py

def func():
    print("FUNC() in one.py")

print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py has been imported")


#OR

if __name__ == "__main__":
    function()
    function2()


