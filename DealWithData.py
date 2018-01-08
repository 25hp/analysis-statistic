import csv
import DealWithData


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
        self.peakOfWave = 0
        self.valleyOfWave = 0
        self.timeOfThisPeak = 0
        self.timeOfLastPeak = 0
        self.timeOfNow = 0
        self.gravityNew = 0
        self.gravityOld = 0
        self.InitialValue = float(1.3)
        self.ThreadValue = float(2.0)
        self.TimeIntervalMin = 6
        self.TimeIntervalMax = 50
        self.step = 0
        self.indexOfLastPeak = 0


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
                if self.timeOfNow - self.timeOfLastPeak >= self.TimeIntervalMin and self.peakOfWave - self.valleyOfWave >= self.ThreadValue:
                    self.timeOfThisPeak = self.timeOfNow
                    self.countStep(index)
                if self.timeOfNow - self.timeOfLastPeak >= self.TimeIntervalMin and (
                                self.peakOfWave - self.valleyOfWave >= self.InitialValue):
                    self.timeOfThisPeak = self.timeOfNow
                    self.ThreadValue = self.peakValleyThread(self.peakOfWave - self.valleyOfWave)
        if index == len(self.Src) - 1:
            print("步数:" + str(self.step))
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
        if not self.isDirectionUp and self.lastStatus and (self.continueUpFormerCount >= 2 or oldValue >= 20):
            self.peakOfWave = oldValue
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
        for index in range(len(values)):
            ave += values[index]
        ave = ave / self.ValueNum
        if ave >= 8:
            ave = 4.3
        elif ave >= 7 and ave < 8:
            ave = 3.3
        elif ave >= 4 and ave < 7:
            ave = 2.3
        elif ave >= 3 and ave < 4:
            ave = 2.0
        else:
            ave = 1.3
        return ave


    def countStep(self, index):
        if self.step < 9:
            self.step += 1
        elif self.step == 9:
            self.step += 1
        else:
            self.step += 1
            # TODO:判断小于9步的


if __name__ == '__main__':
    dir = "data/"
    cvsname = "cd_slow150.csv"
    columnG = []
    with open(dir + cvsname, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            columnG.append(int(row['G']) / 100)
    print(columnG)
    sd = DealWithData(csv=cvsname, src=columnG)
    sd.onSensorChanged()
