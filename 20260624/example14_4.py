import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family']='Microsoft JhengHei'
np.random.seed(42)
population = np.random.exponential(scale=1000, size=100_000) # 右偏分佈
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
# 左圖：原始資料的分佈（右偏）
axes[0].hist(population, bins=80, edgecolor="white", alpha=0.7)
axes[0].set_title("原始訂單⾦額分佈（右偏）")
axes[0].set_xlabel("訂單⾦額（元）")
# 右圖：抽樣平均值的分佈（CLT 發揮作⽤）
sample_means = [
np.random.choice(population, size=100).mean() # 每次抽 100 筆取平均
for _ in range(10_000) # 重複 10,000 次
]
axes[1].hist(sample_means, bins=60, edgecolor="white", alpha=0.7, color="orange")
axes[1].set_title("樣本平均值的抽樣分佈（趨近常態）")
axes[1].set_xlabel("樣本平均值（元）")
plt.tight_layout()
plt.show()
