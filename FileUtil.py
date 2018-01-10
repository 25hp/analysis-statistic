from os import walk
import pandas as pd
import csv
import re
import Global_List as gl
import pickle as pk


def getCsvFile(path):
    f = []
    ret = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        break
    for i in range(len(f)):
        if str(f[i]).__contains__(".csv"):
            ret.append(f[i])
    return ret


def readColum(csvname="", colum="G"):
    with open("data/" + csvname, newline='') as f:
        reader = csv.DictReader(f)
        columnG = []
        for row in reader:
            columnG.append(int(row[colum]))
    return columnG


def addTh2Csv(selIndex=[], threshold=[], csv=""):
    thresholdColum = []
    gColum = readColum(csv)
    gLen = len(gColum)
    selLen = len(selIndex)
    thLen = len(threshold)
    if selLen != thLen:
        print("createCsv Error")
    for i in range(selLen):
        if i != 0:
            num = selIndex[i] - selIndex[i - 1]
            for j in range(num):
                thresholdColum.append(threshold[i - 1])
    for x in range(gLen - selIndex[selLen - 1]):
        thresholdColum.append(threshold[thLen - 1])
    dataframe = pd.DataFrame({'G': gColum, 'T': thresholdColum})
    dataframe.to_csv(gl.G_DIR_PATH + csv, index=False, sep=',')


def addDiff2Csv(dicList, csv):
    data = pd.read_csv(gl.G_DIR_PATH + csv)
    data['D'] = 0
    columnD = list(data['D'])
    for i in range(len(dicList)):
        columnD[dicList[i][gl.DIFF_KEY]] = dicList[i][gl.DIFF_VALUE]
    data['D'] = columnD
    df = pd.DataFrame(data, columns=['G', 'T', 'D'])
    df.to_csv(gl.G_DIR_PATH + csv, index=False, sep=',')


def addSd2Csv(dicList, csv):
    data = pd.read_csv(gl.G_DIR_PATH + csv)
    data['S'] = 0
    columnS = list(data['S'])
    columnG = list(data['G'])
    for i in range(len(dicList)):
        columnS[dicList[i]] = columnG[dicList[i]]
    data['S'] = columnS
    df = pd.DataFrame(data, columns=['G', 'T', 'D', 'S'])
    df.to_csv(gl.G_DIR_PATH + csv, index=False, sep=',')


def saveSummary(data):
    path = gl.G_DIR_PATH + gl.SUMMARY_CSV
    with open(path, 'wb') as f:
        pk.dump(data, f, -1)


def readSummary():
    path = gl.G_DIR_PATH + gl.SUMMARY_CSV
    with open(path, 'rb') as f:
        data = pk.load(f)
    return data


def getActualStep(name):
    item = re.sub("\D", "", name)
    return int(item)


if __name__ == '__main__':
    # getCsvFile("data/")
    # a = [1, 2, 3]
    # b = [4, 5, 6]
    # dataframe = pd.DataFrame({'a_name': a, 'b_name': b})
    # dataframe.to_csv("g-data/test.csv", index=False, sep=',')
    # addTh2Csv(csv="cd_slow150.csv")
    data1 = [{'file': "a.csv",
              'actual': 500,
              'calculate': 504},
             {'file': "b.csv",
              'actual': 5001,
              'calculate': 5024}
             ]
    saveSummary(data=data1)
    print(readSummary())
