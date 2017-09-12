hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
#h = float(hrs)
#r = float(rate)
try:
    fh = float(hrs)
    fr = float(rate)
except:
    print("Error, please give numeric input")
    quit()

#print(fh, fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print(xp)
