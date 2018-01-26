import math

import FileUtil
import Global_List as gl


# TODO:画出peak - valley 的图
class DealWithData(object):
    def __init__(self, csv="", src=[]):
        self.Src = src
        self.csvName = csv
        self.oriValues = []
        self.ValueNum = 4
        self.tempValue = []
        self.tempCount = 0
        self.isDirectionUp = False
        self.continueUpCount = 0
        self.continueUpFormerCount = 0
        self.lastStatus = False
        self.peakOfWave = float(0)
        self.valleyOfWave = float(0)
        self.timeOfThisPeak = 0
        self.timeOfLastPeak = 0
        self.timeOfNow = 0
        self.gravityNew = 0
        self.gravityOld = 0
        self.InitialValue = float(130)
        self.ThreadValue = float(200)
        self.TimeIntervalMin = float(6)
        self.TimeIntervalMax = float(50)
        self.step = 0
        self.indexOfLastPeak = 0
        self.selIndex = [0]  # for create  threshold matplot
        self.threshold = [200]
        self.DiffPV = []
        self.StepDot = []
        self.startCountFlag = True
        # 方差 20180112
        self.peakNum = 5
        self.peakArray = []  # 波峰值
        self.peakArrCount = 0
        self.peakVar = 100  # 波峰方差
        self.peakVarArr = []
        self.peakAvage = 0
        self.peakAvageArrDisplay = []
        self.peakVarArrDisplay = []

    def saveGpeakArray(self, value):
        if self.peakArrCount < self.peakNum:
            self.peakArray.append(value)
            self.peakArrCount += 1
        else:
            for i in range(self.peakNum):
                self.peakArray[i - 1] = self.peakArray[i]
                self.peakArray[self.peakNum - 1] = value

    def getPeakVar(self):
        ret = 100
        sum = 0
        if self.peakArrCount == self.peakNum:
            for i in range(self.peakNum):
                sum += self.peakArray[i]
                self.peakAvage = sum / self.peakNum
            if self.peakAvage != 0:
                sum = 0
                for i in range(self.peakNum):
                    sum += math.pow((self.peakArray[i] - self.peakAvage), 2)
                ret = sum / self.peakNum
            self.peakVar = ret
        return ret

    def createDiffDict(self, keyValue, valueValue):
        return {gl.DIFF_KEY: keyValue, gl.DIFF_VALUE: valueValue}

    def onSensorChanged(self):
        for i in range(len(self.Src)):
            self.detectorNewStep(self.Src[i], i)

    def detectorNewStep(self, values, index):
        if self.gravityOld == 0:
            self.gravityOld = values
        else:
            if self.detectorPeak(values, self.gravityOld):
                self.timeOfLastPeak = self.timeOfThisPeak
                self.timeOfNow = index
                self.DiffPV.append(self.createDiffDict(index, self.peakOfWave - self.valleyOfWave))
                if self.timeOfNow - self.timeOfLastPeak >= self.TimeIntervalMin and self.peakOfWave - self.valleyOfWave >= self.ThreadValue:
                    self.timeOfThisPeak = self.timeOfNow
                    self.countStep(index)
                    self.StepDot.append(index - 1)
                if self.timeOfNow - self.timeOfLastPeak >= self.TimeIntervalMin and (
                                self.peakOfWave - self.valleyOfWave >= self.InitialValue):
                    self.timeOfThisPeak = self.timeOfNow
                    self.ThreadValue = self.peakValleyThread(self.peakOfWave - self.valleyOfWave)
                    self.selIndex.append(index)
                    self.threshold.append(self.ThreadValue)
        if index == len(self.Src) - 1:
            print(self.csvName + ",步数:" + str(self.step))
            FileUtil.addTh2Csv(selIndex=self.selIndex, threshold=self.threshold, csv=self.csvName)
            FileUtil.addDiff2Csv(dicList=self.DiffPV, csv=self.csvName)
            FileUtil.addSd2Csv(dicList=self.StepDot, csv=self.csvName)
        self.gravityOld = values

    def detectorPeak(self, newValue, oldValue):
        self.lastStatus = self.isDirectionUp
        if newValue >= oldValue:
            self.isDirectionUp = True
            self.continueUpCount += 1
        else:
            self.continueUpFormerCount = self.continueUpCount
            self.continueUpCount = 0
            self.isDirectionUp = False
        if not self.isDirectionUp and self.lastStatus and (self.continueUpFormerCount >= 2 or oldValue >= 980):
            self.peakOfWave = oldValue
            self.saveGpeakArray(oldValue)
            self.getPeakVar()
            self.peakAvageArrDisplay.append(self.peakAvage)
            self.peakVarArrDisplay.append(round(self.peakVar / 10000, 3))
            return True
        elif not self.lastStatus and self.isDirectionUp:
            self.valleyOfWave = oldValue
            return False
        else:
            return False

    def peakValleyThread(self, value):
        self.tempThread = self.ThreadValue
        if self.tempCount < self.ValueNum:
            self.tempValue.append(value)
            self.tempCount += 1
        else:
            self.tempThread = self.averageValue(self.tempValue, self.ValueNum)
            for i in range(self.ValueNum):
                if i < 0:
                    self.tempValue[i - 1] = self.tempValue[i]
            self.tempValue[self.ValueNum - 1] = value
        return self.tempThread

    def averageValue(self, values, n):
        ave = 0
        for index in range(n):
            ave += values[index]
        ave = float(ave / self.ValueNum)
        if ave >= 800:
            ave = 430
        elif ave >= 700 and ave < 800:
            ave = 330
        elif ave >= 400 and ave < 700:
            ave = 230
        elif ave >= 300 and ave < 400:
            ave = 200
        else:
            ave = 130
        return ave

    def countStep(self, index):
        if index - self.indexOfLastPeak <= 80 or self.startCountFlag:
            if self.step < 9:
                self.step += 1
            elif self.step == 9:
                self.step += 1
            else:
                self.step += 1
        else:
            self.startCountFlag = True
            self.step = 0


if __name__ == '__main__':
    dirPath = "data/"
    listCsv = FileUtil.getCsvFile(dirPath)
    listSummary = []
    for i in range(len(listCsv)):
        sd = DealWithData(csv=listCsv[i], src=FileUtil.readColum(listCsv[i]))
        sd.onSensorChanged()
        # print(listCsv[i] + " Avg :" + str(sd.peakAvageArrDisplay))
        # print(listCsv[i] + " Var :" + str(sd.peakVarArrDisplay))
        FileUtil.saveVd2Csv(sd.peakAvageArrDisplay, sd.peakVarArrDisplay, listCsv[i])
        listSummary.append(
            {gl.SK_File: listCsv[i].split('.')[0], gl.SK_A: FileUtil.getActualStep(listCsv[i]), gl.SK_C: sd.step})
    FileUtil.saveSummary(listSummary)
