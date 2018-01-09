# key = "index"
# value = "diff"
# dict1 = {key: 1, value: 234}
# dict2 = {key: 2, value: 2}
# dict3 = {key: 3, value: 333}
# dict4 = {key: 4, value: 44}
# listDict = [dict1, dict2, dict3, dict4]
#
# temp = listDict[1][value]
# print(temp)
import pandas as pd

# read from
data = pd.read_csv('g-data/cd_quick130.csv')
data['D'] = 0
df = pd.DataFrame(data, columns=['G', 'T', 'D'])
columnD = list(data['D'])
df.to_csv("g-data/cd_quick130.csv", index=False, sep=',')