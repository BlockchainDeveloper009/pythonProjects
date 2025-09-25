from utils.metrics_time_helper import  TimeHelper

def knapsack(W, val, wt):
    n = len(wt)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(n + 1):
        for j in range(W + 1):

            # If there is no item or the knapsack's capacity is 0
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                pick = 0

                # Pick ith item if it does not exceed the capacity of knapsack
                if wt[i - 1] <= j:
                    pick = val[i - 1] + dp[i - 1][j - wt[i - 1]]

                # Don't pick the ith item
                notPick = dp[i - 1][j]

                dp[i][j] = max(pick, notPick)

    return dp[n][W]


if __name__ == "__main__":
    val = [1, 2, 3]
    wt = [4, 5, 1]
    W = 4
    mt = TimeHelper()
    print(knapsack(W, val, wt))
    mt.print_time_taken("knapsack_optimized", mt.start_time)


"""
3
Measuring performance of knapsack_optimized approach...
knapsack_optimized duration: 0.000210 seconds

Process finished with exit code 0
"""
