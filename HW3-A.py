N = int(input())
a = N // 100         
b = (N // 10) % 10  
c = N % 10           
total_sum = a + b + c
product = a * b * c
reversed_num = c * 100 + b * 10 + a
print(f"{a} {b} {c}")
print(total_sum)
print(product)
print(reversed_num)