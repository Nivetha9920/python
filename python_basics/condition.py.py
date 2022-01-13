hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hrs == 40:
    gross = (hrs * rate)
if hrs > 40:
    hrs = hrs - 40
    rate2 = rate * 1.5
    gross = (40 * rate)+(hrs * rate2)

print("Pay:",gross)
