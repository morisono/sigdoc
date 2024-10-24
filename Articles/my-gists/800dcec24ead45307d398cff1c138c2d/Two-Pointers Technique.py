N = 6
array = [1, 2, 2, 3, 1, 2]
target_sum = 4

left, right = 0, 0
current_sum = 0

while right < N:
    current_sum += array[right]
    while current_sum > target_sum:
        current_sum -= array[left]
        left += 1
    if current_sum == target_sum:
        # 区間 [left, right] が条件を満たす
        # 何か処理を行う
    right += 1
