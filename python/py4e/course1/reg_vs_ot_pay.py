hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
if h <= 40:
    pay = str(h * r)
    print("Standard pay: "+ pay)
else:
    reghours = 40 * r
    othours = h - 40
    pay = reghours + othours * r * 1.5
    print("Total pay: "+ str(pay))    