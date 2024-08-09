def max_sum_increasing_subsequence(arr):
    n = len(arr)
    if n == 0:
        return 0, []

    max_sum = arr[:]
    sequence = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and max_sum[i] < max_sum[j] + arr[i]:
                max_sum[i] = max_sum[j] + arr[i]
                sequence[i] = j

    max_index = 0
    for i in range(1, n):
        if max_sum[i] > max_sum[max_index]:
            max_index = i

    subsequence = []
    current_index = max_index
    while current_index != -1:
        subsequence.append(arr[current_index])
        current_index = sequence[current_index]

    subsequence.reverse()

    return max_sum[max_index], subsequence


arr = [10, 20, 30, 50, 60, 80]
max_sum, seq = max_sum_increasing_subsequence(arr)
print("Максимальна сума:", max_sum)
print("Підпослідовність:", seq)
