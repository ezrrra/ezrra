
def parking_fee(minutes):
    if minutes == 0:
        return 0

    fee = ((minutes + 29) // 30) * 30
    return min(fee, 200)


N = int(input())
minutes_list = list(map(int, input().split()))

fees = []

for minutes in minutes_list:
    fees.append(parking_fee(minutes))

print(*fees)
print(sum(fees))
