import sys


def solve():
    # 讀取一整行原始帳號（保留結尾的換行符號以便後續處理，或使用 sys.stdin.readline()）
    line = sys.stdin.readline()
    if not line:
        return
    # 去除結尾的換行符號 \n 或 \r\n
    raw_s = line.rstrip("\r\n")

    # 1. 依序移除頭尾的半形空白
    s = raw_s.strip(" ")

    # 2. 把英文字母轉成小寫
    s = s.lower()

    # 3. 將中間每一段連續半形空白改成一個底線。原本的底線與符號均保留。
    # 利用 split() 預設會以任意連續空白進行切割
    parts = s.split()
    if not parts:
        formatted = ""
    else:
        formatted = "_".join(parts)

    # 4. 輸出第一行：整理後的帳號（若為空字串，第一行為空白行）
    print(formatted)

    # 5. 檢查是否合法
    # 合法條件：
    # - 長度為 6 至 16
    # - 每個字元只能是 a 至 z、0 至 9 或底線
    # - 開頭可為數字或底線 (實際上依題意，a-z, 0-9, _ 只要開頭不是其他非法字元即可，此處合法字元包含數字與底線)
    is_valid = True
    length = len(formatted)

    if length < 6 or length > 16:
        is_valid = False
    else:
        for char in formatted:
            # 檢查字元是否為 a-z, 0-9 或底線
            if not (
                ("a" <= char <= "z") or ("0" <= char <= "9") or (char == "_")
            ):
                is_valid = False
                break

    # 6. 輸出第二行：合法時輸出 VALID，否則輸出 INVALID
    if is_valid:
        print("VALID")
    else:
        print("INVALID")


if __name__ == "__main__":
    solve()