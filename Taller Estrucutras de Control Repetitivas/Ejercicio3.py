TotalSum = 0
for RangeNumber in range(98, 1004, 1):
    if (RangeNumber % 2 == 0):
        TotalSum += RangeNumber

print(f"Suma Total: {TotalSum}")