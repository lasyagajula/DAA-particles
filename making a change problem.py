def making_change(coins, amount):
    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[amount]


coins = [1, 2, 5, 10]
amount = 18

result = making_change(coins, amount)

print("Minimum coins required:", result)
