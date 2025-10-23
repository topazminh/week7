# Ví dụ: chọn nguyên liệu sao cho chi phí thấp mà năng suất cao nhất
def optimize_production(costs, profits, budget):
    n = len(costs)
    dp = [[0]*(budget+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for b in range(1, budget+1):
            if costs[i-1] <= b:
                dp[i][b] = max(dp[i-1][b], dp[i-1][b-costs[i-1]] + profits[i-1])
            else:
                dp[i][b] = dp[i-1][b]
    return dp[n][budget]

costs = [1, 3, 5, 7]
profits = [2, 4, 6, 8]
budget = 10
print("Lợi nhuận tối đa:", optimize_production(costs, profits, budget))
