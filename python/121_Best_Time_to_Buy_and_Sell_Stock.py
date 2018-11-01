# 121. Best Time to Buy and Sell Stock


x = [7,6,5,4,3,1,3]


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    if not prices:
        return 0

    m = 0
    s = prices[0]

    for i in range(1, len(prices)):

        if prices[i] < s:
            s = prices[i]

        else:
            r = prices[i] - s
            if r > m:
                m = r

    return m


print(maxProfit(x))