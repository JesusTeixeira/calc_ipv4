x = 0
y = 10

while x >= 0 and x <= 10:
    print(x, y)
    x += 1
    y -= 1

print('========================================')

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)