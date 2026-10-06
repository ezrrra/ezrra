# 讀取矩陣 A 的第一列 a, b 與第二列 c, d
a, b = map(float, input().split())
c, d = map(float, input().split())

# 計算行列式 det
det = a * d - b * c

# 計算反矩陣四個元素
inv_a = d / det
inv_b = -b / det
inv_c = -c / det
inv_d = a / det

# 輸出結果（共 2 行，每行 2 個實數，保留小數點後 4 位）
print(f"{inv_a:.4f} {inv_b:.4f}")
print(f"{inv_c:.4f} {inv_d:.4f}")