rawNumbers = int(input("enter the raw number: "))

list = []

for raw in range(rawNumbers):
    list.append([])
    list[raw].append(1)
    
    for column in range(1, raw):
        list[raw].append(list[raw-1][column-1] + list[raw-1][column])
    if rawNumbers != 0 :
        list[raw].append(1)

print(list[raw])
