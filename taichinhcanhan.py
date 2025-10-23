# Tối ưu hóa số tiền tiết kiệm qua n tháng
def financial_plan(income, expense):
    n = len(income)
    dp = [0]*(n+1)

    for i in range(1, n+1):
        dp[i] = max(dp[i-1], dp[i-1] + income[i-1] - expense[i-1])
    return dp[n]

income = [1000, 1200, 800, 1500]
expense = [800, 1100, 900, 1000]
print("Tiền tiết kiệm tối đa:", financial_plan(income, expense))
