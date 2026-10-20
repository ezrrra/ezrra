# 讀取輸入的一行資料，包含 a, b, k
input_data = input().split()
a = int(input_data[0])
b = int(input_data[1])
k = int(input_data[2])

count = 0
total = 0

# 使用 for 迴圈走訪區間 [a, b] 內的每一個數字
for i in range(a, b + 1):
    if i % k == 0:
        count += 1
        total += i

# 輸出結果：個數與總和，以空白分隔
print(count, total)