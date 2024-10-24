import numpy as np

# ダミーデータを生成
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# 最急降下法で回帰係数を計算
eta = 0.1  # 学習率
n_iterations = 1000  # 反復回数
m = 100  # サンプル数

theta = np.random.randn(2, 1)  # 初期パラメータ

for iteration in range(n_iterations):
    gradients = 2/m * X.T.dot(X.dot(theta) - y)
    theta = theta - eta * gradients

print("最急降下法による回帰係数:")
print(theta)
