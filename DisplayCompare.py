import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import FileUtil as fu
import Global_List as gl
import FileUtil

summaryData = FileUtil.readSummary()
print(summaryData)
listname = []
listactual = []
listcalculate = []
for i in summaryData:
    listname.append(i[gl.SK_File])
    listactual.append(i[gl.SK_A])
    listcalculate.append(i[gl.SK_C])

plt.figure(figsize=(18, 8))
x = np.linspace(0, 5 * len(listname), len(listname))
x1 = np.linspace(0, 5 * len(listname), len(listname))
plt.bar(x1, listactual, color='g', width=2, alpha=0.6, label='Actual Steps')
plt.bar(x + 2, listcalculate, color='r', width=2, alpha=0.4, label='Calculate Steps')
plt.xticks(x, listname, fontsize=7)
for x, y in zip(x1, np.array(listactual)):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, y + 0.05, '%d' % y, ha='center', va='bottom')


for x2, y2 in zip(x1, np.array(listcalculate)):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x2 + 2.4, y2 + 0.05, '%d' % y2, ha='center', va='bottom')

plt.subplots_adjust(left=0.02, right=0.98, top=0.95, bottom=0.1)
plt.legend(loc='upper right')
plt.xlabel('FileName')
plt.ylabel('Steps')
plt.title('Compare')
plt.show()
