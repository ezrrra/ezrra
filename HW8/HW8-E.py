n = int(input())
seen = set()
stamp_counts = {}

for _ in range(n):
    student, booth = input().split()
    record = (student, booth)

    if record not in seen:
        seen.add(record)
        stamp_counts[student] = stamp_counts.get(student, 0) + 1

def ranking_key(entry):
    student, count = entry
    return (-count, student)

ranking = sorted(stamp_counts.items(), key=ranking_key)

print(len(seen))
for student, count in ranking:
    print(student, count)