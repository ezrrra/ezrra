import sys


def main():
  total = 0
  # 使用 sys.stdin 讀取所有輸入行
  for line in sys.stdin:
    num = int(line.strip())
    if num == 0:
      break
    total += num
  print(total)


if __name__ == "__main__":
  main()