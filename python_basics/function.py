def computepay(hours , rate ) :
    if hours<=40:
        pay=hours*rate
        return pay
    elif hours>=40:
        payy=(40*rate)+(hours-40)*15.75
        return payy

sr=input("Enter the hours")
py=input("Enter the pay")
hours=float(sr)
rate=float(py)

x=computepay(hours,rate)
print("Pay" , x  )
