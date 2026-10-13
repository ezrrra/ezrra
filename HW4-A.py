# 讀取輸入的一行，並將其以空白分隔轉為兩個整數 a 與 b
a, b = map(int, input().split())

# 依照題目規則判斷大小並輸出指定字串
if a > b:
    print("Greater")
elif a < b:
    print("Less")
else:
    print("Equal")