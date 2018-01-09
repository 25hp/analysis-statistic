import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import FileUtil as fu
import Global_List as gl

listFile = fu.getCsvFile(gl.G_DIR_PATH)
listData = []
for i in range(len(listFile)):
    file = listFile[i]
    item = re.sub("\D", "", file)
    listData.append(int(item))

# data_week2015 = pd.read_csv('data_week2015.txt')['nums'].T.values
# data_week2016 = pd.read_csv('data_week2016.txt')['nums'].T.values
# plt.figure(figsize=(10, 6))
# xweek = range(0, len(data_week2015))
# xweek1 = [i + 0.3 for i in xweek]
# plt.bar(xweek, data_week2015, color='g', width=.3, alpha=0.6, label='2015年')
# plt.bar(xweek1, data_week2016, color='r', width=.3, alpha=0.4, label='2016年')
# plt.xlabel('文件名')
# plt.ylabel('步数')
# plt.title('步数比较图')
x = np.linspace(0, 4 * len(listFile), len(listFile))
plt.bar(x, listData, color='g', width=1, alpha=0.6, label='True Steps')
plt.xticks(x, listFile)
plt.legend(loc='upper right')
plt.show()
