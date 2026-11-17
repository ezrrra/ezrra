inventory = {}
n = int(input())

for _ in range(n):
    item, stock = input().split()
    inventory[item] = int(stock)

sold = 0
rejected = 0
q = int(input())

for _ in range(q):
    command, item, qty = input().split()
    qty = int(qty)

    if command == "ADD":
        inventory[item] = inventory.get(item, 0) + qty
    elif command == "BUY":
        if item in inventory and inventory[item] >= qty:
            inventory[item] -= qty
            sold += qty
        else:
            rejected += 1

print(sold, rejected)

for item in sorted(inventory):
    print(item, inventory[item])