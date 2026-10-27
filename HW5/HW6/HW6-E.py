import sys


def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    idx = 0
    # 1. 讀取菜單筆數 M
    M = int(lines[idx].strip())
    idx += 1

    drink_names = []
    drink_prices = []
    drink_totals = []  # 累積各飲料的總杯數

    for _ in range(M):
        parts = lines[idx].strip().split()
        idx += 1
        drink_names.append(parts[0])
        drink_prices.append(int(parts[1]))
        drink_totals.append(0)

    # 2. 讀取訂單筆數 N
    N = int(lines[idx].strip())
    idx += 1

    student_names = []
    student_totals = []  # 累積各學生的應付金額

    for _ in range(N):
        parts = lines[idx].strip().split()
        idx += 1
        s_name = parts[0]
        d_name = parts[1]
        qty = int(parts[2])

        # 找出飲料在菜單中的索引以累積杯數
        d_idx = drink_names.index(d_name)
        drink_totals[d_idx] += qty

        # 檢查學生是否已經存在於 student_names 中
        if s_name not in student_names:
            student_names.append(s_name)
            student_totals.append(0)

        s_idx = student_names.index(s_name)

        # 計算本筆訂單的金額（先暫存數量，等整批計算單價時再乘）
        # 為了符合平行串列限制，我們可以用一個暫時的訂單串列記錄所有訂單
    # 重新讀取訂單來做後續計算比較安全
    # 我們回溯並重新解析訂單，或在第一次讀取時存入訂單串列：

    # 重新寫一個清晰的訂單處理流程：
    # 重新把剛才的讀取邏輯調整好：