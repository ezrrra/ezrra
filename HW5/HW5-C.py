# 讀取輸入的整數 n
n = int(input())

# 初始化階乘結果為 1
result = 1

# 使用 for 迴圈從 1 乘到 n
for i in range(1, n + 1):
    result *= i

# 輸出結果
print(result)