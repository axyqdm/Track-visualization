import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.mpl.gridliner as gridliner

data = np.genfromtxt('D:/AA_work/AIS数据/data/traj_149.txt', delimiter=';', skip_header=1)

lon = data[:, 0]
lat = data[:, 1]

# 创建地图
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cfeature.OCEAN, color=[0.9373, 0.9804, 0.9882])
ax.add_feature(cfeature.LAND, color=[0.9647, 0.9647, 0.9647])
ax.add_feature(cfeature.COASTLINE, edgecolor='black')

# 绘制航线轨迹
ax.plot(lon, lat, transform=ccrs.Geodetic(), color='blue', linewidth=2)

# 经纬度网格
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_right = False

# 地图范围
ax.set_extent([lon.min()-1, lon.max()+1, lat.min()-1, lat.max()+1])

plt.title('航线轨迹图')
plt.show()




