import csv
import numpy as np
import matplotlib.pyplot as plt

dir = "data/"
cvsname = "cd_quick130.csv"
with open(dir + cvsname, newline='') as f:
    reader = csv.DictReader(f)
    columnX = []
    columnY = []
    columnZ = []
    columnS = []
    columnG = []
    columnAVG = []
    for row in reader:
        columnX.append(row['X'])
        columnY.append(row['Y'])
        columnZ.append(row['Z'])
        columnG.append(row['G'])
        columnS.append(row['S'])
        columnAVG.append(row['AVG'])
x = np.linspace(0, 40 * len(columnX), len(columnX))
plt.scatter(x, columnX, c='y', marker='.')
plt.plot(x, columnX, color='y', linewidth=0.5, linestyle='-', label=u'X')
plt.scatter(x, columnY, c='k', marker='.')
plt.plot(x, columnY, color='k', linewidth=0.5, linestyle='-', label=u'Y')
plt.scatter(x, columnZ, c='g', marker='.')
plt.plot(x, columnZ, color='g', linewidth=0.5, linestyle='-', label='Z')
plt.scatter(x, columnG, c='r', marker='.')
plt.plot(x, columnG, color='r', linewidth=0.5, linestyle='-', label='G')
# plt.scatter(x, columnS, c='m', marker='.')
# plt.plot(x, columnS, color='m', linewidth=0.5, linestyle='-', label='S')
plt.scatter(x, columnAVG, c='b', marker='.')
plt.plot(x, columnAVG, color='b', linewidth=0.5, linestyle='-', label='AVG')
plt.legend(loc='upper left')
plt.subplots_adjust(left=0.02, right=0.99, top=0.95, bottom=0.1)
plt.xlabel("unit:ms")
plt.title(cvsname)
plt.show()
