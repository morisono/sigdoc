import numpy as np

# ダミーデータを生成
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# 最小二乗法で回帰係数を計算
X_b = np.c_[np.ones((100, 1)), X]  # バイアス項を追加
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

print("OLSによる回帰係数:")
print(theta_best)
