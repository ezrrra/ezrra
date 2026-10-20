# 讀取輸入的非負整數 n
n = int(input())

# 處理 n = 0 的特殊情況
if n == 0:
    print(0)
else:
    a, b = 0, 1
    # 使用 for 迴圈逐步更新數值，計算至第 n 項
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)