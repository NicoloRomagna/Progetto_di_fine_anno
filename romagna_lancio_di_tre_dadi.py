import random

dx = [1, 2, 3, 4, 5, 6] 

lanci = input("inserisci il numero di lanci: ")
lanci = int(lanci)
ndadi = 3
maxValori = ndadi*6
spazioEventi = 6**ndadi
r = list()
ptg = list()

i = 0
while i <= maxValori:
    r.append(0)
    ptg.append(0)
    i = i + 1
print(r)
print(ptg)

i = 1
while i <= 6:
    j = 1
    while j <= 6:
        k = 1
        while k <= 6:
            ds = i + j + k
            ptg[ds] = ptg[ds] + 1
            k = k + 1
        j = j + 1
    i = i + 1

print('------------------ spazio degli eventi ------------------')
i = 0
for item in ptg:
    print(i, item)
    i = i + 1
print("---------------------------------------------------------") 

i = 0
for item in ptg:
    ptg[i] = item/spazioEventi
    i = i + 1

i = 1
while i <= lanci:
    d1 = random.choice(dx)
    d2 = random.choice(dx)
    d3 = random.choice(dx)
    ds = d1 + d2 + d3
    r[ds] = r[ds] + 1
    i = i + 1

i = ndadi
while i <= maxValori:
    print(i, '   ', r[i], '   ', r[i]/lanci, '   ', ptg[i])
    i = i + 1