"""显示从磁盘文件导入色图的示例。"""
from trollimage import utilities as tu

#  示例：导入色图
filename = 'setvak.rgb'
my_cmap = tu.cmap_from_text(filename)
print(my_cmap.colors)
my_cmap_norm = tu.cmap_from_text(filename, norm=True)
print(my_cmap_norm.colors)
my_cmap_transp = tu.cmap_from_text(filename, norm=True, transparency=True)
print(my_cmap_transp.colors)
filename = 'hrv.rgb'
my_cmap_hex = tu.cmap_from_text(filename, hex=True)
print(my_cmap_hex.colors)

#  示例：将 PIL 转换为 trollimage.Image
image = "pifn.png"
timage = tu.pilimage2trollimage(image)
