import numpy as np
import math

def readData_1(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 6], dtype=float)

    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(',')[0])
        returnData[i, 1] = float(readline.split(',')[1])
        returnData[i, 2] = float(readline.split(',')[2])
        returnData[i, 3] = float(readline.split(',')[3])
        returnData[i, 4] = float(readline.split(',')[4])
        returnData[i, 5] = float(readline.split(',')[5])
        i = i + 1
    readfile.close()
    return returnData

def readData_2(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 2], dtype=float)
    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(',')[0])
        returnData[i, 1] = float(readline.split(',')[1])
        i = i + 1
    readfile.close()
    return returnData


def readData_5(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 5], dtype=float)
    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(',')[0])
        returnData[i, 1] = float(readline.split(',')[1])
        returnData[i, 2] = float(readline.split(',')[2])
        returnData[i, 3] = float(readline.split(',')[3])
        returnData[i, 4] = float(readline.split(',')[4])
        i = i + 1
    readfile.close()
    return returnData



def readData_9(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 9], dtype=float)
    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(',')[0])
        returnData[i, 1] = float(readline.split(',')[1])
        returnData[i, 2] = float(readline.split(',')[2])
        returnData[i, 3] = float(readline.split(',')[3])
        returnData[i, 4] = float(readline.split(',')[4])
        returnData[i, 5] = float(readline.split(',')[5])
        returnData[i, 6] = float(readline.split(',')[6])
        returnData[i, 7] = float(readline.split(',')[7])
        returnData[i, 8] = float(readline.split(',')[8])
        i = i + 1
    readfile.close()
    return returnData


def readData_10(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 10], dtype=float)
    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(',')[0])
        returnData[i, 1] = float(readline.split(',')[1])
        returnData[i, 2] = float(readline.split(',')[2])
        returnData[i, 3] = float(readline.split(',')[3])
        returnData[i, 4] = float(readline.split(',')[4])
        returnData[i, 5] = float(readline.split(',')[5])
        returnData[i, 6] = float(readline.split(',')[6])
        returnData[i, 7] = float(readline.split(',')[7])
        returnData[i, 8] = float(readline.split(',')[8])
        returnData[i, 9] = float(readline.split(',')[9])
        i = i + 1
    readfile.close()
    return returnData

def readData_11(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 11], dtype=float)
    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(',')[0])
        returnData[i, 1] = float(readline.split(',')[1])
        returnData[i, 2] = float(readline.split(',')[2])
        returnData[i, 3] = float(readline.split(',')[3])
        returnData[i, 4] = float(readline.split(',')[4])
        returnData[i, 5] = float(readline.split(',')[5])
        returnData[i, 6] = float(readline.split(',')[6])
        returnData[i, 7] = float(readline.split(',')[7])
        returnData[i, 8] = float(readline.split(',')[8])
        returnData[i, 9] = float(readline.split(',')[9])
        returnData[i, 10] = float(readline.split(',')[10])
        i = i + 1
    readfile.close()
    return returnData

def readData_12(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 12], dtype=float)
    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(',')[0])
        returnData[i, 1] = float(readline.split(',')[1])
        returnData[i, 2] = float(readline.split(',')[2])
        returnData[i, 3] = float(readline.split(',')[3])
        returnData[i, 4] = float(readline.split(',')[4])
        returnData[i, 5] = float(readline.split(',')[5])
        returnData[i, 6] = float(readline.split(',')[6])
        returnData[i, 7] = float(readline.split(',')[7])
        returnData[i, 8] = float(readline.split(',')[8])
        returnData[i, 9] = float(readline.split(',')[9])
        returnData[i, 10] = float(readline.split(',')[10])
        returnData[i, 11] = float(readline.split(',')[11])
        i = i + 1
    readfile.close()
    return returnData



def write_neighborID(path, data):
    writefilePosition = open(path, "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for j in range(len(data)):
        writefilePosition.writelines(
            [str(data[j, 0]), ', ', str(data[j, 1]), ', ',\
             str(data[j, 2]),  ', ', str(data[j, 3]), '\n']) # str(data[j, 4]), ', ', str(data[j, 5]), ', ', str(data[j, 6]), ', ', str(data[j, 7]),
    writefilePosition.close()


# 将FeatureData_L1C1删除label=0的行之后的data_pure数据存入到pureFeatureData_L1C1_deleteLable0文件中
def write_pureRawData_deleteLabel0(path, data_pure):
    writefilePosition = open(path, "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(data_pure)):
        writefilePosition.writelines([str(data_pure[i, 0]), ', ', str(data_pure[i, 1]), ', ', str(data_pure[i, 2]), ', ',\
          str(data_pure[i, 3]), ', ', str(data_pure[i, 4]), ', ', str(data_pure[i, 5]), '\n'])
    writefilePosition.close()

# 将需要的部分数据从txt文件中提取出来，存放到array数组中
def readData_N(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 4], dtype=float)

    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(',')[0])
        returnData[i, 1] = float(readline.split(',')[1])
        returnData[i, 2] = float(readline.split(',')[2])
        returnData[i, 3] = float(readline.split(',')[3])
        i = i + 1
    readfile.close()
    return returnData

# 将需要的部分数据从txt文件中提取出来，存放到array数组中
def readData_N_test(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 5], dtype=float)

    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(',')[0])
        returnData[i, 1] = float(readline.split(',')[1])
        returnData[i, 2] = float(readline.split(',')[2])
        returnData[i, 3] = float(readline.split(',')[3])
        returnData[i, 4] = float(readline.split(',')[4])
        # returnData[i, 5] = float(readline.split(',')[5])
        i = i + 1
    readfile.close()
    return returnData


# 将需要的部分数据从Points_L1C1.txt文件中提取出来，存放到array数组中
def readData_Points(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 10], dtype=float)

    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(' ')[0])
        returnData[i, 1] = float(readline.split(' ')[1])
        returnData[i, 2] = float(readline.split(' ')[2])
        returnData[i, 3] = float(readline.split(' ')[3])
        returnData[i, 4] = float(readline.split(' ')[4])
        returnData[i, 5] = float(readline.split(' ')[5])
        returnData[i, 6] = float(readline.split(' ')[6])
        returnData[i, 7] = float(readline.split(' ')[7])
        returnData[i, 8] = float(readline.split(' ')[8])
        returnData[i, 9] = float(readline.split(' ')[9])
        i = i + 1
    readfile.close()
    return returnData


def readData_F(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 5], dtype=float)

    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(',')[0])
        returnData[i, 1] = float(readline.split(',')[1])
        returnData[i, 2] = float(readline.split(',')[2])
        returnData[i, 3] = float(readline.split(',')[3])
        returnData[i, 4] = float(readline.split(',')[4])
        i = i + 1
    readfile.close()
    return returnData

def readData_O(path, pos):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 2], dtype=float)

    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(',')[0])
        returnData[i, 1] = float(readline.split(',')[pos])
        i = i + 1
    readfile.close()
    return returnData


def readData_neighobr(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 4], dtype='float32')

    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(',')[0])
        returnData[i, 1] = float(readline.split(',')[1])
        returnData[i, 2] = float(readline.split(',')[2])
        returnData[i, 3] = float(readline.split(',')[3])
        i = i + 1
    readfile.close()
    return returnData


# Classifier.py 将需要的部分数据从txt文件中提取出来，存放到array数组中
def readData_C(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 6], dtype=float)

    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(',')[0])
        returnData[i, 1] = float(readline.split(',')[1])
        returnData[i, 2] = float(readline.split(',')[2])
        returnData[i, 3] = float(readline.split(',')[3])
        returnData[i, 4] = float(readline.split(',')[4])
        returnData[i, 5] = float(readline.split(',')[5])
        i = i + 1
    readfile.close()
    return returnData


# 将X_train写入一个txt，方便调试
def write_X(path, X_train):
    writefilePosition = open(path, "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(X_train)):
        writefilePosition.writelines([str(X_train[i, 0]), ', ', str(X_train[i, 1]), ', ', str(X_train[i, 2]), ', ', str(X_train[i, 3]), ', ', str(X_train[i, 4]), '\n'])
    writefilePosition.close()


def read_X(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 5], dtype=float)
    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(', ')[0])
        returnData[i, 1] = float(readline.split(', ')[1])
        returnData[i, 2] = float(readline.split(', ')[2])
        returnData[i, 3] = float(readline.split(', ')[3])
        returnData[i, 4] = float(readline.split(', ')[4])
        i = i + 1
    readfile.close()
    return returnData


# 将Y_train写入一个txt，方便调试
def write_Y(path, Y_train):
    writefilePosition = open(path, "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(Y_train)):
        writefilePosition.writelines([str(Y_train[i, 0]), '\n'])
    writefilePosition.close()


def read_Y(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 1], dtype=float)
    for readline in readAllLine:
        returnData[i] = float(readline.split(',')[5])
        # returnData[i] = float(readline[0])
        i = i + 1
    readfile.close()
    return returnData


# 将X_train_featureVector写入一个txt，方便调试
def write_X_featureVector(path, X_featureVector):
    writefilePosition = open(path, "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(X_featureVector)):
        writefilePosition.writelines([str(X_featureVector[i, 0]), ', ', str(X_featureVector[i, 1]), ', ', str(X_featureVector[i, 2]), \
         ', ', str(X_featureVector[i, 3]), ', ', str(X_featureVector[i, 4]), '\n'])  #
    writefilePosition.close()

def write_all_featureVector(path, X_featureVector):
    writefilePosition = open(path, "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(X_featureVector)):
        writefilePosition.writelines(
            [str(X_featureVector[i, 0]), ', ', str(X_featureVector[i, 1]), ', ', str(X_featureVector[i, 2]), \
             ', ', str(X_featureVector[i, 3]), ', ', str(X_featureVector[i, 4]), ', ', str(X_featureVector[i, 5]),
             ', ', str(X_featureVector[i, 6]), ', ', str(X_featureVector[i, 7]), ', ', str(X_featureVector[i, 8]),
             ', ', str(X_featureVector[i, 9]), ', ', str(X_featureVector[i, 10]), ', ', str(X_featureVector[i, 11]),
             ', ', str(X_featureVector[i, 12]), '\n'])  #
    writefilePosition.close()


def read_X_featureVector(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 4], dtype=float)
    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(', ')[1])
        returnData[i, 1] = float(readline.split(', ')[2])
        returnData[i, 2] = float(readline.split(', ')[3])
        returnData[i, 3] = float(readline.split(', ')[4])
        # returnData[i, 2] = float(readline.split(', ')[5])
        # returnData[i, 3] = float(readline.split(', ')[6])
        # returnData[i, 4] = float(readline.split(', ')[7])
        # returnData[i, 5] = float(readline.split(', ')[8])
        # returnData[i, 6] = float(readline.split(', ')[9])
        # returnData[i, 7] = float(readline.split(', ')[10])
        # returnData[i, 8] = float(readline.split(', ')[11])
        # returnData[i, 9] = float(readline.split(', ')[12])
        i = i + 1
    readfile.close()
    return returnData


def read_featureVector(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 4], dtype=float)
    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(',')[1])
        returnData[i, 1] = float(readline.split(',')[2])
        returnData[i, 2] = float(readline.split(',')[3])
        returnData[i, 3] = float(readline.split(',')[4])
        # returnData[i, 4] = float(readline.split(', ')[4])
        # returnData[i, 5] = float(readline.split(', ')[5])
        i = i + 1
    readfile.close()
    return returnData


# 将X_train_featureVector写入一个txt，方便调试
def write_X_addGF_featureVector(path, X_featureVector):
    writefilePosition = open(path, "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(X_featureVector)):
        writefilePosition.writelines([str(X_featureVector[i, 0]), ', ', str(X_featureVector[i, 1]), ', ', str(X_featureVector[i, 2]), \
         ', ', str(X_featureVector[i, 3]), ', ', str(X_featureVector[i, 4]), ', ', str(X_featureVector[i, 5]), ', ', str(X_featureVector[i, 6]), \
         ', ', str(X_featureVector[i, 7]), ', ', str(X_featureVector[i, 8]), ', ', str(X_featureVector[i, 9]), ', ', str(X_featureVector[i, 10]), \
         ', ', str(X_featureVector[i, 11]), ', ', str(X_featureVector[i, 12]), '\n'])
    writefilePosition.close()

def read_X_addGF_featureVector(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 14], dtype=float)
    # 0-ID; 1-I1; 2-E2; 3-I2; 4-I3; 5-omnivariance; 6-anisotropy; 7-eigenentropy; 8-summation, 9-localCurvature, 10-linearity, 11-planarity, 12-sphericity
    for readline in readAllLine:
        if math.isinf(float(readline.split(', ')[1])) or math.isnan(float(readline.split(', ')[1])):
            returnData[i, 0] = 0
        else:
            returnData[i, 0] = float(readline.split(', ')[1])
        if math.isinf(float(readline.split(', ')[2])) or math.isnan(float(readline.split(', ')[2])):
            returnData[i, 1] = 0
        else:
            returnData[i, 1] = float(readline.split(', ')[2])
        if math.isinf(float(readline.split(', ')[3])) or math.isnan(float(readline.split(', ')[3])):
            returnData[i, 2] = 0
        else:
            returnData[i, 2] = float(readline.split(', ')[3])
        if math.isinf(float(readline.split(', ')[4])) or math.isnan(float(readline.split(', ')[4])):
            returnData[i, 3] = 0
        else:
            returnData[i, 3] = float(readline.split(', ')[4])
        if math.isinf(float(readline.split(', ')[5])) or math.isnan(float(readline.split(', ')[5])):
            returnData[i, 4] = 0
        else:
            returnData[i, 4] = float(readline.split(', ')[5])
        if math.isinf(float(readline.split(', ')[6])) or math.isnan(float(readline.split(', ')[6])):
            returnData[i, 5] = 0
        else:
            returnData[i, 5] = float(readline.split(', ')[6])
        if math.isinf(float(readline.split(', ')[7])) or math.isnan(float(readline.split(', ')[7])):
            returnData[i, 6] = 0
        else:
            returnData[i, 6] = float(readline.split(', ')[7])
        if math.isinf(float(readline.split(', ')[8])) or math.isnan(float(readline.split(', ')[8])):
            returnData[i, 7] = 0
        else:
            returnData[i, 7] = float(readline.split(', ')[8])
        if math.isinf(float(readline.split(', ')[9])) or math.isnan(float(readline.split(', ')[9])):
            returnData[i, 8] = 0
        else:
            returnData[i, 8] = float(readline.split(', ')[9])
        if math.isinf(float(readline.split(', ')[10])) or math.isnan(float(readline.split(', ')[10])):
            returnData[i, 9] = 0
        else:
            returnData[i, 9] = float(readline.split(', ')[10])
        returnData[i, 10] = float(readline.split(', ')[11])
        returnData[i, 11] = float(readline.split(', ')[12])
        returnData[i, 12] = float(readline.split(', ')[13])
        returnData[i, 13] = float(readline.split(', ')[14])
        i = i + 1
    readfile.close()
    return returnData


def write_geometricFeature(path, X_featureVector):
    writefilePosition = open(path, "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(X_featureVector)):
        writefilePosition.writelines(
            [str(X_featureVector[i, 0]), ', ', str(X_featureVector[i, 1]), ', ', str(X_featureVector[i, 2]), \
             ', ', str(X_featureVector[i, 3]), ', ', str(X_featureVector[i, 4]), ', ', str(X_featureVector[i, 5]),
             ', ', str(X_featureVector[i, 6]),', ', str(X_featureVector[i, 7]), ', ', str(X_featureVector[i, 8]),
             ', ', str(X_featureVector[i, 9]),', ', str(X_featureVector[i, 10]), ', ', str(X_featureVector[i, 11]), '\n'])
    writefilePosition.close()

def write_geometricFeature_easy(path, X_featureVector):
    writefilePosition = open(path, "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(X_featureVector)):
        writefilePosition.writelines(
            [str(X_featureVector[i, 0]), ', ', str(X_featureVector[i, 1]), ', ', str(X_featureVector[i, 2]), \
             ', ', str(X_featureVector[i, 3]), ', ', str(X_featureVector[i, 4]), ', ', str(X_featureVector[i, 5]),
             ', ', str(X_featureVector[i, 6]), ', ', str(X_featureVector[i, 7]), ', ', str(X_featureVector[i, 8]), '\n'])
    writefilePosition.close()

def write_ch13(path, ch13):
    writefilePosition = open(path, "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(ch13)):
        writefilePosition.writelines(
            [str(ch13[i, 0]), ', ', str(ch13[i, 1]), ', ', str(ch13[i, 2]), '\n'])
    writefilePosition.close()

def write_ch2(path, ch2):
    writefilePosition = open(path, "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(ch2)):
        writefilePosition.writelines(
            [str(ch2[i, 0]), ', ', str(ch2[i, 1]), ', ', str(ch2[i, 2]), \
             ', ', str(ch2[i, 3]), ', ', str(ch2[i, 4]), '\n'])
    writefilePosition.close()


def write_RadEleFeature(path, XY_all, ch1_RadEleFeature, ch2_RadEleFeature, ch3_RadEleFeature):
    writefilePosition = open(path, "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    i_1 = 0
    i_2 = 0
    i_3 = 0
    i = 0
    for i in range(len(XY_all)):
        if i_1 == len(ch1_RadEleFeature) and i_3 == len(ch3_RadEleFeature):
            writefilePosition.writelines(
                [str(XY_all[i, 0]), ', ', str(0), ', ', str(0), ', ', str(ch2_RadEleFeature[i_2, 1]), \
                 ', ', str(ch2_RadEleFeature[i_2, 2]), ', ', str(ch2_RadEleFeature[i_2, 3]), ', ',
                 str(ch2_RadEleFeature[i_2, 4]), ', ', str(0), ', ', str(0), '\n'])
            i_2 = i_2 + 1
        elif i_1 == len(ch1_RadEleFeature) and i_3 < len(ch3_RadEleFeature):
            writefilePosition.writelines(
                [str(XY_all[i, 0]), ', ', str(0),', ', str(0),', ', str(ch2_RadEleFeature[i_2, 1]), \
                 ', ', str(ch2_RadEleFeature[i_2, 2]),', ', str(ch2_RadEleFeature[i_2, 3]),', ', str(ch2_RadEleFeature[i_2, 4]), ', ',\
                 str(ch3_RadEleFeature[i_3, 1]), ', ', str(ch3_RadEleFeature[i_3, 2]), '\n'])
            i_2 = i_2 + 1
            i_3 = i_3 + 1
        elif i_1 < len(ch1_RadEleFeature) and i_3 == len(ch3_RadEleFeature):
            writefilePosition.writelines(
                [str(XY_all[i, 0]), ', ', str(ch1_RadEleFeature[i_1, 1]), ', ', str(ch1_RadEleFeature[i_1, 2]),', ', str(ch2_RadEleFeature[i_2, 1]), \
                 ', ', str(ch2_RadEleFeature[i_2, 2]),', ', str(ch2_RadEleFeature[i_2, 3]),', ', str(ch2_RadEleFeature[i_2, 4]), ', ', str(0),', ', str(0), '\n'])
            i_1 = i_1 + 1
            i_2 = i_2 + 1
        else:
            if XY_all[i, 0] == ch1_RadEleFeature[i_1, 0] == ch2_RadEleFeature[i_2, 0] == ch3_RadEleFeature[i_3, 0]:
                writefilePosition.writelines(
                    [str(XY_all[i, 0]), ', ', str(ch1_RadEleFeature[i_1, 1]), ', ', str(ch1_RadEleFeature[i_1, 2]),', ', str(ch2_RadEleFeature[i_2, 1]), \
                     ', ', str(ch2_RadEleFeature[i_2, 2]),', ', str(ch2_RadEleFeature[i_2, 3]),', ', str(ch2_RadEleFeature[i_2, 4]), ', ', str(ch3_RadEleFeature[i_3, 1]),', ', str(ch3_RadEleFeature[i_3, 2]), '\n'])
                i_1 = i_1 + 1
                i_2 = i_2 + 1
                i_3 = i_3 + 1
            elif XY_all[i, 0] == ch1_RadEleFeature[i_1, 0] == ch2_RadEleFeature[i_2, 0] and XY_all[i, 0] != ch3_RadEleFeature[i_3, 0]:
                writefilePosition.writelines(
                    [str(XY_all[i, 0]), ', ', str(ch1_RadEleFeature[i_1, 1]), ', ', str(ch1_RadEleFeature[i_1, 2]),', ', str(ch2_RadEleFeature[i_2, 1]), \
                     ', ', str(ch2_RadEleFeature[i_2, 2]),', ', str(ch2_RadEleFeature[i_2, 3]),', ', str(ch2_RadEleFeature[i_2, 4]), ', ', str(0),', ', str(0), '\n'])
                i_1 = i_1 + 1
                i_2 = i_2 + 1
            elif XY_all[i, 0] == ch1_RadEleFeature[i_1, 0] == ch3_RadEleFeature[i_3, 0] and XY_all[i, 0] != ch2_RadEleFeature[i_2, 0]:
                writefilePosition.writelines(
                    [str(ch2_RadEleFeature[i_2, 0]), ', ', str(ch1_RadEleFeature[i_1, 1]), ', ', str(ch1_RadEleFeature[i_1, 2]),', ', str(0),', ', str(0),', ', \
                     str(0),', ', str(0), ', ', str(ch3_RadEleFeature[i_3, 1]), ', ', str(ch3_RadEleFeature[i_3, 2]), '\n'])
                i_1 = i_1 + 1
                i_3 = i_3 + 1
            elif XY_all[i, 0] == ch2_RadEleFeature[i_2, 0] == ch3_RadEleFeature[i_3, 0] and XY_all[i, 0] != ch1_RadEleFeature[i_1, 0]:
                writefilePosition.writelines(
                    [str(XY_all[i, 0]), ', ', str(0),', ', str(0),', ', str(ch2_RadEleFeature[i_2, 1]), \
                     ', ', str(ch2_RadEleFeature[i_2, 2]),', ', str(ch2_RadEleFeature[i_2, 3]),', ', str(ch2_RadEleFeature[i_2, 4]), ', ',\
                     str(ch3_RadEleFeature[i_3, 1]), ', ', str(ch3_RadEleFeature[i_3, 2]), '\n'])
                i_2 = i_2 + 1
                i_3 = i_3 + 1
            elif XY_all[i, 0] == ch1_RadEleFeature[i_1, 0] and XY_all[i, 0] != ch2_RadEleFeature[i_2, 0] and XY_all[i, 0] != ch3_RadEleFeature[i_3, 0]:
                writefilePosition.writelines(
                    [str(XY_all[i, 0]), ', ', str(ch1_RadEleFeature[i_1, 1]), ', ', str(ch1_RadEleFeature[i_1, 2]),', ', str(0), \
                     ', ', str(0),', ', str(0),', ', str(0), ', ', str(0),', ', str(0), '\n'])
                i_1 = i_1 + 1
            elif XY_all[i, 0] == ch2_RadEleFeature[i_2, 0] and XY_all[i, 0] != ch3_RadEleFeature[i_3, 0] and XY_all[i, 0] != ch1_RadEleFeature[i_1, 0]:
                writefilePosition.writelines(
                    [str(XY_all[i, 0]), ', ', str(0),', ', str(0),', ', str(ch2_RadEleFeature[i_2, 1]), \
                     ', ', str(ch2_RadEleFeature[i_2, 2]),', ', str(ch2_RadEleFeature[i_2, 3]),', ', str(ch2_RadEleFeature[i_2, 4]), ', ',\
                     str(0), ', ', str(0), '\n'])
                i_2 = i_2 + 1
            elif XY_all[i, 0] == ch3_RadEleFeature[i_3, 0] and XY_all[i, 0] != ch2_RadEleFeature[i_2, 0] and XY_all[i, 0] != ch1_RadEleFeature[i_1, 0]:
                writefilePosition.writelines(
                    [str(XY_all[i, 0]), ', ', str(0),', ', str(0),', ', str(0), \
                     ', ', str(0),', ', str(0),', ', str(0), ', ',\
                     str(ch3_RadEleFeature[i_3, 1]), ', ', str(ch3_RadEleFeature[i_3, 2]), '\n'])
                i_3 = i_3 + 1
            else:
                writefilePosition.writelines(
                    [str(XY_all[i, 0]), ', ', str(0), ', ', str(0),', ', str(0), \
                     ', ', str(0),', ', str(0),', ', str(0), ', ', str(0),', ', str(0), '\n'])
        i = i + 1
    writefilePosition.close()


def read_geometricfeature(path):
    readfile = open(path, "r")
    readAllLine = readfile.readlines()
    lineNum = len(readAllLine)
    i = 0
    returnData = np.empty([lineNum, 12], dtype=float)
    for readline in readAllLine:
        returnData[i, 0] = float(readline.split(', ')[0])
        returnData[i, 1] = float(readline.split(', ')[1])
        returnData[i, 2] = float(readline.split(', ')[2])
        returnData[i, 3] = float(readline.split(', ')[3])
        returnData[i, 4] = float(readline.split(', ')[4])
        returnData[i, 5] = float(readline.split(', ')[5])
        returnData[i, 6] = float(readline.split(', ')[6])
        returnData[i, 7] = float(readline.split(', ')[7])
        returnData[i, 8] = float(readline.split(', ')[8])
        returnData[i, 9] = float(readline.split(', ')[9])
        returnData[i, 10] = float(readline.split(', ')[10])
        returnData[i, 11] = float(readline.split(', ')[11])
        i = i + 1
    readfile.close()
    return returnData


# 将labelResult写入一个txt
def write_label(path, labelResult):
    writefilePosition = open(path, "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(labelResult)):
        writefilePosition.writelines([str(labelResult[i, 0]), ', ', str(labelResult[i, 1]), '\n'])
    writefilePosition.close()



def write_test(path, data):
    writefilePosition = open(path, "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    writefilePosition.writelines([str(data[0, 0]), '\n'])
    writefilePosition.close()


