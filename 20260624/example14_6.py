import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Microsoft JhengHei'
np.random.seed(42)
#信賴區間
mu = 1000 # 假設⺟體真實平均值（現實中未知）
sigma = 500 # 假設⺟體標準差
n = 100 # 每次抽樣的樣本量
n_trials = 100 # 重複抽樣 100 次
z_star = 1.96
hits = 0 # 記錄包含 μ 的次數
plt.figure(figsize=(10, 8))
for i in range(n_trials):
    sample = np.random.normal(mu, sigma, n) # 從⺟體抽樣
    print(sample)
    print('='*30)
    x_bar = sample.mean()
    se = sample.std(ddof=1) / np.sqrt(n) #不使用母體標準差,而使用樣本標準差
    ci_lo = x_bar - z_star * se
    ci_hi = x_bar + z_star * se
    contains_mu = ci_lo <= mu <= ci_hi # 這個區間有沒有包含 μ？
    hits += contains_mu
    color = "steelblue" if contains_mu else "red" # 命中藍⾊，偏掉紅⾊
    plt.plot([ci_lo, ci_hi], [i, i], color=color, alpha=0.6)
plt.axvline(mu, color="black", linewidth=2, label=f"μ = {mu}（真實值）")
plt.title(f"100 次抽樣的信賴區間（命中 μ 的次數：{hits}/100）")
plt.xlabel("營收（元）")
plt.legend()
plt.tight_layout()
plt.show()
# 你會看到⼤約 95 條藍⾊線（包含 μ），5 條紅⾊線（偏掉了）