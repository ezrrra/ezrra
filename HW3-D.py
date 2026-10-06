# 讀取第一行點 P (x1, y1)
x1, y1 = map(int, input().split())

# 讀取第二行點 Q (x2, y2)
x2, y2 = map(int, input().split())

# 計算兩點距離的平方
dx = x2 - x1
dy = y2 - y1
dist_sq = dx * dx + dy * dy

# 輸出結果
print(dist_sq)