hrs = input("Enter Hours:")
pph = input("Enter rate per hour:")
h = float(hrs)
pr = float(pph)

over_hp = 1.5

if (h <= 40):
    payment = h * pr
    print(payment)

elif (h > 40):
    regular_hr = 40;
    regular_payment = 40 * pr
    over_hour = h - regular_hr
    over_hour_payment = over_hour * pr * over_hp
    total = regular_payment + over_hour_payment
    print(total)

else:
    print("Invalid entry")