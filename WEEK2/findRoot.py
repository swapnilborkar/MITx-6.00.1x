def findRoot2(x, power, epsilon):
    if x < 0 and power%2 == 0:
        return None
    # can't find even powered root of negative number
    low = min(0, x)
    high = max(0, x)
    ans = (high+low)/2.0
    while abs(ans**power - x) > epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
    print(ans)
    return ans


findRoot2(27, 3, .001)