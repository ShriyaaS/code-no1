def findDistinctNumbers(arr):
    frequency = {}
    
    
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    
    result = []
    for num, count in frequency.items():
        if count == 1:
            result.append(num)
    
    
    return sorted(result)

arr1 = [1, 2, 3, 2, 1, 4]
print(findDistinctNumbers(arr1))  # Output: [3, 4]

arr2 = [2, 1, 3, 2]
print(findDistinctNumbers(arr2))  # Output: [1, 3]
