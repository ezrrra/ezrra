n = int(input())
records = []

for _ in range(n):
    user, item = input().split()
    records.append((user, item))

target, k = input().split()
k = int(k)

purchases = {}
for user, item in records:
    if user not in purchases:
        purchases[user] = set()
    purchases[user].add(item)

target_items = purchases[target]
scores = {}

for user, items in purchases.items():
    if user == target:
        continue

    if items & target_items:
        for item in items - target_items:
            scores[item] = scores.get(item, 0) + 1

def ranking_key(entry):
    item, score = entry
    return (-score, item)

ranking = sorted(scores.items(), key=ranking_key)
r = min(k, len(ranking))

print(r)
for item, score in ranking[:r]:
    print(item, score)