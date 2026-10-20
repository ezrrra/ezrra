import sys


def main():
  # 讀取輸入的一行，包含 a, b
  line = sys.stdin.readline()
  if not line:
    return
  a, b = map(int, line.split())

  # 使用 while 迴圈實作輾轉相除法
  while b != 0:
    r = a % b
    a = b
    b = r

  print(a)


if __name__ == "__main__":
  main()