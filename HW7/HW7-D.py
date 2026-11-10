
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def simplify_recipe(tea, milk, syrup):
    g = gcd(tea, milk)
    g = gcd(g, syrup)

    if g == 0:
        return tea, milk, syrup

    return tea // g, milk // g, syrup // g


N = int(input())

for i in range(N):
    tea, milk, syrup = map(int, input().split())
    a, b, c = simplify_recipe(tea, milk, syrup)
    print(a, b, c)
