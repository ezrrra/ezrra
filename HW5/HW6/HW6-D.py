import sys


def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    # 1. 讀取商品種類數 N
    N = int(lines[0].strip())

    names = []
    prices = []
    quantities = []
    subtotals = []

    # 2. 依序讀取每項商品的名稱、單價、數量
    for i in range(1, N + 1):
        parts = lines[i].strip().split()
        name = parts[0]
        price = int(parts[1])
        quantity = int(parts[2])

        names.append(name)
        prices.append(price)
        quantities.append(quantity)

        # 計算優惠後小計：每買 3 件其中 1 件免費（即付費件數 = q - q // 3）
        paid_qty = quantity - (quantity // 3)
        subtotal = paid_qty * price
        subtotals.append(subtotal)

    # 3. 輸出前 N 行：商品名稱及優惠後小計
    for i in range(N):
        print(f"{names[i]} {subtotals[i]}")

    # 4. 計算合計並處理滿 1000 折 100
    total_sum = sum(subtotals)
    if total_sum >= 1000:
        final_total = total_sum - 100
    else:
        final_total = total_sum

    print(f"TOTAL {final_total}")

    # 5. 找出花費最多的商品（最高小計以整單折扣之前的小計比較；同額選輸入較早者）
    max_sub = -1
    top_name = ""
    for i in range(N):
        if subtotals[i] > max_sub:
            max_sub = subtotals[i]
            top_name = names[i]

    print(f"TOP {top_name}")


if __name__ == "__main__":
    solve()