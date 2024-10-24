N = 3
for i in range(1 << N):
    subset = [j for j in range(N) if (i & (1 << j)) != 0]
    # subsetにはi番目の組み合わせの要素が含まれる
