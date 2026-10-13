# 讀取輸入的一行，並將其以空白分隔轉為三個整數 a、b、c
a, b, c = map(int, input().split())

# 將三邊長排序，確保 c 為最長邊（或者透過三角形兩邊和大於第三邊來判斷）
# 這裡將邊長放入串列並排序
sides = sorted([a, b, c])
x, y, z = sides[0], sides[1], sides[2]

# 判斷能否構成三角形 (任兩邊長之和嚴格大於第三邊)
if x + y <= z:
    print("Invalid")
elif x == y and y == z:
    print("Equilateral")
elif x == y or y == z:
    print("Isosceles")
else:
    print("Scalene")