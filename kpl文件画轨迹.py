import pickle
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

pickle_file_path = "ct_dma_train.pkl"
with open(pickle_file_path, "rb") as f:
    data = pickle.load(f)
print(data[0])
# 提取纬度和经度
latitudes = [item[0] for item in data[4022]['traj']]
longitudes = [item[1] for item in data[4022]['traj']]

# 创建地图
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cfeature.OCEAN, color=[0.9373, 0.9804, 0.9882])
ax.add_feature(cfeature.LAND, color=[0.9647, 0.9647, 0.9647])
ax.add_feature(cfeature.COASTLINE, edgecolor='black')

# 绘制航线轨迹
ax.plot(longitudes, latitudes, transform=ccrs.Geodetic(), color='blue', linewidth=2)
# 地图范围
ax.set_extent([min(longitudes)-7, max(longitudes)+7, min(latitudes)-7, max(latitudes)+7])

plt.title('航线轨迹图')
plt.show()