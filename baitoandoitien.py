def count_ways_to_make_change(coins, S):
    dp = [0] * (S + 1)
    dp[0] = 1  # Có 1 cách để đổi 0 đồng

    # Duyệt từng loại tiền
    for coin in coins:
        for i in range(coin, S + 1):
            dp[i] += dp[i - coin]

    return dp[S]

# --- Ví dụ ---
coins = [1, 2, 5]   # mệnh giá tiền
S = 10              # số tiền cần đổi

print("Số cách đổi tiền:", count_ways_to_make_change(coins, S))
