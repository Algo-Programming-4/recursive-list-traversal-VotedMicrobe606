def sumList(lst, depth=1):
    totalSum, recursions, totalItems = 0, 0, 0
    maxDepth = depth
    for item in lst:
        totalItems += 1
        if isinstance(item, list):
            recursions += 1
            subSum, subRecursions, subItems, subDepth = sumList(item, depth + 1)
            totalSum += subSum
            recursions += subRecursions
            totalItems += subItems - 1
            maxDepth = max(maxDepth, subDepth)
        else:
            totalSum += item
    return totalSum, recursions, totalItems, maxDepth

lst = [[[3, [4]], 6], 7, [10, 3], [4, [5, [2, 8]]], 8]
result = sumList(lst)

print(f"Sum of numbers: {result[0]}")
print(f"Total recursions: {result[1]}")
print(f"Number of items: {result[2]}")
print(f"Deepest level of nesting: {result[3]}")
