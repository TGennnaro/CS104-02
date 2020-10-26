x=1
total=0
for x in range(11):
    if x==10:
        print(total)
        break
    else:
        total += x
        x += 1
