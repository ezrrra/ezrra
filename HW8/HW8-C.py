n, m = map(int, input().split())
club_a = set(input().split())
club_b = set(input().split())

results = (club_a & club_b, club_a | club_b, club_a - club_b, club_b - club_a)

for members in results:
    if members:
        print(" ".join(sorted(members)))
    else:
        print("NONE")