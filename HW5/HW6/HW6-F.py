import sys


def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    # 1. 第一行為整數 K（向後移動的位置數）
    K = int(lines[0].strip())

    # 2. 第二行為原始訊息 S（可能包含空白，需完整讀取並保留）
    if len(lines) > 1:
        S = lines[1]
    else:
        S = ""

    result = []
    for char in S:
        code = ord(char)
        # 檢查是否為大寫英文字母 (A-Z)
        if 65 <= code <= 90:
            new_code = 65 + (code - 65 + K) % 26
            result.append(chr(new_code))
        # 檢查是否為小寫英文字母 (a-z)
        elif 97 <= code <= 122:
            new_code = 97 + (code - 97 + K) % 26
            result.append(chr(new_code))
        else:
            # 數字、空白與標點符號保持原樣
            result.append(char)

    # 輸出加密後的完整訊息（保留頭尾及連續空白）
    print("".join(result))


if __name__ == "__main__":
    solve()