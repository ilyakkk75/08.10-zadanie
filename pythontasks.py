n = int(input())
pokupki = {}

for _ in range(n):
    parts = input().split()
    name = parts[0]
    count = int(parts[-1])
    item = parts[1]
    if name not in pokupki:
        pokupki[name] = {}
    if item in pokupki[name]:
        pokupki[name][item] += count
    else:
        pokupki[name][item] = count

for name in pokupki:
    print(f"{name}:")
    for item, count in pokupki[name].items():
        print(f"{item} {count}")