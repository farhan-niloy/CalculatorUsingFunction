largest_so_far = -1

print("Before", largest_so_far)

for the_num in [9, 42, 23, 455, 64, 35644, 33, 31, 3, 43, 89, 79,] :
    if (largest_so_far < the_num):
        largest_so_far = the_num
    print(largest_so_far, the_num)

print("After", largest_so_far)