import sys


def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    # 1. 第一行輸入每日目標 G
    G = int(lines[0].strip())

    # 2. 第二行輸入七個以空白分隔的整數（以字串儲存並處理）
    steps_str_list = lines[1].strip().split()

    # 將字串轉換為整數串列
    steps = []
    for s in steps_str_list:
        steps.append(int(s))

    # 第一行輸出：總步數
    total_steps = sum(steps)
    print(total_steps)

    # 第二行輸出：達標天數
    achieve_days = 0
    for step in steps:
        if step >= G:
            achieve_days += 1
    print(achieve_days)

    # 第三行輸出：最高步數出現的所有日期（以空白分隔由小到大排列）
    max_step = max(steps)
    max_days = []
    for i in range(len(steps)):
        if steps[i] == max_step:
            max_days.append(
                str(i + 1)
            )  # 日期為第 1 至第 7 天，故索引 + 1
    print(" ".join(max_days))

    # 第四行輸出：最長連續達標天數；若沒有任何一天達標則為 0
    max_consecutive = 0
    current_consecutive = 0
    for step in steps:
        if step >= G:
            current_consecutive += 1
            if current_consecutive > max_consecutive:
                max_consecutive = current_consecutive
        else:
            current_consecutive = 0
    print(max_consecutive)


if __name__ == "__main__":
    solve()