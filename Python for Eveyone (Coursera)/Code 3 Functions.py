def Myfunction(parameter):
    if   parameter < 10:
        print(parameter,"is Below than 10")
    elif parameter > 10:
        print(parameter,"is bigger than 10")
    else:
        print(parameter,"is equal to 10")

Myfunction(3)

Myfunction(15)

Myfunction(10)


def calculatepay(hrs,pay):
    hrs = float(hrs)
    pay = float(pay)
    if hrs > 40:
        st = hrs*pay
        Ovt = (hrs-40)*(pay*1.5)
        p = st + Ovt
    else:
        st = hrs * pay
    return st

print(calculatepay(41,8))

print(calculatepay(45,8))

