smallest = None
print("Before")

for value in [9, 42, 23, 455, 64, 35644, 33, 31, 3, 43, 89, 79,] :
    if smallest is None :
        smallest = value
        print("smallest", smallest)
    elif value < smallest :
        smallest = value
    print(smallest, value)
print("After", smallest)
