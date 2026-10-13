# 讀取輸入的一個整數年份 y
y = int(input())

# 依照題目的閏年與平年判斷規則
if y % 400 == 0:
    print("Leap")
elif y % 100 == 0:
    print("Common")
elif y % 4 == 0:
    print("Leap")
else:
    print("Common")