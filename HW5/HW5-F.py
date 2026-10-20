# 讀取輸入的正整數 n
n = int(input())

# 使用巢狀 for 迴圈逐列與逐欄處理
for i in range(1, n + 1):
    row_str = ""
    for j in range(1, n + 1):
        # 計算相乘數值，並以欄寬 4 靠右對齊格式化
        row_str += f"{i * j:4d}"
    print(row_str)