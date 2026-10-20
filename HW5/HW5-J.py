import sys


def main():
  # 讀取輸入的一行，包含 s, d, t
  line = sys.stdin.readline()
  if not line:
    return
  s, d, t = map(int, line.split())

  days = 0
  # 使用 while 迴圈每日更新存款直到達到或超過目標
  while s < t:
    s += d
    days += 1

  print(days)


if __name__ == "__main__":
  main()