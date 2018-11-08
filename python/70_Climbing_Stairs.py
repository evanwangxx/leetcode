# 70. Climbing Stairs

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """

    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        r = list(range(n))
        r[0] = 1
        r[1] = 2
        for i in range(2, n):
            r[i] = r[i-2] + r[i-1]

        return r[n-1]


for i in range(1, 10):
    print(i, ": ", climbStairs(i))
