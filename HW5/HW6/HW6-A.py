def main():
    # 讀取一行四個整數 B, N, R, C
    # 依序代表原餐費、人數、服務費百分比及折價券金額
    line = input().strip()
    if not line:
        return
    B, N, R, C = map(int, line.split())

    # 計算服務費：原餐費乘以服務費百分比，不足 1 元的部分捨去 (使用整數除法)
    service_fee = (B * R) // 100

    # 應付總額 = 原餐費 + 服務費 - 折價券金額；若小於 0，改為 0
    total = B + service_fee - C
    if total < 0:
        total = 0

    # 計算每人基礎應付金額 q 及餘數 b
    # q 為 T 除以 N 的整數商，b 為餘數 (即有 b 人需多付 1 元)
    q = total // N
    b = total % N
    a = N - b

    # 輸出三行格式
    print(total)
    print(f"{q} {a}")
    print(f"{q + 1} {b}")


if __name__ == "__main__":
    main()