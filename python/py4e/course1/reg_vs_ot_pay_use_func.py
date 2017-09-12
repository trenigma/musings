def computepay(hrs, rt) :
    if hrs > 40 :
        reghrs = rt * hrs
        otp = (hrs - 40.0) * (rt * 0.5)
        guap = reghrs + otp
    else:
        guap = hrs * rt
    return guap

totalhrs = input("Enter Hours: ")
payrate = input("Enter Rate: ")
fh = float(totalhrs)
fr = float(payrate)

xp = computepay(fh,fr)

print(xp)