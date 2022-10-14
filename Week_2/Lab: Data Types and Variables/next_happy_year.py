year = int(input())
flag = False

while not flag:
    year += 1
    year_set = set()
    for i in range(len(str(year))):
        year_set.add(str(year)[i])

    flag = len(year_set) == len(str(year))
print(year)
