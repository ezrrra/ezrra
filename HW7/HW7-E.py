
def count_ways(step, n, blocked, memo):
    if step > n:
        return 0

    if step in blocked:
        return 0

    if step == n:
        return 1

    if memo[step] != -1:
        return memo[step]

    ways = count_ways(step + 1, n, blocked, memo)
    ways += count_ways(step + 2, n, blocked, memo)

    memo[step] = ways
    return ways


N, K = map(int, input().split())

blocked = set()
if K > 0:
    blocked = set(map(int, input().split()))

memo = [-1] * (N + 1)

print(count_ways(0, N, blocked, memo))
