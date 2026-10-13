# 讀取輸入的停車小時數 h
h = int(input())

# 計算總停車費
fee = 0

if h <= 2:
    fee = h * 30
elif h <= 5:
    fee = 2 * 30 + (h - 2) * 20
else:
    fee = 2 * 30 + 3 * 20 + (h - 5) * 10

# 輸出總費用
print(fee)