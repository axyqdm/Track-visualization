import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 把字体设置为SimHei
plt.rcParams['axes.unicode_minus'] = False

file_paths = ['D:/AA_work/AIS数据/data/traj_149.txt']

fig, axs = plt.subplots(2, figsize=(10, 12))  # 两子图

for i, file_path in enumerate(file_paths):
    my_data = np.loadtxt(file_path, delimiter=";", skiprows=1)
    lat = my_data[:, 1]
    lon = my_data[:, 0]
    time = my_data[:, 4]

    axs[0].plot(time, lat, label=f'Trajectory {i + 1}', linewidth=2)  # 第一个子图中画时间-纬度图
    axs[1].plot(time, lon, label=f'Trajectory {i + 1}', linewidth=2)  # 第二个子图中画时间-经度图

axs[0].legend()  # 第一个子图
axs[0].set_xlabel('时间（秒）')
axs[0].set_ylabel('纬度')
axs[0].set_title('时间-纬度图')

axs[1].legend()  # 第二个子图
axs[1].set_xlabel('时间（秒）')
axs[1].set_ylabel('经度')
axs[1].set_title('时间-经度图')

plt.tight_layout()  # 调整布局
plt.show()
