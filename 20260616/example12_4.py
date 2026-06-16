import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


plt.rcParams['font.family'] = 'Microsoft JhengHei' # Mac 請改為 'PingFang TC'
plt.rcParams['axes.unicode_minus'] = False

data = pd.DataFrame({
    'segment': ['new', 'growth', 'vip'],
    'revenue': [100000, 150000, 410000]
})


fig, ax = plt.subplots(figsize=(10, 6))

fig.set_facecolor('#F8F9FA')
ax.set_facecolor('#F8F9FA')


colors = ['#B0BEC5', '#B0BEC5', "#C31111"] 
sns.barplot(
    data=data,
    x='segment',
    y='revenue',
    palette=colors,
    width=0.55,
    ax=ax
)


ax.text(0, 1.2, 'VIP 營收達新客的 4.1 倍，為本季絕對獲利主力', 
        transform=ax.transAxes, fontsize=18, fontweight='bold', color='#2C3E50')
ax.text(0, 1.1, '各客群營收貢獻對比 (2024 Q1) | 單位：元', 
        transform=ax.transAxes, fontsize=12, color='#7F8C8D')


sns.despine(left=True, bottom=False, right=True, top=True)
ax.yaxis.set_visible(False) 
ax.set_xlabel('')           

ax.spines['bottom'].set_color('#CFD8DC')
ax.tick_params(axis='x', labelsize=13, colors='#546E7A', bottom=False, pad=10)
label_colors = ['#78909C', '#78909C', '#C62828']
color_idx=0
for i, container in enumerate(ax.containers):
    labels = ax.bar_label(
        container,
        fmt='%d 萬',          
        padding=8,           
        fontsize=13,
        fontweight='bold'
    )
    for text_obj in labels:
            text_obj.set_color(label_colors[color_idx])
            color_idx += 1


action_text = (
    "💡 營運戰略建議：\n\n"
    "VIP 佔比極低，但客單價驚人。\n"
    "建議本月將 20% 行銷預算，\n"
    "轉移至 VIP 專屬尊榮封館活動。"
)


ax.text(
    0.6, 0.5, 
    action_text, 
    transform=ax.transAxes,
    fontsize=12, 
    color='#34495E',
    linespacing=1.8, 
    bbox=dict(facecolor='white', edgecolor='#E0E0E0', boxstyle='round,pad=1.5', alpha=0.95)
)

# --- 8. 安全邊距設定 (修正重點 🎯) ---
# 將 top 壓低到 0.75，刻意在上半部留出 25% 的巨大空間，讓標題完美呈現
plt.subplots_adjust(top=0.75, bottom=0.1, left=0.05, right=0.95)

plt.show()