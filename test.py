sum = 2
for i in range(2, 101):
    if i == 3:
        sum += 3
    if i == 5:
        sum += 5
    if i == 7:
        sum += 7
    if i % 2 != 0:
        if i % 3 != 0:
            if i % 5 != 0:
                if i % 7 != 0:
                    sum += i

print(sum)
