# List Unpacking
months  = ["January", "February","March","April","May","June","July","August","September","October","November","December"]

print(months[0])

firstMonth, secondMonth, *restOfTheMonths = months
print(firstMonth)

# Iterate Over Lists
# for index, month in enumerate(months):
    # print(index)
    # print(month)
    # print(month[0], month[1])

for month in months:
    print(month)