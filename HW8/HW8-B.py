n = int(input())
runners = []

for _ in range(n):
    name, time, penalty = input().split()
    runners.append((name, int(time), int(penalty)))

def race_key(runner):
    name, time, penalty = runner
    return (time + penalty, time, name)

for name, time, penalty in sorted(runners, key=race_key):
    print(name, time + penalty)