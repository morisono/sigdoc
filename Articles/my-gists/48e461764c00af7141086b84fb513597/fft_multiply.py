import numpy as np

def fft_multiply(A, B):
    # 2つのポリノミアルの長さを決定し、FFTに適した次数の2のべき乗に拡張します。
    n = 1
    while n < len(A) + len(B):
        n *= 2

    # 2つのポリノミアルをFFTに適した形に拡張します。
    A = np.pad(A, (0, n - len(A)))
    B = np.pad(B, (0, n - len(B))

    # FFTを実行します。
    fft_A = np.fft.fft(A)
    fft_B = np.fft.fft(B)

    # 2つのポリノミアルの畳み込みを計算します。
    convolution = np.fft.ifft(fft_A * fft_B).real

    return convolution

# 2つのポリノミアルを定義します。
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# 2つのポリノミアルの畳み込みを計算します。
result = fft_multiply(A, B)

# 結果を表示します。
print("畳み込み結果:", result)
