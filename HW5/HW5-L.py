import sys


def main():
  # 讀取輸入的金額 m
  line = sys.stdin.readline()
  if not line:
    return
  m = int(line.strip())

  coins = 0
  # 使用 while 迴圈依照規則每次扣除最大硬幣數
  while m > 0:
    if m >= 50:
      m -= 50
    elif m >= 10:
      m -= 10
    elif m >= 5:
      m -= 5
    else:
      m -= 1
    coins += 1

  print(coins)


if __name__ == "__main__":
  main()