def maxArray(x):

    max_so_far = x[0]
    max_ending = x[0]

    for i in range(len(x)):

        max_ending = max(max_ending + x[i], x[i])
        max_so_far = max(max_so_far, max_ending)
        print(max_so_far)

    return max_so_far


print(maxArray(x))