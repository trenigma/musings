## Take numerical input, sum the inputs, tally the count 
## of inputs and give an average of the input values
num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue

    num = num + 1
    tot = tot + fval
print('All Done',tot,num,tot/num)