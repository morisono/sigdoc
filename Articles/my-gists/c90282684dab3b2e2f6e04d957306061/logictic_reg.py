# 必要なライブラリのインポート
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def logistic_regression_classifier(X, y, test_size=0.2, random_state=42, learning_rate=0.1, n_iterations=1000):
    """
    ロジスティック回帰モデルをトレーニングし、性能を評価する関数。

    Parameters:
    X (array-like): 特徴行列
    y (array-like): ターゲットラベル
    test_size (float): テストデータの割合
    random_state (int): 乱数のシード
    learning_rate (float): 学習率
    n_iterations (int): 反復回数

    Returns:
    accuracy (float): 正解率
    report (str): 分類レポート
    """

    # データの分割
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # ロジスティック回帰モデルの作成と学習
    model = LogisticRegression(max_iter=n_iterations, C=1/learning_rate)
    model.fit(X_train, y_train)

    # テストデータで予測
    y_pred = model.predict(X_test)

    # モデルの評価
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    return accuracy, report

# ダミーデータの生成
np.random.seed(0)
X = np.random.randn(100, 2)
y = (X[:, 0] + 2 * X[:, 1] > 1).astype(int)

# ロジスティック回帰モデルの性能評価
accuracy, report = logistic_regression_classifier(X, y)

print("正解率:", accuracy)
print("分類レポート:\n", report)
