import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 1. グラフの横軸（平均μがとりうる範囲：95から105まで）を設定
mu_axis = np.linspace(95, 105, 500)

# 2. 検査前（事前分布）：平均100、分散1（標準偏差1）
prior = norm.pdf(mu_axis, loc=100, scale=1.0)

# 3. 検査後（事後分布）：平均100、分散0.5（標準偏差は √0.5 ≒ 0.707）
posterior = norm.pdf(mu_axis, loc=100, scale=np.sqrt(0.5))

# 4. グラフの描画
plt.figure(figsize=(8, 5))
plt.plot(mu_axis, prior, label="Prior: N(100, 1)", color="blue", linestyle="--")
plt.plot(mu_axis, posterior, label="Posterior: N(100, 0.5)", color="red", linewidth=2)

# データのプロット（得られた標本平均100の位置に点線を通すなど）
plt.axvline(x=100, color="gray", linestyle=":", label="Sample Mean ($\mu=100$)")

# グラフの装飾
plt.title("Bayesian Update: Prior vs Posterior Distribution", fontsize=12)
plt.xlabel("$\mu$ (Weight of Potato Chips)", fontsize=10)
plt.ylabel("Probability Density", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# 画像として保存、または表示
plt.savefig("bayes_plot.png", dpi=300)
plt.show()