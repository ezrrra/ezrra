# 讀取輸入的一行，並將其以空白分隔轉為三個整數 a、b、c
a, b, c = map(int, input().split())

# 計算判別式 D = b^2 - 4 * a * c
D = b * b - 4 * a * c

# 依照判別式大小判斷實數根個數並輸出
if D > 0:
    print(2)
elif D == 0:
    print(1)
else:
    print(0)