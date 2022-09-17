coords = [ list(map(int, input().split(' '))) for _ in range(3)]

l1 = [coords[1][0] - coords[0][0], coords[1][1] - coords[0][1]]
l2 = [coords[2][0] - coords[1][0], coords[2][1] - coords[1][1]]

res = l1[0] * l2[1] - l1[1] * l2[0]
res = int(res / abs(res) if res != 0 else 0)

print(res)