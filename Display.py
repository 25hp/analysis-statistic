import csv
import numpy as np
import matplotlib.pyplot as plt

dir = "g-data/"
cvsname = "sx_ride0.csv"
columnG = []
columnT = []
columnD = []
columnS = []
with open(dir + cvsname, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        columnG.append(float(row['G']))
        columnT.append(float(row['T']))
        columnD.append(float(row['D']))
        columnS.append(float(row['S']))

x = np.linspace(0, 40 * len(columnG), len(columnG))
plt.scatter(x, columnG, c='r', marker='.')
plt.plot(x, columnG, color='r', linewidth=0.5, linestyle='-', label='G-Axis')
plt.scatter(x, columnT, c='k', marker='.')
plt.plot(x, columnT, color='k', linewidth=0.5, linestyle='-', label='Threshold')
plt.scatter(x, columnD, facecolor='m', edgecolor='white', label='DiffPeakAndValley')
countS = 0
for i in range(len(columnS)):
    if columnS[i] > 0:
        countS += 1
plt.scatter(x, columnS, facecolor='b', edgecolor='white', label='CalculateStep' + str(countS))

plt.legend(loc='upper left')
plt.subplots_adjust(left=0.02, right=0.99, top=0.95, bottom=0.1)
plt.xlabel("unit:ms")
plt.ylabel("cm/s^2")
plt.title(cvsname)
# plt.scatter(x, columnX, c='y', marker='.')
# plt.plot(x, columnX, color='y', linewidth=0.5, linestyle='-', label=u'X')
# plt.scatter(x, columnY, c='k', marker='.')
# plt.plot(x, columnY, color='k', linewidth=0.5, linestyle='-', label=u'Y')
# plt.scatter(x, columnZ, c='g', marker='.')
# plt.plot(x, columnZ, color='g', linewidth=0.5, linestyle='-', label='Z')
# plt.scatter(x, columnS, c='m', marker='.')
# plt.plot(x, columnS, color='m', linewidth=0.5, linestyle='-', label='S')
# plt.scatter(x, columnAVG, c='b', marker='.')
# plt.plot(x, columnAVG, color='b', linewidth=0.5, linestyle='-', label='AVG')
plt.show()
