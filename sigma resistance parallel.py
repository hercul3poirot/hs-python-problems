def parallel_resistance(lst):
    total = 0 
    for i in lst:
        total += 1/i
    actual = round(1/total,1)
    return actual

print(parallel_resistance([6,3,6]))