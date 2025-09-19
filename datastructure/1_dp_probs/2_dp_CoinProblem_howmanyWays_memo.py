"""
Given a set of coin values coins = { c1,c2 ... ck} amd a
target sum money m, in how many ways can we form the sum m using these coins?


"""

from collections import defaultdict

def how_many_ways(m, coins):
    memo = defaultdict(lambda _:0)
    print(memo)
    memo[0] = 1
    print(memo[0])
    for i in range(1, m+1):
        memo[i] = 0

        for coin in coins:
            subproblem = i-coin
            if subproblem < 0:
                continue

            memo[i] = memo[i] + memo[subproblem]

    return memo[m]


print(how_many_ways(5, [1,4,5]))
