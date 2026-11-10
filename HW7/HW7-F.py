
def best_total(prices, index, remaining):
    if index == len(prices):
        return 0

    skip = best_total(prices, index + 1, remaining)

    if prices[index] <= remaining:
        buy = prices[index] + best_total(
            prices, index + 1, remaining - prices[index]
        )
        return max(skip, buy)

    return skip


N, B = map(int, input().split())
prices = list(map(int, input().split()))

print(best_total(prices, 0, B))
