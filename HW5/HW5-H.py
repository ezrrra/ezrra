import sys


def main():
  # 讀取輸入的非負整數 n
  line = sys.stdin.readline()
  if not line:
    return
  n = int(line.strip())

  total = 0
  # 使用 while 迴圈與運算子逐位取出相加
  while n > 0:
    total += n % 10
    n = n // 10

  print(total)


if __name__ == "__main__":
  main()