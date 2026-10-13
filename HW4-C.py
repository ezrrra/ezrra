# 讀取輸入的一行，並將其以空白分隔轉為三個整數 a、b、c
a, b, c = map(int, input().split())

# 利用條件判斷找出最大值
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)