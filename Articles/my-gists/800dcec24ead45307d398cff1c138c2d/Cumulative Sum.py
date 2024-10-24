N = 5
array = [1, 2, 3, 4, 5]
prefix_sum = [0] * (N + 1)

for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + array[i]
