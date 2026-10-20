import sys


def main():
  # 讀取輸入的非負整數 n
  line = sys.stdin.readline()
  if not line:
    return
  n = int(line.strip())

  reversed_num = 0
  # 使用 while 迴圈與數學運算將數字反轉
  while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n = n // 10

  print(reversed_num)


if __name__ == "__main__":
  main()