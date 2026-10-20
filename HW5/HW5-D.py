# 讀取人數 n 與成績清單
n = int(input())
scores = list(map(int, input().split()))

total_score = 0
pass_count = 0

# 使用 for 迴圈逐筆累加成績並計算及格人數
for score in scores:
    total_score += score
    if score >= 60:
        pass_count += 1

# 計算平均分數並以固定小數點格式保留小數後 2 位
average_score = total_score / n

# 輸出結果
print(f"{average_score:.2f}")
print(pass_count)