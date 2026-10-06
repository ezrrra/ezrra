# 讀取矩陣 A 的第一列 a, b 與第二列 c, d
a, b = map(int, input().split())
c, d = map(int, input().split())

# 讀取矩陣 B 的第一列 e, f 與第二列 g, h
e, f = map(int, input().split())
g, h = map(int, input().split())

# 計算矩陣乘積 C = A * B
c11 = a * e + b * g
c12 = a * f + b * h
c21 = c * e + d * g
c22 = c * f + d * h

# 輸出結果（共 2 行，每行 2 個整數，以空白分隔）
print(f"{c11} {c12}")
print(f"{c21} {c22}")