from os import walk
import pandas as pd
import csv


def getCsvFile(path):
    f = []
    ret = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        break
    for i in range(len(f)):
        if str(f[i]).__contains__(".csv"):
            ret.append(f[i])
    print(ret)
    return ret


def readGcolum(csvname=""):
    with open("data/" + csvname, newline='') as f:
        reader = csv.DictReader(f)
        columnG = []
        for row in reader:
            columnG.append(row['G'])
    return columnG


def createCsv(selIndex=[], threshold=[], csv=""):
    thresholdColum = []
    gColum = readGcolum(csv)
    print(gColum)
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
    dataframe.to_csv("g-data/" + csv, index=False, sep=',')


if __name__ == '__main__':
    # getCsvFile("data/")
    # a = [1, 2, 3]
    # b = [4, 5, 6]
    # dataframe = pd.DataFrame({'a_name': a, 'b_name': b})
    # dataframe.to_csv("g-data/test.csv", index=False, sep=',')
    createCsv(csv="cd_slow150.csv")
