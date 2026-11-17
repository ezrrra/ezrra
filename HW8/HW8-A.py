n = int(input())
playlist = input().split()  # 即使 n 是 0，也要讀取第二行
q = int(input())

for _ in range(q):
    parts = input().split()
    command = parts[0]

    if command == "ADD":
        playlist.append(parts[1])
    elif command == "REMOVE":
        song = parts[1]
        if song in playlist:
            playlist.remove(song)
    elif command == "REVERSE":
        playlist.reverse()

print(len(playlist))
print(" ".join(playlist) if playlist else "EMPTY")