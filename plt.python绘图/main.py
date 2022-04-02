import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")  # 这是seaborn默认的风格

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 生成数据
tool = [73, 82, 89, 66, 82, 77, 74, 70, 75, 74]
cello = [73, 119, 115, 90, 73, 89, 137, 85, 103, 127]

fig = plt.figure(figsize=(20, 8), dpi=500)  # 指明画图区间的大小
ax1 = fig.add_subplot(1, 2, 2)

# plt.title('部署时间箱线图', fontsize=25)
data = [tool, cello]
box = ax1.boxplot(
    data
)
ax1.set_xticklabels(['原型工具', 'cello'], fontsize=20)
ax1.set_ylabel('部署时间(秒)', fontsize=20)
ax1.tick_params(labelsize=20)
ax1.set_facecolor('#FFFFFF')
ax1.grid(alpha=0.3, linestyle='-.', linewidth=1, color='black')
ax1.spines['left'].set_color('black')
ax1.spines['bottom'].set_color('black')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ax2 = fig.add_subplot(1, 2, 1)
ax2.plot(x, sorted(tool, reverse=True), linestyle='-', marker='x', linewidth=1.5, label="原型工具")
ax2.plot(x, sorted(cello, reverse=True), linestyle='-', marker='x', linewidth=1.5, label="cello")
ax2.legend(loc='upper right')

ax2.set_ylabel('部署时间(秒)', fontsize=20)
ax2.tick_params(labelsize=20)
ax2.set_facecolor('#FFFFFF')
ax2.grid(alpha=0.3, linestyle='-.', linewidth=1, color='black')
ax2.spines['left'].set_color('black')
ax2.spines['bottom'].set_color('black')

plt.savefig('./plt_deployment.png', dpi=500)
plt.show()

