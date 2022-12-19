from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.svm import NuSVC
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import naive_bayes
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
import random
import math
import numpy as np
from datetime import datetime

from sklearn.tree import DecisionTreeClassifier

import MyFileOperator
def mpi_entrance():
    start_time = datetime.now()
    print(start_time)
    print('MyMaxEnt')


    def readLabel(path_label):
        readfile = open(path_label, "r")
        readAllLine = readfile.readlines()
        lineNum = len(readAllLine)
        i = 0
        returnData3 = np.empty([lineNum, 1], dtype=float)
        for readline in readAllLine:
            returnData3[i, 0] = float(readline.split(', ')[5])
            i = i + 1
        readfile.close()
        return returnData3

    def readFeatureVector_16(path_r):
        for n in range(10):
            readfile = open(path_r.format(bulk=n), "r")
            readAllLine = readfile.readlines()
            lineNum = len(readAllLine)
            i = 0
            returnData = np.empty([lineNum, 17], dtype=float)
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
                returnData[i, 12] = float(readline.split(', ')[12])
                returnData[i, 13] = float(readline.split(', ')[13])
                returnData[i, 14] = float(readline.split(', ')[14])
                returnData[i, 15] = float(readline.split(', ')[15])
                returnData[i, 16] = float(readline.split(', ')[16])
                i = i + 1
            readfile.close()
            if n == 0:
                featureVector = returnData
            else:
                featureVector = np.vstack((featureVector, returnData))
        return featureVector


    def Classifier(X_featureVector, Y_label):
        # clf = svm.LinearSVC(dual=False, multi_class='ovr')
        # clf = tree.DecisionTreeClassifier()
        clf = RandomForestClassifier(random_state=0)
        # clf = KNeighborsClassifier(n_neighbors=3)
        # clf = naive_bayes.GaussianNB()
        # clf = LinearDiscriminantAnalysis()
        # clf = QuadraticDiscriminantAnalysis()
        # clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=10), algorithm="SAMME", n_estimators=50, learning_rate=1)
        # clf = MLPClassifier(activation='logistic',solver='adam', max_iter=300)

        clf = clf.fit(X_featureVector, Y_label)
        print(clf)
        return clf

    sampleRatio = 0.01
    path_r_train = 'Data/cutArea/MyMaxEnt/train/{bulk}/featureVector_e213.txt'
    path_r_test = 'Data/cutArea/MyMaxEnt/test/{bulk}/featureVector_e213.txt'
    print('featureVector:featureVector_e213')
    train_featureVector_16 = readFeatureVector_16(path_r_train)
    test_featureVector_16 = readFeatureVector_16(path_r_test)
    featureVector_16 = np.vstack((train_featureVector_16, test_featureVector_16))
    path_label = 'Data/cutArea/train_test/L1C2_addC1C3_train_test.txt'
    originalLabel = readLabel(path_label)
    featureVector_16_label = np.hstack((featureVector_16, originalLabel))
    # random select 1% as training sample
    featureVector_16_label_without0 = []
    for n in range(len(featureVector_16_label)):
        if featureVector_16_label[n, 17] != 0:
            featureVector_16_label_without0.append(featureVector_16_label[n, :])
    featureVector_16_label_without0 = np.array(featureVector_16_label_without0)
    road = []
    house = []
    fence = []
    treee = []
    grass = []
    power = []
    others = []
    for j in range(len(featureVector_16_label)):
        if featureVector_16_label[j, 17] == 1:
            road.append(featureVector_16_label[j, :])
        elif featureVector_16_label[j, 17] == 2:
            house.append(featureVector_16_label[j, :])
        elif featureVector_16_label[j, 17] == 3:
            fence.append(featureVector_16_label[j, :])
        elif featureVector_16_label[j, 17] == 4:
            treee.append(featureVector_16_label[j, :])
        elif featureVector_16_label[j, 17] == 6:
            grass.append(featureVector_16_label[j, :])
        elif featureVector_16_label[j, 17] == 8:
            power.append(featureVector_16_label[j, :])
        elif featureVector_16_label[j, 17] == 0:
            others.append(featureVector_16_label[j, :])
    road = np.array(road)
    road_sample = road[np.random.choice(road.shape[0], size=int(sampleRatio*len(road)), replace=False), :]
    house = np.array(house)
    house_sample = house[np.random.choice(house.shape[0], size=int(sampleRatio*len(house)), replace=False), :]
    fence = np.array(fence)
    fence_sample = fence[np.random.choice(fence.shape[0], size=int(1*sampleRatio*len(fence)), replace=False), :]
    treee = np.array(treee)
    treee_sample = treee[np.random.choice(treee.shape[0], size=int(sampleRatio*len(treee)), replace=False), :]
    grass = np.array(grass)
    grass_sample = grass[np.random.choice(grass.shape[0], size=int(sampleRatio*len(grass)), replace=False), :]
    power = np.array(power)
    power_sample = power[np.random.choice(power.shape[0], size=int(1*sampleRatio*len(power)), replace=False), :]
    sampleFeatureVector_label = np.vstack((road_sample, house_sample))
    sampleFeatureVector_label = np.vstack((sampleFeatureVector_label, fence_sample))
    sampleFeatureVector_label = np.vstack((sampleFeatureVector_label, treee_sample))
    sampleFeatureVector_label = np.vstack((sampleFeatureVector_label, grass_sample))
    sampleFeatureVector_label = np.vstack((sampleFeatureVector_label, power_sample))


    sampleFeatureVector = sampleFeatureVector_label[:, 1:17]
    sampleLabel = sampleFeatureVector_label[:, 17]
    # 得出训练模型clf_train
    clf_train = Classifier(sampleFeatureVector, sampleLabel)
    labelPredict = clf_train.predict(featureVector_16_label_without0[:, 1:17])
    originalLabel = np.array([featureVector_16_label_without0[:, 17]]).T
    label_ori_predit = np.hstack((originalLabel, np.array([labelPredict]).T))
    label_writePath = 'Data/cutArea/MyMaxEnt/'
    # MyFileOperator.write_label(label_writePath + '1SVM_labelResult_ch2.txt', label_ori_predit)
    # MyFileOperator.write_label(label_writePath + '2DT_labelResult_ch2.txt', label_ori_predit)
    MyFileOperator.write_label(label_writePath + '3RandomForests_labelResult_e213.txt', label_ori_predit)  # 修改3
    # MyFileOperator.write_label(label_writePath + '4KNN_labelResult_ch2.txt', label_ori_predit)
    # MyFileOperator.write_label(label_writePath + '5GNB_labelResult_ch2.txt', label_ori_predit)
    # MyFileOperator.write_label(label_writePath + '6LDA_labelResult_ch2.txt', label_ori_predit)
    # MyFileOperator.write_label(label_writePath + '7QDA_labelResult_ch2.txt', label_ori_predit)
    # MyFileOperator.write_label(label_writePath + '8AB_labelResult_ch2.txt', label_ori_predit)
    # MyFileOperator.write_label(label_writePath + '9MLP_labelResult_ch2.txt', label_ori_predit)
    print('sample:' + str(sampleRatio))

    correctNum = 0
    for i in range(len(originalLabel)):
        if originalLabel[i, 0] == labelPredict[i]:
            correctNum = correctNum + 1
    accu = correctNum / len(originalLabel)
    print('3correctNum='+str(correctNum)+'; accuracy='+str(accu))


    end_time = datetime.now()
    print('All done: {}'.format(end_time - start_time))
    print(end_time)



mpi_entrance()