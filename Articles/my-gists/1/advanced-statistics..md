# ベリー・エッセンの定理 (Berry-Esseen Theorem)

ベリー・エッセンの定理は、サンプル平均の分布を正規分布で近似する際の近似誤差を、第三標準化モーメントに基づいて定量的に評価するものです。この定理によれば、サンプル平均と正規分布の累積分布関数の差は、サンプルサイズ $\(n\)$ が大きくなるにつれて、 $\(\frac{1}{\sqrt{n}}\)$ に比例する速さで収束します。この定理は、サンプルサイズが増加するにつれてサンプル平均がどのくらい速く正規分布に近づくかを評価するための見積もりを提供します。特に、小さなサンプルサイズでも、サンプル分布を正規分布で近似する正確性を評価するのに役立ちます。

数式で表すと、ベリー・エッセンの定理は以下のように表されます：

$$
sup_x \left| F_n(x) - \Phi(x) \right| \leq \frac{C \cdot \rho}{\sigma^3 \sqrt{n}}
$$

ここで、
- $\(F_n(x)\)$ はサンプル平均の累積分布関数,
- $\(\Phi(x)\)$ は標準正規分布の累積分布関数,
- $\(C\)$ は定数,
- $\(\rho\)$ は第三標準化モーメント,
- $\(\sigma\)$ は母集団の標準偏差,
- $\(n\)$ はサンプルサイズです。

# バーンスタインの不等式 (Bernstein Inequalities)

バーンスタインの不等式は、独立な有界な確率変数の和の尾部の振る舞いに関する増大の不等式の一群です。これは、有界な範囲を持つ確率変数に対して、チェルノフの境界やヘフディングの不等式よりも緊密な境界を提供します。バーンスタインの不等式は、確率変数の最大範囲だけでなく分散も考慮に入れ、収束の境界を改善します。

バーンスタインの不等式の一般的な形式は以下のように表されます：

$$
P\left(\left|\sum_{i=1}^n X_i\right| \geq t\right) \leq 2 \exp\left(-\frac{t^2}{2\left(\sum_{i=1}^n \sigma_i^2 + Bt/3\right)}\right)
$$

ここで、
- $\(X_i\)$ は独立な確率変数,
- $\(t\)$ は閾値,
- $\(\sigma_i^2\)$ は $\(X_i\)$ の分散,
- $\(B\)$ は確率変数 $\(X_i\)$ の上界です。

# ヘフディングの不等式 (Hoeffding's Inequality)

ヘフディングの不等式は、独立な確率変数の和がその期待値から大きく外れる確率の上限を提供する集中不等式です。有界な確率変数を扱う際に使用され、機械学習や統計解析で広く活用されています。ヘフディングの不等式は、サンプル平均がどのくらい速く期待値に収束するかを指数的に評価する境界を提供します。

ヘフディングの不等式は、以下のように表されます：

$$
P\left(\left|\frac{1}{n}\sum_{i=1}^n X_i - \mu\right| \geq t\right) \leq 2\exp\left(-\frac{2nt^2}{\sum_{i=1}^n (b_i-a_i)^2}\right)
$$

ここで、
- $\(X_i\)$ は独立な確率変数,
- $\(n\)$ はサンプルサイズ,
- $\(\mu\)$ は確率変数 $\(X_i\)$ の期待値,
- $\(a_i\)$ から $\(b_i\)$ は確率変数 $\(X_i\)$ の範囲です。
