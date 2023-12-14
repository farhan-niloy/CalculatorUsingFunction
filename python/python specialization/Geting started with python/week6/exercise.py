def computepay(h, r):
    if (h < 40):
        return h * r
    elif (h > 40):
        return ((h - 40) * r * 1.5) + (40 * 10.50)
    else:
        printf("invalid entry")


hrs = input("Enter Hours:")
fhrs = float(hrs)
rate = input("Enter Hourly Rate:")
frate = float(rate)

p = computepay(fhrs, frate)
print("Pay", p)