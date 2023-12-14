score = input("Enter Score: ")
fScore = float(score)
print(fScore)

if fScore < 0.0 or fScore > 1.0:
    print("You are out of range")
elif fScore >= 0.9:
    print("A")
elif fScore >= 0.8:
    print("B")
elif fScore >= 0.7:
    print("C")
elif fScore >= 0.6:
    print("D")
else:
    print("F")
