from sklearn.neighbors import NearestNeighbors
import numpy as np
import math
import MyFileOperator
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree
# X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# Y = np.array([[1,1]])
# nbrs = NearestNeighbors(n_neighbors=3, algorithm='ball_tree').fit(X)
# distances, indices = nbrs.kneighbors(Y)
# print(X)

# x = [650020.75, 4850075.3, 53.46]
# y = [650021.85, 4850077.65, 55.66]
# dis = math.sqrt(math.pow(x[0]-y[0], 2) + math.pow(x[1]-y[1], 2) + math.pow(x[2]-y[2], 2))
# print(dis)



# filter noise  # elevation大于100的点将被视为noise point
# channel_data = MyFileOperator.readData_1('Data/RawData_L1C1.txt')  #channel 2
# channel_data = MyFileOperator.readData_2('Data/RawData_L1C3.txt')  #channel 1 and 3
# channel_cleanData = []
# channel_noise = []
# for i in range(len(channel_data)):
#     if channel_data[i, 3] < 100:
#         channel_cleanData.append(channel_data[i, :])
#     else:
#         channel_noise.append(channel_data[i, :])
#
# channel_cleanData = np.array(channel_cleanData)
# writefilePosition = open('Data/RawData_L1C3_clean.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for i in range(len(channel_cleanData)):
#     writefilePosition.writelines([str(channel_cleanData[i, 0]), ', ', str(channel_cleanData[i, 1]), ', ', str(channel_cleanData[i, 2]), ', ',\
#       str(channel_cleanData[i, 3]), ', ', str(channel_cleanData[i, 4]),  '\n']) # ', ', str(channel_cleanData[i, 5]),
# writefilePosition.close()
#
# channel_noise = np.array(channel_noise)
# writefilePosition = open('Data/RawData_L1C3_noise.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for i in range(len(channel_noise)):
#     writefilePosition.writelines([str(channel_noise[i, 0]), ', ', str(channel_noise[i, 1]), ', ', str(channel_noise[i, 2]), ', ',\
#       str(channel_noise[i, 3]), ', ', str(channel_noise[i, 4]),  '\n']) # ', ', str(channel_noise[i, 5]),
# writefilePosition.close()



# # L1C2 clean data sampling
# readfile = open('Data/RawData_L1C2_clean.txt', "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData_2 = np.empty([lineNum, 6], dtype=float)
# for readline in readAllLine:
#     returnData_2[i, 0] = float(readline.split(', ')[0])
#     returnData_2[i, 1] = float(readline.split(', ')[1])
#     returnData_2[i, 2] = float(readline.split(', ')[2])
#     returnData_2[i, 3] = float(readline.split(', ')[3])
#     returnData_2[i, 4] = float(readline.split(', ')[4])
#     returnData_2[i, 5] = float(readline.split(', ')[5])
#     i = i + 1
# readfile.close()
# # 均匀采样，间隔100
# outputID = []
# step = 50
# for i in range(0, len(returnData_2), step):
#     if i < len(returnData_2):
#         outputID.append(i)
# outputID = np.array(outputID)
# output = returnData_2[outputID, :]
#
# writefilePosition = open('Data/SampleStep_50/RawData_L1C2_clean_sample.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for j in range(len(output)):
#     writefilePosition.writelines([str(output[j, 0]), ', ', str(output[j, 1]), ', ', str(output[j, 2]), \
#                                   ', ', str(output[j, 3]), ', ', str(output[j, 4]), ', ', str(output[j, 5]), '\n'])
# writefilePosition.close()




# # add one nearest neighbor point information from channel 1 and channel 3 into channel 2 sample data
# channel1_data = MyFileOperator.readData_5('Data/cutArea/L1C1.txt')
# channel3_data = MyFileOperator.readData_5('Data/cutArea/L1C3.txt')
# channel2_data_cut = MyFileOperator.readData_1('Data/cutArea/L1C2.txt')
#
# nbrs_1 = NearestNeighbors(n_neighbors=1, algorithm='kd_tree').fit(channel1_data[:, 1:4])
# distances_1, indices_1 = nbrs_1.kneighbors(channel2_data_cut[:, 1:4])
#
# nbrs_3 = NearestNeighbors(n_neighbors=1, algorithm='kd_tree').fit(channel3_data[:, 1:4])
# distances_3, indices_3 = nbrs_3.kneighbors(channel2_data_cut[:, 1:4])
#
# i = 0
# returnData = np.empty([len(channel2_data_cut), 10], dtype=float)
# returnData[:, 0:6] = channel2_data_cut
# for i in range(len(channel2_data_cut)):
#     returnData[i, 6] = indices_1[i]
#     returnData[i, 7] = channel1_data[indices_1[i], 4]
#     returnData[i, 8] = indices_3[i]
#     returnData[i, 9] = channel3_data[indices_3[i], 4]
#     i = i + 1
#
# writefilePosition = open('Data/cutArea/L1C2_addC1C3.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for i in range(len(returnData)):
#     writefilePosition.writelines(
#         [str(returnData[i, 0]), ', ', str(returnData[i, 1]), ', ', str(returnData[i, 2]), \
#          ', ', str(returnData[i, 3]), ', ', str(returnData[i, 4]), ', ', str(returnData[i, 5]),
#          ', ', str(returnData[i, 6]), ', ', str(returnData[i, 7]), ', ', str(returnData[i, 8]),
#          ', ', str(returnData[i, 9]), '\n'])  #
# writefilePosition.close()



# readfile = open('Data/cutArea/L1C2_Normalization.txt', "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData = np.empty([lineNum, 6], dtype=float)
# for readline in readAllLine:
#     returnData[i, 0] = float(readline.split(',')[0])
#     returnData[i, 1] = float(readline.split(',')[1])
#     returnData[i, 2] = float(readline.split(',')[2])
#     returnData[i, 3] = float(readline.split(',')[3])
#     returnData[i, 4] = float(readline.split(',')[4])
#     returnData[i, 5] = float(readline.split(',')[5])
#     # returnData[i, 6] = float(readline.split(',')[6])
#     # returnData[i, 7] = float(readline.split(',')[7])
#     # returnData[i, 8] = float(readline.split(',')[8])
#     # returnData[i, 9] = float(readline.split(',')[9])
#     # returnData[i, 10] = float(readline.split(',')[10])
#     i = i + 1
# readfile.close()
#
# returnData = returnData[:100000, :]
# writefilePosition = open('Data/cutArea/L1C2_Normalization_cut.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for j in range(len(returnData)):
#     writefilePosition.writelines([str(returnData[j, 0]), ', ', str(returnData[j, 1]), ', ',str(returnData[j, 2]), ', ',
#                                   str(returnData[j, 3]), ', ', str(returnData[j, 4]), ', ', str(returnData[j, 5]),  '\n'])
#     # ', ', str(returnData[j, 5]), ', ', str(returnData[j, 6]), ', ',
#     # str(returnData[j, 7]), ', ', str(returnData[j, 8]), \
#     # ', ', str(returnData[j, 9]), ', ', str(returnData[j, 10]),
# writefilePosition.close()


#
# # 生成10个文件夹
# for i in range(10):
#     path_train = 'Data/cutArea/NormalizedData/OptimalKNN(Weinmann)/test/{bulk}'
#     np.os.makedirs(path_train.format(bulk=i))


# # 生成180个文件夹
# for i in range(180):
#     path_train = 'Data/cutArea/train_test/train/1/{bulk}'
#     # path_train = 'Data/cutArea/MyMaxEnt/train/1/{bulk}'
#     np.os.makedirs(path_train.format(bulk=i))



# readfile = open('Data/cutArea/train_test/test/9/L1C2_addC1C3_test.txt', "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData = np.empty([lineNum, 10], dtype=float)
#
# for readline in readAllLine:
#     returnData[i, 0] = float(readline.split(', ')[0])
#     returnData[i, 1] = float(readline.split(', ')[1])
#     returnData[i, 2] = float(readline.split(', ')[2])
#     returnData[i, 3] = float(readline.split(', ')[3])
#     returnData[i, 4] = float(readline.split(', ')[4])
#     returnData[i, 5] = float(readline.split(', ')[5])
#     returnData[i, 6] = float(readline.split(', ')[6])
#     returnData[i, 7] = float(readline.split(', ')[7])
#     returnData[i, 8] = float(readline.split(', ')[8])
#     returnData[i, 9] = float(readline.split(', ')[9])
#     i = i + 1
# readfile.close()
#
# # for i in range(200):
# for i in range(116):
#     path_w = 'Data/cutArea/train_test/test/9/{bulk}/'
#     writefilePosition = open(path_w.format(bulk=i) + 'L1C2_addC1C3_test.txt', "a")
#     writefilePosition.seek(0)
#     writefilePosition.truncate()
#     a = 1000  # train
#     if i < 115:
#         num_left = i * a
#         num_right = (i+1) * a
#     else:
#         num_left = i * a
#         num_right = len(returnData)
#     for j in range(num_left, num_right):
#         writefilePosition.writelines([str(returnData[j, 0]), ', ', str(returnData[j, 1]), ', ', str(returnData[j, 2]), \
#                                       ', ', str(returnData[j, 3]), ', ', str(returnData[j, 4]), ', ', str(returnData[j, 5]), \
#                                       ', ', str(returnData[j, 6]), ', ', str(returnData[j, 7]), ', ', str(returnData[j, 8]),\
#                                       ', ', str(returnData[j, 9]), '\n'])
#     writefilePosition.close()

# for m in range(10):
#     path_w = 'Data/cutArea/train_test/test/{bulk}/'
#     writefilePosition = open(path_w.format(bulk=m) + 'L1C2_addC1C3_test1.txt', "a")
#     writefilePosition.seek(0)
#     writefilePosition.truncate()
#     a = 180000  # train
#     if m < 9:
#         num_left = 1797091 + m * a
#         num_right = 1797091 + (m+1) * a
#     else:
#         num_left = 1797091 + m * a
#         num_right = len(returnData)
#     for j in range(num_left, num_right):
#         writefilePosition.writelines([str(returnData[j, 0]), ', ', str(returnData[j, 1]), ', ', str(returnData[j, 2]), \
#                                       ', ', str(returnData[j, 3]), ', ', str(returnData[j, 4]), ', ', str(returnData[j, 5]), \
#                                       ', ', str(returnData[j, 6]), ', ', str(returnData[j, 7]), ', ', str(returnData[j, 8]),\
#                                       ', ', str(returnData[j, 9]), '\n'])
#     writefilePosition.close()


# readfile = open('Data/cutArea/train_test/train/L1C2_addC1C3_train.txt', "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData = np.empty([lineNum, 10], dtype=float)
#
# for readline in readAllLine:
#     returnData[i, 0] = float(readline.split(', ')[0])
#     returnData[i, 1] = float(readline.split(', ')[1])
#     returnData[i, 2] = float(readline.split(', ')[2])
#     returnData[i, 3] = float(readline.split(', ')[3])
#     returnData[i, 4] = float(readline.split(', ')[4])
#     returnData[i, 5] = float(readline.split(', ')[5])
#     returnData[i, 6] = float(readline.split(', ')[6])
#     returnData[i, 7] = float(readline.split(', ')[7])
#     returnData[i, 8] = float(readline.split(', ')[8])
#     returnData[i, 9] = float(readline.split(', ')[9])
#     i = i + 1
# readfile.close()
#
# for i in range(10):
#     path_w = 'Data/cutArea/train_test/train/{bulk}/'
#     writefilePosition = open(path_w.format(bulk=i) + 'L1C2_addC1C3_train.txt', "a")
#     writefilePosition.seek(0)
#     writefilePosition.truncate()
#     # a = 20000
#     a = 180000  # train
#     # a = 17247  # test
#     # if i < 180:
#     # if i < 175:
#     if i < 9:
#         num_left = i * a
#         num_right = (i+1) * a
#     else:
#         num_left = i * a
#         num_right = len(returnData)
#     # for i in range(len(returnData)):
#     for j in range(num_left, num_right):
#         writefilePosition.writelines([str(returnData[j, 0]), ', ', str(returnData[j, 1]), ', ', str(returnData[j, 2]), \
#                                       ', ', str(returnData[j, 3]), ', ', str(returnData[j, 4]), ', ', str(returnData[j, 5]), \
#                                       ', ', str(returnData[j, 6]), ', ', str(returnData[j, 7]), ', ', str(returnData[j, 8]),\
#                                       ', ', str(returnData[j, 9]),'\n'])
#     writefilePosition.close()






#
# # 合并180个文件
# path_w = 'Data/cutArea/MyMaxEnt/train/0/'
# writefilePosition = open(path_w + 'featureVector_ch3.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
#
# path_r = 'Data/cutArea/MyMaxEnt/train/0/{bulk}/featureVector_ch3.txt'
# for i in range(180):  # 176   # 118
#     readfile = open(path_r.format(bulk=i), "r")
#     readAllLine = readfile.readlines()
#     lineNum = len(readAllLine)
#     i = 0
#     returnData = np.empty([lineNum, 18], dtype=float)
#
#     for readline in readAllLine:
#         returnData[i, 0] = float(readline.split(', ')[0])
#         returnData[i, 1] = float(readline.split(', ')[1])
#         returnData[i, 2] = float(readline.split(', ')[2])
#         returnData[i, 3] = float(readline.split(', ')[3])
#         returnData[i, 4] = float(readline.split(', ')[4])
#         returnData[i, 5] = float(readline.split(', ')[5])
#         returnData[i, 6] = float(readline.split(', ')[6])
#         returnData[i, 7] = float(readline.split(', ')[7])
#         returnData[i, 8] = float(readline.split(', ')[8])
#         returnData[i, 9] = float(readline.split(', ')[9])
#         returnData[i, 10] = float(readline.split(', ')[10])
#         returnData[i, 11] = float(readline.split(', ')[11])
#         returnData[i, 12] = float(readline.split(', ')[12])
#         returnData[i, 13] = float(readline.split(', ')[13])
#         returnData[i, 14] = float(readline.split(', ')[14])
#         returnData[i, 15] = float(readline.split(', ')[15])
#         returnData[i, 16] = float(readline.split(', ')[16])
#         returnData[i, 17] = float(readline.split(', ')[17])
#         i = i + 1
#     readfile.close()
#
#     for j in range(len(returnData)):
#         writefilePosition.writelines([str(returnData[j, 0]), ', ', str(returnData[j, 1]), ', ', str(returnData[j, 2]), \
#                                       ', ', str(returnData[j, 3]), ', ', str(returnData[j, 4]), ', ', str(returnData[j, 5]), \
#                                       ', ', str(returnData[j, 6]), ', ', str(returnData[j, 7]), ', ', str(returnData[j, 8]),\
#                                       ', ', str(returnData[j, 9]), ', ', str(returnData[j, 10]), ', ', str(returnData[j, 11]),
#                                       ', ', str(returnData[j, 12]), ', ', str(returnData[j, 13]), ', ', str(returnData[j, 14]),
#                                       ', ', str(returnData[j, 15]), ', ', str(returnData[j, 16]), ', ', str(returnData[j, 17]), '\n'])
# writefilePosition.close()



# # 合并10个文件
# path_w = 'Data/cutArea/MyMaxEnt/train/'
# writefilePosition = open(path_w + 'featureVector_e213.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()

# # path_r = 'Data/cutArea/MultiScaleCylindrical/test/{bulk}/featureVector.txt'
# path_r = 'Data/cutArea/MyMaxEnt/train/{bulk}/featureVector_e213.txt'
# for n in range(10):
#     readfile = open(path_r.format(bulk=n), "r")
#     readAllLine = readfile.readlines()
#     lineNum = len(readAllLine)
#     i = 0
#     returnData = np.empty([lineNum, 18], dtype=float)
#     for readline in readAllLine:
#         returnData[i, 0] = float(readline.split(', ')[0])
#         returnData[i, 1] = float(readline.split(', ')[1])
#         returnData[i, 2] = float(readline.split(', ')[2])
#         returnData[i, 3] = float(readline.split(', ')[3])
#         returnData[i, 4] = float(readline.split(', ')[4])
#         returnData[i, 5] = float(readline.split(', ')[5])
#         returnData[i, 6] = float(readline.split(', ')[6])
#         returnData[i, 7] = float(readline.split(', ')[7])
#         returnData[i, 8] = float(readline.split(', ')[8])
#         returnData[i, 9] = float(readline.split(', ')[9])
#         returnData[i, 10] = float(readline.split(', ')[10])
#         returnData[i, 11] = float(readline.split(', ')[11])
#         returnData[i, 12] = float(readline.split(', ')[12])
#         returnData[i, 13] = float(readline.split(', ')[13])
#         returnData[i, 14] = float(readline.split(', ')[14])
#         returnData[i, 15] = float(readline.split(', ')[15])
#         returnData[i, 16] = float(readline.split(', ')[16])
#         returnData[i, 17] = float(readline.split(', ')[17])
#         # returnData[i, 18] = float(readline.split(', ')[18])
#         # returnData[i, 19] = float(readline.split(', ')[19])
#         # returnData[i, 20] = float(readline.split(', ')[20])
#         # returnData[i, 21] = float(readline.split(', ')[21])
#         # returnData[i, 22] = float(readline.split(', ')[22])
#         # returnData[i, 23] = float(readline.split(', ')[23])
#         # returnData[i, 24] = float(readline.split(', ')[24])
#         # returnData[i, 25] = float(readline.split(', ')[25])
#         # returnData[i, 26] = float(readline.split(', ')[26])
#         # returnData[i, 27] = float(readline.split(', ')[27])
#         # returnData[i, 28] = float(readline.split(', ')[28])
#         # returnData[i, 29] = float(readline.split(', ')[29])
#         # returnData[i, 30] = float(readline.split(', ')[30])
#         # returnData[i, 31] = float(readline.split(', ')[31])
#         # returnData[i, 32] = float(readline.split(', ')[32])
#         # returnData[i, 33] = float(readline.split(', ')[33])
#         # returnData[i, 34] = float(readline.split(', ')[34])
#         # returnData[i, 35] = float(readline.split(', ')[35])
#         # returnData[i, 36] = float(readline.split(', ')[36])
#         # returnData[i, 37] = float(readline.split(', ')[37])
#         # returnData[i, 38] = float(readline.split(', ')[38])
#         # returnData[i, 39] = float(readline.split(', ')[39])
#         # returnData[i, 40] = float(readline.split(', ')[40])
#         # returnData[i, 41] = float(readline.split(', ')[41])
#         # returnData[i, 42] = float(readline.split(', ')[42])
#         # returnData[i, 43] = float(readline.split(', ')[43])
#         # returnData[i, 44] = float(readline.split(', ')[44])
#         # returnData[i, 45] = float(readline.split(', ')[45])
#         # returnData[i, 46] = float(readline.split(', ')[46])
#         # returnData[i, 47] = float(readline.split(', ')[47])
#         # returnData[i, 48] = float(readline.split(', ')[48])
#         # returnData[i, 49] = float(readline.split(', ')[49])
#         i = i + 1
#     readfile.close()
#
#     for j in range(len(returnData)):
#         writefilePosition.writelines([str(returnData[j, 0]), ', ', str(returnData[j, 1]), ', ', str(returnData[j, 2]), \
#                     ', ', str(returnData[j, 3]), ', ', str(returnData[j, 4]), ', ', str(returnData[j, 5]), \
#                     ', ', str(returnData[j, 6]), ', ', str(returnData[j, 7]), ', ', str(returnData[j, 8]), \
#                     ', ', str(returnData[j, 9]), ', ', str(returnData[j, 10]), ', ', str(returnData[j, 11]),
#                     ', ', str(returnData[j, 12]), ', ', str(returnData[j, 13]), ', ', str(returnData[j, 14]),
#                     ', ', str(returnData[j, 15]), ', ', str(returnData[j, 16]), ', ', str(returnData[j, 17]), '\n'])
#
#
#     # for j in range(len(returnData)):
#     #     writefilePosition.writelines([str(returnData[j, 0]), ', ', str(returnData[j, 1]), ', ', str(returnData[j, 2]), \
#     #                                   ', ', str(returnData[j, 3]), ', ', str(returnData[j, 4]), ', ', str(returnData[j, 5]), \
#     #                                   ', ', str(returnData[j, 6]), ', ', str(returnData[j, 7]), ', ', str(returnData[j, 8]),\
#     #                                   ', ', str(returnData[j, 9]), ', ', str(returnData[j, 10]), ', ', str(returnData[j, 11]),
#     #                                   ', ', str(returnData[j, 12]), ', ', str(returnData[j, 13]), ', ', str(returnData[j, 14]),
#     #                                   ', ', str(returnData[j, 15]), ', ', str(returnData[j, 16]),  ', ', str(returnData[j, 17]),
#     #                                   ', ', str(returnData[j, 18]), ', ', str(returnData[j, 19]),  ', ', str(returnData[j, 20]),
#     #                                   ', ', str(returnData[j, 21]), ', ', str(returnData[j, 22]),  ', ', str(returnData[j, 23]),
#     #                                   ', ', str(returnData[j, 24]), ', ', str(returnData[j, 25]),  ', ', str(returnData[j, 26]),
#     #                                   ', ', str(returnData[j, 27]), ', ', str(returnData[j, 28]),  ', ', str(returnData[j, 29]),
#     #                                   ', ', str(returnData[j, 30]), ', ', str(returnData[j, 31]),  ', ', str(returnData[j, 32]),
#     #                                   ', ', str(returnData[j, 33]), ', ', str(returnData[j, 34]),  ', ', str(returnData[j, 35]),
#     #                                   ', ', str(returnData[j, 36]), ', ', str(returnData[j, 37]),  ', ', str(returnData[j, 38]),
#     #                                   ', ', str(returnData[j, 39]), ', ', str(returnData[j, 40]),  ', ', str(returnData[j, 41]),
#     #                                   ', ', str(returnData[j, 42]), ', ', str(returnData[j, 43]),  ', ', str(returnData[j, 44]),
#     #                                   ', ', str(returnData[j, 45]), ', ', str(returnData[j, 46]),  ', ', str(returnData[j, 47]),
#     #                                   ', ', str(returnData[j, 48]), ', ', str(returnData[j, 49]), '\n'])
# writefilePosition.close()
#


# # 合并train 和 test
# # path_r = 'Data/cutArea/MultiScaleCylindrical/test/{bulk}/featureVector.txt'
# path_r = 'Data/cutArea/MyMaxEnt/train/featureVector_e312.txt'
# readfile = open(path_r, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData1 = np.empty([lineNum, 17], dtype=float)
# for readline in readAllLine:
#     returnData1[i, 0] = float(readline.split(', ')[0])
#     returnData1[i, 1] = float(readline.split(', ')[1])
#     returnData1[i, 2] = float(readline.split(', ')[2])
#     returnData1[i, 3] = float(readline.split(', ')[3])
#     returnData1[i, 4] = float(readline.split(', ')[4])
#     returnData1[i, 5] = float(readline.split(', ')[5])
#     returnData1[i, 6] = float(readline.split(', ')[6])
#     returnData1[i, 7] = float(readline.split(', ')[7])
#     returnData1[i, 8] = float(readline.split(', ')[8])
#     returnData1[i, 9] = float(readline.split(', ')[9])
#     returnData1[i, 10] = float(readline.split(', ')[10])
#     returnData1[i, 11] = float(readline.split(', ')[11])
#     returnData1[i, 12] = float(readline.split(', ')[12])
#     returnData1[i, 13] = float(readline.split(', ')[13])
#     returnData1[i, 14] = float(readline.split(', ')[14])
#     returnData1[i, 15] = float(readline.split(', ')[15])
#     returnData1[i, 16] = float(readline.split(', ')[16])
#     i = i + 1
# readfile.close()
#
# path_r = 'Data/cutArea/MyMaxEnt/test/featureVector_e312.txt'
# readfile = open(path_r, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData2 = np.empty([lineNum, 17], dtype=float)
# for readline in readAllLine:
#     returnData2[i, 0] = float(readline.split(', ')[0])
#     returnData2[i, 1] = float(readline.split(', ')[1])
#     returnData2[i, 2] = float(readline.split(', ')[2])
#     returnData2[i, 3] = float(readline.split(', ')[3])
#     returnData2[i, 4] = float(readline.split(', ')[4])
#     returnData2[i, 5] = float(readline.split(', ')[5])
#     returnData2[i, 6] = float(readline.split(', ')[6])
#     returnData2[i, 7] = float(readline.split(', ')[7])
#     returnData2[i, 8] = float(readline.split(', ')[8])
#     returnData2[i, 9] = float(readline.split(', ')[9])
#     returnData2[i, 10] = float(readline.split(', ')[10])
#     returnData2[i, 11] = float(readline.split(', ')[11])
#     returnData2[i, 12] = float(readline.split(', ')[12])
#     returnData2[i, 13] = float(readline.split(', ')[13])
#     returnData2[i, 14] = float(readline.split(', ')[14])
#     returnData2[i, 15] = float(readline.split(', ')[15])
#     returnData2[i, 16] = float(readline.split(', ')[16])
#     i = i + 1
# readfile.close()
#
#
# returnData = np.vstack((returnData1, returnData2))
#
#
# path_r = '../dataCorrect/L1C2_addC1C3_train_test_correct.txt'
# readfile = open(path_r, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData3 = np.empty([lineNum, 1], dtype=float)
# for readline in readAllLine:
#     returnData3[i, 0] = float(readline.split(', ')[5])
#     i = i + 1
# readfile.close()
#
# returnDataLabel = np.hstack((returnData, returnData3))
#
# path_w = 'Data/cutArea/MyMaxEnt/'
# writefilePosition = open(path_w + 'featureVector_e312_addLabel.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for j in range(len(returnDataLabel)):
#     writefilePosition.writelines([str(returnDataLabel[j, 0]), ', ', str(returnDataLabel[j, 1]), ', ', str(returnDataLabel[j, 2]), \
#                 ', ', str(returnDataLabel[j, 3]), ', ', str(returnDataLabel[j, 4]), ', ', str(returnDataLabel[j, 5]), \
#                 ', ', str(returnDataLabel[j, 6]), ', ', str(returnDataLabel[j, 7]), ', ', str(returnDataLabel[j, 8]), \
#                 ', ', str(returnDataLabel[j, 9]), ', ', str(returnDataLabel[j, 10]), ', ', str(returnDataLabel[j, 11]),
#                 ', ', str(returnDataLabel[j, 12]), ', ', str(returnDataLabel[j, 13]), ', ', str(returnDataLabel[j, 14]),
#                 ', ', str(returnDataLabel[j, 15]), ', ', str(returnDataLabel[j, 16]), ', ', str(returnDataLabel[j, 17]), '\n'])
# writefilePosition.close()



# sumNeighbor = 0
# path_r = 'Data/cutArea/MyMaxEnt/train/featureVector_e312.txt'
# readfile = open(path_r, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData1 = np.empty([lineNum, 2], dtype=float)
# for readline in readAllLine:
#     returnData1[i, 0] = float(readline.split(', ')[0])
#     returnData1[i, 1] = float(readline.split(', ')[1])
#     sumNeighbor = sumNeighbor + returnData1[i, 1]
#
#
# path_r = 'Data/cutArea/MyMaxEnt/test/featureVector_e312.txt'
# readfile = open(path_r, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData2 = np.empty([lineNum, 2], dtype=float)
# for readline in readAllLine:
#     returnData2[i, 0] = float(readline.split(', ')[0])
#     returnData2[i, 1] = float(readline.split(', ')[1])
#     sumNeighbor = sumNeighbor + returnData2[i, 1]
#
# mean = sumNeighbor/(len(returnData1)+len(returnData2))
# print(mean)




# readfile = open('Data/cutArea/MyOptimalNeighbor/test/0/bulk180/169/L1C2_test_addC1C3_bulk180.txt', "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData = np.empty([lineNum, 10], dtype=float)
#
# for readline in readAllLine:
#     returnData[i, 0] = float(readline.split(', ')[0])
#     returnData[i, 1] = float(readline.split(', ')[1])
#     returnData[i, 2] = float(readline.split(', ')[2])
#     returnData[i, 3] = float(readline.split(', ')[3])
#     returnData[i, 4] = float(readline.split(', ')[4])
#     returnData[i, 5] = float(readline.split(', ')[5])
#     returnData[i, 6] = float(readline.split(', ')[6])
#     returnData[i, 7] = float(readline.split(', ')[7])
#     returnData[i, 8] = float(readline.split(', ')[8])
#     returnData[i, 9] = float(readline.split(', ')[9])
#     returnData[i, 10] = float(readline.split(', ')[10])
#     returnData[i, 11] = float(readline.split(', ')[11])
#     returnData[i, 12] = float(readline.split(', ')[12])
#     returnData[i, 13] = float(readline.split(', ')[13])
#     returnData[i, 14] = float(readline.split(', ')[14])
#     returnData[i, 15] = float(readline.split(', ')[15])
#     returnData[i, 16] = float(readline.split(', ')[16])
#     i = i + 1
# readfile.close()
#
# for i in range(10):
# path_w = 'Data/cutArea/MyOptimalNeighbor/test/0/bulk180/169/'
# writefilePosition = open(path_w.format(bulk=i) + 'L1C2_test_addC1C3_bulk180_8.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# # a = 1000  # train
# # if i < 179:
# #     num_left = i * a
# #     num_right = (i+1) * a
# # else:
# #     num_left = i * a
# #     num_right = len(returnData)
# num_left = 800
# num_right = 900
# for j in range(num_left, num_right):
#     writefilePosition.writelines([str(returnData[j, 0]), ', ', str(returnData[j, 1]), ', ', str(returnData[j, 2]), \
#                                   ', ', str(returnData[j, 3]), ', ', str(returnData[j, 4]), ', ', str(returnData[j, 5]), \
#                                   ', ', str(returnData[j, 6]), ', ', str(returnData[j, 7]), ', ', str(returnData[j, 8]),\
#                                   ', ', str(returnData[j, 9]),'\n'])
# writefilePosition.close()





# # 重写txt文件
# # path_r = 'Data/cutArea/train_test/train/0/pointAnalysis/data_cut.txt'  # train_test/bulk/train/0/
# path_r = '../dataCorrect/L1C2_addC1C3_train_test_correct1.txt'
# readfile = open(path_r, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData = np.empty([lineNum, 10], dtype=float)
# for readline in readAllLine:
#     returnData[i, 0] = float(readline.split(',')[1])
#     returnData[i, 1] = float(readline.split(',')[2])
#     returnData[i, 2] = float(readline.split(',')[3])
#     returnData[i, 3] = float(readline.split(',')[4])
#     returnData[i, 4] = float(readline.split(',')[5])
#     returnData[i, 5] = float(readline.split(',')[6])
#     returnData[i, 6] = float(readline.split(',')[7])
#     returnData[i, 7] = float(readline.split(',')[8])
#     returnData[i, 8] = float(readline.split(',')[9])
#     returnData[i, 9] = float(readline.split(',')[10])
#     # returnData[i, 10] = float(readline.split(',')[11])
#     # returnData[i, 11] = float(readline.split(',')[12])
#     i = i + 1
# readfile.close()
#
#
# for k in range(len(returnData)):
#     if returnData[k, 5] == 2:
#         if returnData[k, 3] < 2.5:
#             returnData[k, 5] = 0
#
# # path_w = 'Data/cutArea/train_test/train/0/pointAnalysis/'
# path_w = '../dataCorrect/'
# writefilePosition = open(path_w + 'L1C2_addC1C3_train_test_correct2.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for j in range(len(returnData)):
#     writefilePosition.writelines([str(returnData[j, 0]), ', ', str(returnData[j, 1]), ', ', str(returnData[j, 2]),
#                                   ', ', str(returnData[j, 3]), ', ', str(returnData[j, 4]), ', ', str(returnData[j, 5]),
#                                   ', ', str(returnData[j, 6]), ', ', str(returnData[j, 7]), ', ', str(returnData[j, 8]),
#                                   ', ', str(returnData[j, 9]),  '\n'])  # ', ', str(returnData[j, 10]), ', ', str(returnData[j, 11]),
# writefilePosition.close()



# path_r = '../dataCorrect/L1C2_addC1C3_train_test_correct_2.txt'
# readfile = open(path_r, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData2 = np.empty([lineNum, 1], dtype=float)
# for readline in readAllLine:
#     # returnData2[i, 0] = float(readline.split(',')[1])
#     # returnData2[i, 1] = float(readline.split(',')[2])
#     # returnData2[i, 2] = float(readline.split(',')[3])
#     # returnData2[i, 3] = float(readline.split(',')[4])
#     # returnData2[i, 4] = float(readline.split(',')[5])
#     returnData2[i, 0] = float(readline.split(',')[5])
#     # returnData2[i, 6] = float(readline.split(',')[7])
#     # returnData2[i, 7] = float(readline.split(',')[8])
#     # returnData2[i, 8] = float(readline.split(',')[9])
#     # returnData2[i, 9] = float(readline.split(',')[10])
#     i = i + 1
# readfile.close()
# #
# path_r = '../dataCorrect/L1C2_addC1C3_train_test_correct_2.txt'
# readfile = open(path_r, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData3 = np.empty([lineNum, 10], dtype=float)
# for readline in readAllLine:
#     returnData3[i, 0] = float(readline.split(',')[0])
#     returnData3[i, 1] = float(readline.split(',')[1])
#     returnData3[i, 2] = float(readline.split(',')[2])
#     returnData3[i, 3] = float(readline.split(',')[3])
#     returnData3[i, 4] = float(readline.split(',')[4])
#     returnData3[i, 5] = float(readline.split(',')[5])
#     returnData3[i, 6] = float(readline.split(',')[6])
#     returnData3[i, 7] = float(readline.split(',')[7])
#     returnData3[i, 8] = float(readline.split(',')[8])
#     returnData3[i, 9] = float(readline.split(',')[9])
#     i = i + 1
# readfile.close()
#
# for i in range(len(returnData3)):
#     if returnData3[i, 5] == 6:
#         if returnData3[i, 3] > 0.2:
#             returnData3[i, 5] = 4
#         else:
#             returnData3[i, 5] = 6
#
# # path_w = 'Data/cutArea/train_test/train/0/pointAnalysis/'
# path_w = '../dataCorrect/'
# writefilePosition = open(path_w + 'L1C2_addC1C3_train_test_correct_3.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for j in range(len(returnData3)):
#     writefilePosition.writelines([str(returnData3[j, 0]), ', ', str(returnData3[j, 1]), ', ', str(returnData3[j, 2]),
#                                   ', ', str(returnData3[j, 3]), ', ', str(returnData3[j, 4]), ', ', str(returnData3[j, 5]),
#                                   ', ', str(returnData3[j, 6]), ', ', str(returnData3[j, 7]), ', ', str(returnData3[j, 8]),
#                                   ', ', str(returnData3[j, 9]),  '\n'])  # ', ', str(returnData[j, 10]), ', ', str(returnData[j, 11]),
# writefilePosition.close()



# # 重写txt文件
# def read(path):
#     readfile = open(path, "r")
#     readAllLine = readfile.readlines()
#     lineNum = len(readAllLine)
#     i = 0
#     returnData = np.empty([lineNum, 12], dtype=float)
#     for readline in readAllLine:
#         returnData[i, 0] = float(readline.split(',')[0])
#         returnData[i, 1] = float(readline.split(',')[1])
#         returnData[i, 2] = float(readline.split(',')[2])
#         returnData[i, 3] = float(readline.split(',')[3])
#         returnData[i, 4] = float(readline.split(',')[4])
#         returnData[i, 5] = float(readline.split(',')[5])
#         returnData[i, 6] = float(readline.split(',')[6])
#         returnData[i, 7] = float(readline.split(',')[7])
#         returnData[i, 8] = float(readline.split(',')[8])
#         returnData[i, 9] = float(readline.split(',')[9])
#         returnData[i, 10] = float(readline.split(',')[10])
#         returnData[i, 11] = float(readline.split(',')[11])
#         i = i + 1
#     readfile.close()
#     return returnData
#
# data0 = read('Data/cutArea/train_test/trainingSample/road.txt')
# data1 = read('Data/cutArea/train_test/trainingSample/grass.txt')
# # data2 = read('Data/cutArea/train_test/trainingSample/road_2.txt')
# # data3 = read('Data/cutArea/train_test/trainingSample/road_3.txt')
# # data4 = read('Data/cutArea/train_test/trainingSample/road_4.txt')
# # data5 = read('Data/cutArea/train_test/trainingSample/road_5.txt')
# # data6 = read('Data/cutArea/train_test/trainingSample/road_6.txt')
# # data7 = read('Data/cutArea/train_test/trainingSample/road_7.txt')
# # data8 = read('Data/cutArea/train_test/trainingSample/road_8.txt')
# # data9 = read('Data/cutArea/train_test/trainingSample/road_9.txt')
# # data10 = read('Data/cutArea/train_test/trainingSample/road_10.txt')
# # data11 = read('Data/cutArea/train_test/trainingSample/road_11.txt')
# # data12 = read('Data/cutArea/train_test/trainingSample/road_12.txt')
# # data13 = read('Data/cutArea/train_test/trainingSample/road_13.txt')
# # data14 = read('Data/cutArea/train_test/trainingSample/road_14.txt')
# # data15 = read('Data/cutArea/train_test/trainingSample/road_15.txt')
# # data16 = read('Data/cutArea/train_test/trainingSample/road_16.txt')
# # data17 = read('Data/cutArea/train_test/trainingSample/road_17.txt')
# data = np.vstack((data0,data1))
# # data = np.vstack((data,data2))
# # data = np.vstack((data,data3))
# # data = np.vstack((data,data4))
# # data = np.vstack((data,data5))
# # data = np.vstack((data,data6))
# # data = np.vstack((data,data7))
# # data = np.vstack((data,data8))
# # data = np.vstack((data,data9))
# # data = np.vstack((data,data10))
# # data = np.vstack((data,data11))
# # data = np.vstack((data,data12))
# # data = np.vstack((data,data13))
# # data = np.vstack((data,data14))
# # data = np.vstack((data,data15))
# # data = np.vstack((data,data16))
# # data = np.vstack((data,data17))
#
# path_w = 'Data/cutArea/train_test/trainingSample/'
# writefilePosition = open(path_w + 'ground.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for j in range(len(data)):
#     writefilePosition.writelines([str(data[j, 0]), ', ', str(data[j, 1]), ', ', str(data[j, 2]),
#                                   ', ', str(data[j, 3]), ', ', str(data[j, 4]), ', ', str(data[j, 5]),
#                                   ', ', str(data[j, 6]), ', ', str(data[j, 7]), ', ', str(data[j, 8]),
#                                   ', ', str(data[j, 9]), ', ', str(data[j, 10]), ', ', str(data[j, 11]), '\n'])
# writefilePosition.close()




# # 找出错误的行数和ID
# path_r1 = 'Data/cutArea/train_test/bulk/test/9/L1C2_test_addC1C3.txt'
# readfile = open(path_r1, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData1 = np.empty([lineNum, 10], dtype=float)
#
# for readline in readAllLine:
#     returnData1[i, 0] = float(readline.split(', ')[0])
#     returnData1[i, 1] = float(readline.split(', ')[1])
#     returnData1[i, 2] = float(readline.split(', ')[2])
#     returnData1[i, 3] = float(readline.split(', ')[3])
#     returnData1[i, 4] = float(readline.split(', ')[4])
#     returnData1[i, 5] = float(readline.split(', ')[5])
#     returnData1[i, 6] = float(readline.split(', ')[6])
#     returnData1[i, 7] = float(readline.split(', ')[7])
#     returnData1[i, 8] = float(readline.split(', ')[8])
#     returnData1[i, 9] = float(readline.split(', ')[9])
#     i = i + 1
# readfile.close()
#
# path_r2 = 'Data/cutArea/MyOptimalNeighbor/test/wrong/9/L1C2_test_featureVector_maxEnt_e.txt'
# readfile = open(path_r2, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData2 = np.empty([lineNum, 1], dtype=float)
#
# for readline in readAllLine:
#     returnData2[i, 0] = float(readline.split(', ')[0])
#     i = i + 1
# readfile.close()
#
# path_w = 'Data/cutArea/MyOptimalNeighbor/update/test/9/'
# writefilePosition = open(path_w + 'wrong_ID_data.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for i in range(len(returnData1)):
#     if returnData1[i, 0] - returnData2[i, 0] != 0:
#         print(returnData1[i, 0])
#         writefilePosition.writelines([str(i), ', ', str(returnData1[i, 0]), ', ', str(returnData1[i, 1]),
#                                       ', ', str(returnData1[i, 2]), ', ', str(returnData1[i, 3]), ', ', str(returnData1[i, 4]),
#                                       ', ', str(returnData1[i, 5]), ', ', str(returnData1[i, 6]), ', ', str(returnData1[i, 7]),
#                                       ', ', str(returnData1[i, 8]), ', ', str(returnData1[i, 9]),'\n'])
# writefilePosition.close()





# #将改后的正确数据插入
# path_r1 = 'Data/cutArea/MyOptimalNeighbor/update/test/9/L1C2_test_featureVector_maxEnt_e.txt'
# readfile = open(path_r1, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData1 = np.empty([lineNum, 17], dtype=float)
#
# for readline in readAllLine:
#     returnData1[i, 0] = float(readline.split(', ')[0])
#     returnData1[i, 1] = float(readline.split(', ')[1])
#     returnData1[i, 2] = float(readline.split(', ')[2])
#     returnData1[i, 3] = float(readline.split(', ')[3])
#     returnData1[i, 4] = float(readline.split(', ')[4])
#     returnData1[i, 5] = float(readline.split(', ')[5])
#     returnData1[i, 6] = float(readline.split(', ')[6])
#     returnData1[i, 7] = float(readline.split(', ')[7])
#     returnData1[i, 8] = float(readline.split(', ')[8])
#     returnData1[i, 9] = float(readline.split(', ')[9])
#     returnData1[i, 10] = float(readline.split(', ')[10])
#     returnData1[i, 11] = float(readline.split(', ')[11])
#     returnData1[i, 12] = float(readline.split(', ')[12])
#     returnData1[i, 13] = float(readline.split(', ')[13])
#     returnData1[i, 14] = float(readline.split(', ')[14])
#     returnData1[i, 15] = float(readline.split(', ')[15])
#     returnData1[i, 16] = float(readline.split(', ')[16])
#     i = i + 1
# readfile.close()
#
# path_r2 = 'Data/cutArea/MyOptimalNeighbor/test/wrong/9/L1C2_test_featureVector_maxEnt_e.txt'
# readfile = open(path_r2, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData2 = np.empty([lineNum, 17], dtype=float)
#
# for readline in readAllLine:
#     returnData2[i, 0] = float(readline.split(', ')[0])
#     returnData2[i, 1] = float(readline.split(', ')[1])
#     returnData2[i, 2] = float(readline.split(', ')[2])
#     returnData2[i, 3] = float(readline.split(', ')[3])
#     returnData2[i, 4] = float(readline.split(', ')[4])
#     returnData2[i, 5] = float(readline.split(', ')[5])
#     returnData2[i, 6] = float(readline.split(', ')[6])
#     returnData2[i, 7] = float(readline.split(', ')[7])
#     returnData2[i, 8] = float(readline.split(', ')[8])
#     returnData2[i, 9] = float(readline.split(', ')[9])
#     returnData2[i, 10] = float(readline.split(', ')[10])
#     returnData2[i, 11] = float(readline.split(', ')[11])
#     returnData2[i, 12] = float(readline.split(', ')[12])
#     returnData2[i, 13] = float(readline.split(', ')[13])
#     returnData2[i, 14] = float(readline.split(', ')[14])
#     returnData2[i, 15] = float(readline.split(', ')[15])
#     returnData2[i, 16] = float(readline.split(', ')[16])
#     i = i + 1
# readfile.close()
#
#
# path_r3 = 'Data/cutArea/MyOptimalNeighbor/update/test/9/wrong_ID_data.txt'
# readfile = open(path_r3, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData3 = np.empty([lineNum, 1], dtype=float)
# for readline in readAllLine:
#     returnData3[i, 0] = float(readline.split(', ')[0])
#     i = i + 1
# readfile.close()
#
#
# for i in range(len(returnData3)):
#     id = returnData3[i, 0]
#     returnData2[int(id), :] = returnData1[i, :]
#
#
# path_w = 'Data/cutArea/MyOptimalNeighbor/test/9/'
# writefilePosition = open(path_w + 'L1C2_test_featureVector_maxEnt_e.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for j in range(len(returnData2)):
#     writefilePosition.writelines([str(returnData2[j, 0]), ', ', str(returnData2[j, 1]), ', ', str(returnData2[j, 2]), \
#                           ', ', str(returnData2[j, 3]), ', ', str(returnData2[j, 4]), ', ', str(returnData2[j, 5]), \
#                           ', ', str(returnData2[j, 6]), ', ', str(returnData2[j, 7]), ', ', str(returnData2[j, 8]),\
#                           ', ', str(returnData2[j, 9]), ', ', str(returnData2[j, 10]), ', ', str(returnData2[j, 11]),\
#                           ', ', str(returnData2[j, 12]), ', ', str(returnData2[j, 13]), ', ', str(returnData2[j, 14]),\
#                           ', ', str(returnData2[j, 15]), ', ', str(returnData2[j, 16]), '\n'])
# writefilePosition.close()


# road_all = 255718
# house_all = 338221
# fence_all = 1666
# tree_all = 1442602
# grass_all = 974983
# water_all = 142996
# powerline_all = 4917
# road = 0
# house = 0
# fence = 0
# tree = 0
# grass = 0
# powerline = 0
# water = 0
#
# #计算result accuracy
# path_r1 = 'Data/cutArea/train_test/L1C2_addC1C3_train_test.txt'
# readfile = open(path_r1, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData1 = np.empty([lineNum, 10], dtype=float)
# for readline in readAllLine:
#     returnData1[i, 0] = float(readline.split(', ')[0])
#     returnData1[i, 1] = float(readline.split(', ')[1])
#     returnData1[i, 2] = float(readline.split(', ')[2])
#     returnData1[i, 3] = float(readline.split(', ')[3])
#     returnData1[i, 4] = float(readline.split(', ')[4])
#     returnData1[i, 5] = float(readline.split(', ')[5])
#     returnData1[i, 6] = float(readline.split(', ')[6])
#     returnData1[i, 7] = float(readline.split(', ')[7])
#     returnData1[i, 8] = float(readline.split(', ')[8])
#     returnData1[i, 9] = float(readline.split(', ')[9])
#     i = i + 1
# readfile.close()
#
# path_r2 = 'Data/cutArea/OptimalKNN(Weinmann)/'
# readfile = open(path_r2+'3RandomForests_labelResult.txt', "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData2 = np.empty([lineNum, 1], dtype=float)
# for readline in readAllLine:
#     returnData2[i, 0] = float(readline.split(', ')[1])
#     i = i + 1
# readfile.close()

# correctNum = 0
# for i in range(len(returnData2)):
#     label = returnData1[i, 5]
#     if label == 1:
#         if returnData2[i, 0] == label:
#             road = road + 1
#     elif label == 2:
#         if returnData2[i, 0] == label:
#             house = house + 1
#     elif label == 3:
#         if returnData2[i, 0] == label:
#             fence = fence + 1
#     elif label == 4:
#         if returnData2[i, 0] == label:
#             tree = tree + 1
#     elif label == 5:
#         if returnData2[i, 0] == label:
#             tree = tree + 1
#     elif label == 6:
#         if returnData2[i, 0] == label:
#             grass = grass + 1
#     elif label == 7:
#         if returnData2[i, 0] == label:
#             water = water + 1
#     elif label == 8:
#         if returnData2[i, 0] == label:
#             powerline = powerline + 1
    # if returnData2[i, 0] == returnData1[i, 5]:
    #     correctNum = correctNum + 1
# accu = correctNum / len(returnData2)
# print('correctNum='+str(correctNum)+'; accuracy='+str(accu))
# print('road: '+str(road)+' ; '+str(road/road_all))
# print('house: '+str(house)+' ; '+str(house/house_all))
# print('fence: '+str(fence)+' ; '+str(fence/fence_all))
# print('tree: '+str(tree)+' ; '+str(tree/tree_all))
# print('grass: '+str(grass)+' ; '+str(grass/grass_all))
# print('water: '+str(water)+' ; '+str(water/water_all))
# print('powerline: '+str(powerline)+' ; '+str(powerline/powerline_all))








# #将label添加到数据中
# path_r1 = '../dataCorrect/L1C2_addC1C3_train_test_correct.txt'
# readfile = open(path_r1, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData1 = np.empty([lineNum, 10], dtype=float)
# for readline in readAllLine:
#     returnData1[i, 0] = float(readline.split(', ')[0])
#     returnData1[i, 1] = float(readline.split(', ')[1])
#     returnData1[i, 2] = float(readline.split(', ')[2])
#     returnData1[i, 3] = float(readline.split(', ')[3])
#     returnData1[i, 4] = float(readline.split(', ')[4])
#     returnData1[i, 5] = float(readline.split(', ')[5])
#     returnData1[i, 6] = float(readline.split(', ')[6])
#     returnData1[i, 7] = float(readline.split(', ')[7])
#     returnData1[i, 8] = float(readline.split(', ')[8])
#     returnData1[i, 9] = float(readline.split(', ')[9])
#     i = i + 1
# readfile.close()
#
# path_r2 = 'Data/cutArea/MyMaxEnt/'
# readfile = open(path_r2+'3RandomForests_labelResult_e213.txt', "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData2 = np.empty([lineNum, 1], dtype=float)
# for readline in readAllLine:
#     returnData2[i, 0] = float(readline.split(', ')[1])
#     i = i + 1
# readfile.close()
#
# path_w = path_r2
# writefilePosition = open(path_w + 'rawData_labelResult_e213.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for j in range(len(returnData2)):
#     writefilePosition.writelines([str(returnData1[j, 0]), ', ', str(returnData1[j, 1]), ', ', str(returnData1[j, 2]),
#                           ', ', str(returnData1[j, 3]), ', ', str(returnData1[j, 4]), ', ', str(returnData1[j, 5]),
#                           ', ', str(returnData1[j, 6]), ', ', str(returnData1[j, 7]), ', ', str(returnData1[j, 8]),
#                           ', ', str(returnData1[j, 9]), ', ',  str(returnData2[j, 0]), '\n'])
# writefilePosition.close()




# # 将label添加到数据中
# path_r1 = 'Data/RawData_L1C3_clean.txt'
# readfile = open(path_r1, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData1 = np.empty([lineNum, 5], dtype=float)
# for readline in readAllLine:
#     returnData1[i, 0] = float(readline.split(', ')[0])
#     returnData1[i, 1] = float(readline.split(', ')[1])
#     returnData1[i, 2] = float(readline.split(', ')[2])
#     # returnData1[i, 3] = float(readline.split(', ')[3])
#     returnData1[i, 4] = float(readline.split(', ')[4])
#     # returnData1[i, 5] = float(readline.split(', ')[5])
#     i = i + 1
# readfile.close()
#
# path_r2 = 'Data/RawData_L1C3_clean_nor.txt'
# # path_r2 = 'Data/cutArea/OptimalKNN(Weinmann)/Result/3RandomForests/labelResult.txt'
# readfile = open(path_r2, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# # returnData2 = np.empty([lineNum, 1], dtype=float)
# for readline in readAllLine:
#     returnData1[i, 3] = float(readline.split(' ')[5])
#     i = i + 1
# readfile.close()
#
# path_w = 'Data/'
# # path_w = 'Data/cutArea/OptimalKNN(Weinmann)/Result/3RandomForests/'
# writefilePosition = open(path_w + 'RawData_L1C3_clean_normalization.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for j in range(len(returnData1)):
#     writefilePosition.writelines([str(returnData1[j, 0]), ', ', str(returnData1[j, 1]), ', ', str(returnData1[j, 2]), \
#                           ', ', str(returnData1[j, 3]), ', ', str(returnData1[j, 4]), '\n'])
# writefilePosition.close()








# path_w = 'Data/cutArea/'  # train_test/bulk/train/0/
# writefilePosition = open(path_w + 'L1C3_Normalization_new1.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for j in range(len(returnData)):
#     writefilePosition.writelines([str(returnData[j, 0]), ', ', str(returnData[j, 1]), ', ', str(returnData[j, 2]), \
#                                   ', ', str(returnData[j, 3]), ', ', str(returnData[j, 4]),'\n'])
#     #  ', ', str(returnData[j, 5]),
#     #                                   ', ', str(returnData[j, 6]), ', ', str(returnData[j, 7]), ', ', str(returnData[j, 8]),
#     #                                   ', ', str(returnData[j, 9]),
# writefilePosition.close()



# # 纠正label值
# path_r = '../dataCorrect/L1C2_addC1C3_train_test_correct_1.txt'
# readfile = open(path_r, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData = np.empty([lineNum, 10], dtype=float)
# for readline in readAllLine:
#     returnData[i, 0] = float(readline.split(',')[0])
#     returnData[i, 1] = float(readline.split(',')[1])
#     returnData[i, 2] = float(readline.split(',')[2])
#     returnData[i, 3] = float(readline.split(',')[3])
#     returnData[i, 4] = float(readline.split(',')[4])
#     returnData[i, 5] = float(readline.split(',')[5])
#     returnData[i, 6] = float(readline.split(',')[6])
#     returnData[i, 7] = float(readline.split(',')[7])
#     returnData[i, 8] = float(readline.split(',')[8])
#     returnData[i, 9] = float(readline.split(',')[9])
#     i = i + 1
# readfile.close()
#
# for i in range(len(returnData)):
#     if returnData[i, 5] == 6:
#         if returnData[i, 3] < 0.2:
#             returnData[i, 5] = 6
#         else:
#             returnData[i, 5] = 4
#     elif returnData[i, 5] == 4:
#         if returnData[i, 3] < 0.2:
#             returnData[i, 5] = 6
#         else:
#             returnData[i, 5] = 4
#     elif returnData[i, 5] == 1:
#         if returnData[i, 3] < 0.2:
#             returnData[i, 5] = 1
#         else:
#             returnData[i, 5] = 4
#     elif returnData[i, 5] == 5:
#         if returnData[i, 3] < 0.2:
#             returnData[i, 5] = 6
#         else:
#             returnData[i, 5] = 4
#
# path_w = '../dataCorrect/'
# writefilePosition = open(path_w + 'L1C2_addC1C3_train_test_correct_2.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for j in range(len(returnData)):
#     writefilePosition.writelines([str(returnData[j, 0]), ', ', str(returnData[j, 1]), ', ', str(returnData[j, 2]),
#                                   ', ', str(returnData[j, 3]), ', ', str(returnData[j, 4]), ', ', str(returnData[j, 5]),
#                                   ', ', str(returnData[j, 6]), ', ', str(returnData[j, 7]), ', ', str(returnData[j, 8]),
#                                   ', ', str(returnData[j, 9]),  '\n'])  # ', ', str(returnData[j, 10]), ', ', str(returnData[j, 11]),
# writefilePosition.close()





# # 提取label
# path_r = '../dataCorrect/L1C2_addC1C3_train_test_correct_6.txt'
# readfile = open(path_r, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData = np.empty([lineNum, 10], dtype=float)
# for readline in readAllLine:
#     returnData[i, 0] = float(readline.split(',')[1])
#     returnData[i, 1] = float(readline.split(',')[2])
#     returnData[i, 2] = float(readline.split(',')[3])
#     returnData[i, 3] = float(readline.split(',')[4])
#     returnData[i, 4] = float(readline.split(',')[5])
#     returnData[i, 5] = float(readline.split(',')[6])
#     returnData[i, 6] = float(readline.split(',')[7])
#     returnData[i, 7] = float(readline.split(',')[8])
#     returnData[i, 8] = float(readline.split(',')[9])
#     returnData[i, 9] = float(readline.split(',')[10])
#     i = i + 1
# readfile.close()
#
#
# path_w = '../dataCorrect/'
# writefilePosition = open(path_w + 'Label_train_test_correct.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for j in range(len(returnData)):
#     writefilePosition.writelines([str(returnData[j, 0]), ', ', str(returnData[j, 1]), ', ', str(returnData[j, 2]),
#                                   ', ', str(returnData[j, 3]), ', ', str(returnData[j, 4]), ', ', str(returnData[j, 5]),
#                                   ', ', str(returnData[j, 6]), ', ', str(returnData[j, 7]), ', ', str(returnData[j, 8]),
#                                   ', ', str(returnData[j, 9]),  '\n'])  # ', ', str(returnData[j, 10]), ', ', str(returnData[j, 11]),
# writefilePosition.close()




# path_r= 'Data/cutArea/MyMaxEnt/train/0/featureVector_e312.txt'
# readfile = open(path_r, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# sum = 0
# returnData = np.empty([lineNum, 1], dtype=float)
# for readline in readAllLine:
#     returnData[i, 0] = float(readline.split(',')[17])
#     sum = sum + returnData[i, 0]
#     i = i + 1
# readfile.close()
#
# mean = sum/len(returnData)
# print(mean)


# from scipy.spatial import cKDTree
# meanPointSpacing_L1C2 = 0.547
# radius_large = meanPointSpacing_L1C2 * 6
# neighbor_sum = 0
# point_sum = 0
# path_train = 'Data/cutArea/train_test/train/0/'
#
# neighbor_sum_each = 0
# channel2_data = MyFileOperator.readData_10(path_train + 'L1C2_addC1C3_train.txt')
# tree = cKDTree(channel2_data[:, 1:3])
# indices = tree.query_ball_point(channel2_data[:, 1:3], radius_large)
# for i in range(len(channel2_data)):
#     array = np.array(indices[i])
#     neighbor = channel2_data[array]
#     neighbor_sum_each = neighbor_sum_each + len(neighbor)
# mean_train = neighbor_sum_each/len(channel2_data)
# print(mean_train)
# # neighbor_sum = neighbor_sum + neighbor_sum_each
# # point_sum = point_sum + len(channel2_data)




# # calculate the number of neighbor of cylindrical or spherical
# meanPointSpacing_L1C2 = 0.547
# radius_large = meanPointSpacing_L1C2 * 8
# neighbor_sum = 0
# point_sum = 0
# path_train = 'Data/cutArea/train_test/train/{bulk}/'
# for n in range(10):
#     neighbor_sum_each = 0
#     channel2_data = MyFileOperator.readData_10(path_train.format(bulk=n) + 'L1C2_addC1C3_train.txt')
#     tree = cKDTree(channel2_data[:, 1:3])
#     indices = tree.query_ball_point(channel2_data[:, 1:3], radius_large)
#     for i in range(len(channel2_data)):
#         array = np.array(indices[i])
#         neighbor = channel2_data[array]
#         neighbor_sum_each = neighbor_sum_each + len(neighbor)
#     mean_train = neighbor_sum_each/len(channel2_data)
#     print(mean_train)
#     neighbor_sum = neighbor_sum + neighbor_sum_each
#     point_sum = point_sum + len(channel2_data)
#
# print('------------------------------------')
# path_test = 'Data/cutArea/train_test/test/{bulk}/'
# for n in range(10):
#     neighbor_sum_each = 0
#     channel2_data = MyFileOperator.readData_10(path_test.format(bulk=n) + 'L1C2_addC1C3_test.txt')
#     tree = cKDTree(channel2_data[:, 1:3])
#     indices = tree.query_ball_point(channel2_data[:, 1:3], radius_large)
#     for i in range(len(channel2_data)):
#         array = np.array(indices[i])
#         neighbor = channel2_data[array]
#         neighbor_sum_each = neighbor_sum_each + len(neighbor)
#     mean_test = neighbor_sum_each / len(channel2_data)
#     print(mean_test)
#     neighbor_sum = neighbor_sum + neighbor_sum_each
#     point_sum = point_sum + len(channel2_data)
#
# print('------------------------------------')
# mean = neighbor_sum/point_sum
# print(mean)




# # 每个class的结果分析 overall accuracy
# label_writePath = 'Data/cutArea/MyMaxEnt/3RandomForests_labelResult_e213.txt'
# # label_writePath = 'Data/cutArea/OptimalPauly/3RandomForests_labelResult.txt'
# # label_writePath = 'Data/cutArea/MultiScaleCylindrical/3RandomForests_labelResult.txt'
# readfile = open(label_writePath, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData = np.empty([lineNum, 2], dtype=float)
# for readline in readAllLine:
#     returnData[i, 0] = float(readline.split(', ')[0])
#     returnData[i, 1] = float(readline.split(', ')[1])
#     i = i + 1
# readfile.close()
#
# num0 = 0
# num1 = 0
# num2 = 0
# num3 = 0
# num4 = 0
# num6 = 0
# num7 = 0
# num8 = 0
# correctNum0 = 0
# correctNum1 = 0
# correctNum2 = 0
# correctNum3 = 0
# correctNum4 = 0
# correctNum6 = 0
# correctNum7 = 0
# correctNum8 = 0
# for i in range(len(returnData)):
#     if returnData[i, 0] == 0:
#         num0 = num0 + 1
#         if returnData[i, 1] == 0:
#             correctNum0 = correctNum0 + 1
#     elif returnData[i, 0] == 1:
#         num1 = num1 + 1
#         if returnData[i, 1] == 1:
#             correctNum1 = correctNum1 + 1
#         # else:
#         #     print(str(i)+': 1 - '+str(returnData[i, 1]))
#     elif returnData[i, 0] == 2:
#         num2 = num2 + 1
#         if returnData[i, 1] == 2:
#             correctNum2 = correctNum2 + 1
#         # else:
#         #     print(str(i)+': 2 - '+str(returnData[i, 1]))
#     elif returnData[i, 0] == 3:
#         num3 = num3 + 1
#         if returnData[i, 1] == 3:
#             correctNum3 = correctNum3 + 1
#         # else:
#         #     print(str(i)+': 3 - '+str(returnData[i, 1]))
#     elif returnData[i, 0] == 4:
#         num4 = num4 + 1
#         if returnData[i, 1] == 4:
#             correctNum4 = correctNum4 + 1
#         # else:
#             # print(str(i)+': 4 - '+str(returnData[i, 1]))
#     elif returnData[i, 0] == 6:
#         num6 = num6 + 1
#         if returnData[i, 1] == 6:
#             correctNum6 = correctNum6 + 1
#         # else:
#             # print(str(i)+': 6 - '+str(returnData[i, 1]))
#     elif returnData[i, 0] == 7:
#         num7 = num7 + 1
#         if returnData[i, 1] == 7:
#             correctNum7 = correctNum7 + 1
#         # else:
#         #     print(str(i)+': 7 - '+str(returnData[i, 1]))
#     elif returnData[i, 0] == 8:
#         num8 = num8 + 1
#         if returnData[i, 1] == 8:
#             correctNum8 = correctNum8 + 1
#         # else:
#             # print(str(i)+': 8 - '+str(returnData[i, 1]))
# # accu0 = correctNum0 / num0
# accu1 = correctNum1 / num1
# accu2 = correctNum2 / num2
# accu3 = correctNum3 / num3
# accu4 = correctNum4 / num4
# accu6 = correctNum6 / num6
# accu7 = correctNum7 / num7
# accu8 = correctNum8 / num8
#
# correctNum = correctNum1+correctNum2+correctNum3+correctNum4+correctNum6+correctNum7+correctNum8
# num = num1+num2+num3+num4+num6+num7+num8
# accu = correctNum / num
# print('3correctNum=' + str(correctNum) + '; accuracy=' + str(accu))
# print('accu1: '+str(accu1))
# print('accu2: '+str(accu2))
# print('accu3: '+str(accu3))
# print('accu4: '+str(accu4))
# print('accu6: '+str(accu6))
# print('accu7: '+str(accu7))
# print('accu8: '+str(accu8))



# # 每个class的结果分析 mF1
# label_writePath = 'Data/cutArea/MyMaxEnt/train/0/8AB_labelResult_e213.txt'
# label_writePath = 'Data/cutArea/MultiScaleKNN/train/0/8AB_labelResult.txt'
label_writePath = 'Data/cutArea/OptimalWeinmann/train/0/8AB_labelResult.txt'

# label_writePath = 'Data/cutArea/MyMaxEnt/3RandomForests_labelResult_ch3.txt'
# label_writePath = 'Data/cutArea/MultiScaleKNN/3RandomForests_labelResult.txt'
# label_writePath = 'Data/cutArea/OptimalWeinmann/3RandomForests_labelResult.txt'
readfile = open(label_writePath, "r")
readAllLine = readfile.readlines()
lineNum = len(readAllLine)
i = 0
returnData = np.empty([lineNum, 2], dtype=float)
for readline in readAllLine:
    returnData[i, 0] = float(readline.split(', ')[0])
    returnData[i, 1] = float(readline.split(', ')[1])
    i = i + 1
readfile.close()
returnData = returnData[np.where(returnData[:, 0] != 9)]
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num6 = 0
num7 = 0
num8 = 0
correctNum1 = 0
correctNum2 = 0
correctNum3 = 0
correctNum4 = 0
correctNum6 = 0
correctNum7 = 0
correctNum8 = 0
for i in range(len(returnData)):
    if returnData[i, 0] == 1:
        num1 = num1 + 1
        if returnData[i, 1] == 1:
            correctNum1 = correctNum1 + 1
    elif returnData[i, 0] == 2:
        num2 = num2 + 1
        if returnData[i, 1] == 2:
            correctNum2 = correctNum2 + 1
    elif returnData[i, 0] == 3:
        num3 = num3 + 1
        if returnData[i, 1] == 3:
            correctNum3 = correctNum3 + 1
    elif returnData[i, 0] == 4:
        num4 = num4 + 1
        if returnData[i, 1] == 4:
            correctNum4 = correctNum4 + 1
    elif returnData[i, 0] == 6:
        num6 = num6 + 1
        if returnData[i, 1] == 6:
            correctNum6 = correctNum6 + 1
    elif returnData[i, 0] == 7:
        num7 = num7 + 1
        if returnData[i, 1] == 7:
            correctNum7 = correctNum7 + 1
    elif returnData[i, 0] == 8:
        num8 = num8 + 1
        if returnData[i, 1] == 8:
            correctNum8 = correctNum8 + 1
    else:
        print(returnData[i, 0])


TP1 = correctNum1
FN1 = num1 - correctNum1
TP2 = correctNum2
FN2 = num2 - correctNum2
TP3 = correctNum3
FN3 = num3 - correctNum3
TP4 = correctNum4
FN4 = num4 - correctNum4
TP6 = correctNum6
FN6 = num6 - correctNum6
TP7 = correctNum7
FN7 = num7 - correctNum7
TP8 = correctNum8
FN8 = num8 - correctNum8
sum = TP1+FN1+TP2+FN2+TP3+FN3+TP4+FN4+TP6+FN6+TP7+FN7+TP8+FN8
nonRoad1 = returnData[np.where(returnData[:, 0] != 1)]
FP1 = len(nonRoad1[np.where(nonRoad1[:, 1] == 1)])
nonHouse2 = returnData[np.where(returnData[:, 0] != 2)]
FP2 = len(nonHouse2[np.where(nonHouse2[:, 1] == 2)])
nonFence3 = returnData[np.where(returnData[:, 0] != 3)]
FP3 = len(nonFence3[np.where(nonFence3[:, 1] == 3)])
nonTree4 = returnData[np.where(returnData[:, 0] != 4)]
FP4 = len(nonTree4[np.where(nonTree4[:, 1] == 4)])
nonGrass6 = returnData[np.where(returnData[:, 0] != 6)]
FP6 = len(nonGrass6[np.where(nonGrass6[:, 1] == 6)])
nonWater7 = returnData[np.where(returnData[:, 0] != 7)]
FP7 = len(nonWater7[np.where(nonWater7[:, 1] == 7)])
nonPower8 = returnData[np.where(returnData[:, 0] != 8)]
FP8 = len(nonPower8[np.where(nonPower8[:, 1] == 8)])


precision1 = TP1/(TP1+FP1)
recall1 = TP1/(TP1+FN1)
F1 = 2*(precision1*recall1)/(precision1+recall1)
precision2 = TP2/(TP2+FP2)
recall2 = TP2/(TP2+FN2)
F2 = 2*(precision2*recall2)/(precision2+recall2)
precision3 = TP3/(TP3+FP3)
recall3 = TP3/(TP3+FN3)
F3 = 2*(precision3*recall3)/(precision3+recall3)
precision4 = TP4/(TP4+FP4)
recall4 = TP4/(TP4+FN4)
F4 = 2*(precision4*recall4)/(precision4+recall4)
precision6 = TP6/(TP6+FP6)
recall6 = TP6/(TP6+FN6)
F6 = 2*(precision6*recall6)/(precision6+recall6)
# precision7 = TP7/(TP7+FP7)
# recall7 = TP7/(TP7+FN7)
# F7 = 2*(precision7*recall7)/(precision7+recall7)
precision8 = TP8/(TP8+FP8)
recall8 = TP8/(TP8+FN8)
F8 = 2*(precision8*recall8)/(precision8+recall8)
print('F1: '+str(F1))
print('F2: '+str(F2))
print('F3: '+str(F3))
print('F4: '+str(F4))
print('F6: '+str(F6))
# print('F7: '+str(F7))
print('F8: '+str(F8))
mF = (F1+F2+F3+F4+F6+F8)/6
# mF = (F1+F2+F3+F4+F6+F7+F8)/7
print('mF: '+str(mF))




# # MaxEnt(e213) train0:  confusion matrix
# label_writePath = 'Data/cutArea/MyMaxEnt/train/0/8AB_labelResult_e213.txt'
# readfile = open(label_writePath, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData = np.empty([lineNum, 2], dtype=float)
# for readline in readAllLine:
#     returnData[i, 0] = float(readline.split(', ')[0])
#     returnData[i, 1] = float(readline.split(', ')[1])
#     i = i + 1
# readfile.close()
# returnData = returnData[np.where(returnData[:, 0] != 9)]
#
# Road1 = returnData[np.where(returnData[:, 0] == 1)]
# RR = len(Road1[np.where(Road1[:, 1] == 1)])/len(Road1)
# RH = len(Road1[np.where(Road1[:, 1] == 2)])/len(Road1)
# RF = len(Road1[np.where(Road1[:, 1] == 3)])/len(Road1)
# RT = len(Road1[np.where(Road1[:, 1] == 4)])/len(Road1)
# RG = len(Road1[np.where(Road1[:, 1] == 6)])/len(Road1)
# RP = len(Road1[np.where(Road1[:, 1] == 8)])/len(Road1)
# print('RR = '+str(RR))
# print('RH = '+str(RH))
# print('RF = '+str(RF))
# print('RT = '+str(RT))
# print('RG = '+str(RG))
# print('RP = '+str(RP))
# House2 = returnData[np.where(returnData[:, 0] == 2)]
# HR = len(House2[np.where(House2[:, 1] == 1)])/len(House2)
# HH = len(House2[np.where(House2[:, 1] == 2)])/len(House2)
# HF = len(House2[np.where(House2[:, 1] == 3)])/len(House2)
# HT = len(House2[np.where(House2[:, 1] == 4)])/len(House2)
# HG = len(House2[np.where(House2[:, 1] == 6)])/len(House2)
# HP = len(House2[np.where(House2[:, 1] == 8)])/len(House2)
# print('HR = '+str(HR))
# print('HH = '+str(HH))
# print('HF = '+str(HF))
# print('HT = '+str(HT))
# print('HG = '+str(HG))
# print('HP = '+str(HP))
# Fence3 = returnData[np.where(returnData[:, 0] == 3)]
# FR = len(Fence3[np.where(Fence3[:, 1] == 1)])/len(Fence3)
# FH = len(Fence3[np.where(Fence3[:, 1] == 2)])/len(Fence3)
# FF = len(Fence3[np.where(Fence3[:, 1] == 3)])/len(Fence3)
# FT = len(Fence3[np.where(Fence3[:, 1] == 4)])/len(Fence3)
# FG = len(Fence3[np.where(Fence3[:, 1] == 6)])/len(Fence3)
# FP = len(Fence3[np.where(Fence3[:, 1] == 8)])/len(Fence3)
# print('FR = '+str(FR))
# print('FH = '+str(FH))
# print('FF = '+str(FF))
# print('FT = '+str(FT))
# print('FG = '+str(FG))
# print('FP = '+str(FP))
# Tree4 = returnData[np.where(returnData[:, 0] == 4)]
# TR = len(Tree4[np.where(Tree4[:, 1] == 1)])/len(Tree4)
# TH = len(Tree4[np.where(Tree4[:, 1] == 2)])/len(Tree4)
# TF = len(Tree4[np.where(Tree4[:, 1] == 3)])/len(Tree4)
# TT = len(Tree4[np.where(Tree4[:, 1] == 4)])/len(Tree4)
# TG = len(Tree4[np.where(Tree4[:, 1] == 6)])/len(Tree4)
# TP = len(Tree4[np.where(Tree4[:, 1] == 8)])/len(Tree4)
# print('TR = '+str(TR))
# print('TH = '+str(TH))
# print('TF = '+str(TF))
# print('TT = '+str(TT))
# print('TG = '+str(TG))
# print('TP = '+str(TP))
# Grass6 = returnData[np.where(returnData[:, 0] == 6)]
# GR = len(Grass6[np.where(Grass6[:, 1] == 1)])/len(Grass6)
# GH = len(Grass6[np.where(Grass6[:, 1] == 2)])/len(Grass6)
# GF = len(Grass6[np.where(Grass6[:, 1] == 3)])/len(Grass6)
# GT = len(Grass6[np.where(Grass6[:, 1] == 4)])/len(Grass6)
# GG = len(Grass6[np.where(Grass6[:, 1] == 6)])/len(Grass6)
# GP = len(Grass6[np.where(Grass6[:, 1] == 8)])/len(Grass6)
# print('GR = '+str(GR))
# print('GH = '+str(GH))
# print('GF = '+str(GF))
# print('GT = '+str(GT))
# print('GG = '+str(GG))
# print('GP = '+str(GP))
# Power8 = returnData[np.where(returnData[:, 0] == 8)]
# PR = len(Power8[np.where(Power8[:, 1] == 1)])/len(Power8)
# PH = len(Power8[np.where(Power8[:, 1] == 2)])/len(Power8)
# PF = len(Power8[np.where(Power8[:, 1] == 3)])/len(Power8)
# PT = len(Power8[np.where(Power8[:, 1] == 4)])/len(Power8)
# PG = len(Power8[np.where(Power8[:, 1] == 6)])/len(Power8)
# PP = len(Power8[np.where(Power8[:, 1] == 8)])/len(Power8)
# print('PR = '+str(PR))
# print('PH = '+str(PH))
# print('PF = '+str(PF))
# print('PT = '+str(PT))
# print('PG = '+str(PG))
# print('PP = '+str(PP))
#
# array = [[RR,RH,RF,RT,RG,RP],
#          [HR,HH,HF,HT,HG,HP],
#          [FR,FH,FF,FT,FG,FP],
#          [TR,TH,TF,TT,TG,TP],
#          [GR,GH,GF,GT,GG,GP],
#          [PR,PH,PF,PT,PG,PP]]
# df_cm = pd.DataFrame(array, range(6), range(6))
# # plt.figure(figsize=(10,7))
# sn.set(font_scale=1.0) # for label size
# ax = sn.heatmap(df_cm, annot=True, fmt='.3f', annot_kws={"size": 12}, cmap='Blues', vmax=1.0)  # font size
# ax.yaxis.set_ticklabels(['Road','House','Fence','Tree','Grass','Power Line'], rotation=45)
# ax.xaxis.set_ticklabels(['Road','House','Fence','Tree','Grass','Power Line'], rotation=45)
# ax.set_xlabel('Predicted label', labelpad=0)
# ax.set_ylabel('True label', labelpad=0)
# plt.show()



# # MaxEnt(e213) all data: confusion matrix
# label_writePath = 'Data/cutArea/MyMaxEnt/3RandomForests_labelResult_e213.txt'
# readfile = open(label_writePath, "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData = np.empty([lineNum, 2], dtype=float)
# for readline in readAllLine:
#     returnData[i, 0] = float(readline.split(', ')[0])
#     returnData[i, 1] = float(readline.split(', ')[1])
#     i = i + 1
# readfile.close()
# returnData = returnData[np.where(returnData[:, 0] != 9)]
#
#
# Road1 = returnData[np.where(returnData[:, 0] == 1)]
# RR = len(Road1[np.where(Road1[:, 1] == 1)])/len(Road1)
# RH = len(Road1[np.where(Road1[:, 1] == 2)])/len(Road1)
# RF = len(Road1[np.where(Road1[:, 1] == 3)])/len(Road1)
# RT = len(Road1[np.where(Road1[:, 1] == 4)])/len(Road1)
# RG = len(Road1[np.where(Road1[:, 1] == 6)])/len(Road1)
# RW = len(Road1[np.where(Road1[:, 1] == 7)])/len(Road1)
# RP = len(Road1[np.where(Road1[:, 1] == 8)])/len(Road1)
# print('RR = '+str(RR))
# print('RH = '+str(RH))
# print('RF = '+str(RF))
# print('RT = '+str(RT))
# print('RG = '+str(RG))
# print('RW = '+str(RW))
# print('RP = '+str(RP))
# House2 = returnData[np.where(returnData[:, 0] == 2)]
# HR = len(House2[np.where(House2[:, 1] == 1)])/len(House2)
# HH = len(House2[np.where(House2[:, 1] == 2)])/len(House2)
# HF = len(House2[np.where(House2[:, 1] == 3)])/len(House2)
# HT = len(House2[np.where(House2[:, 1] == 4)])/len(House2)
# HG = len(House2[np.where(House2[:, 1] == 6)])/len(House2)
# HW = len(House2[np.where(House2[:, 1] == 7)])/len(House2)
# HP = len(House2[np.where(House2[:, 1] == 8)])/len(House2)
# print('HR = '+str(HR))
# print('HH = '+str(HH))
# print('HF = '+str(HF))
# print('HT = '+str(HT))
# print('HG = '+str(HG))
# print('HW = '+str(HW))
# print('HP = '+str(HP))
# Fence3 = returnData[np.where(returnData[:, 0] == 3)]
# FR = len(Fence3[np.where(Fence3[:, 1] == 1)])/len(Fence3)
# FH = len(Fence3[np.where(Fence3[:, 1] == 2)])/len(Fence3)
# FF = len(Fence3[np.where(Fence3[:, 1] == 3)])/len(Fence3)
# FT = len(Fence3[np.where(Fence3[:, 1] == 4)])/len(Fence3)
# FG = len(Fence3[np.where(Fence3[:, 1] == 6)])/len(Fence3)
# FW = len(Fence3[np.where(Fence3[:, 1] == 7)])/len(Fence3)
# FP = len(Fence3[np.where(Fence3[:, 1] == 8)])/len(Fence3)
# print('FR = '+str(FR))
# print('FH = '+str(FH))
# print('FF = '+str(FF))
# print('FT = '+str(FT))
# print('FG = '+str(FG))
# print('FW = '+str(FW))
# print('FP = '+str(FP))
# Tree4 = returnData[np.where(returnData[:, 0] == 4)]
# TR = len(Tree4[np.where(Tree4[:, 1] == 1)])/len(Tree4)
# TH = len(Tree4[np.where(Tree4[:, 1] == 2)])/len(Tree4)
# TF = len(Tree4[np.where(Tree4[:, 1] == 3)])/len(Tree4)
# TT = len(Tree4[np.where(Tree4[:, 1] == 4)])/len(Tree4)
# TG = len(Tree4[np.where(Tree4[:, 1] == 6)])/len(Tree4)
# TW = len(Tree4[np.where(Tree4[:, 1] == 7)])/len(Tree4)
# TP = len(Tree4[np.where(Tree4[:, 1] == 8)])/len(Tree4)
# print('TR = '+str(TR))
# print('TH = '+str(TH))
# print('TF = '+str(TF))
# print('TT = '+str(TT))
# print('TG = '+str(TG))
# print('TW = '+str(TW))
# print('TP = '+str(TP))
# Grass6 = returnData[np.where(returnData[:, 0] == 6)]
# GR = len(Grass6[np.where(Grass6[:, 1] == 1)])/len(Grass6)
# GH = len(Grass6[np.where(Grass6[:, 1] == 2)])/len(Grass6)
# GF = len(Grass6[np.where(Grass6[:, 1] == 3)])/len(Grass6)
# GT = len(Grass6[np.where(Grass6[:, 1] == 4)])/len(Grass6)
# GG = len(Grass6[np.where(Grass6[:, 1] == 6)])/len(Grass6)
# GW = len(Grass6[np.where(Grass6[:, 1] == 7)])/len(Grass6)
# GP = len(Grass6[np.where(Grass6[:, 1] == 8)])/len(Grass6)
# print('GR = '+str(GR))
# print('GH = '+str(GH))
# print('GF = '+str(GF))
# print('GT = '+str(GT))
# print('GG = '+str(GG))
# print('GW = '+str(GW))
# print('GP = '+str(GP))
# Water7 = returnData[np.where(returnData[:, 0] == 7)]
# WR = len(Water7[np.where(Water7[:, 1] == 1)])/len(Water7)
# WH = len(Water7[np.where(Water7[:, 1] == 2)])/len(Water7)
# WF = len(Water7[np.where(Water7[:, 1] == 3)])/len(Water7)
# WT = len(Water7[np.where(Water7[:, 1] == 4)])/len(Water7)
# WG = len(Water7[np.where(Water7[:, 1] == 6)])/len(Water7)
# WW = len(Water7[np.where(Water7[:, 1] == 7)])/len(Water7)
# WP = len(Water7[np.where(Water7[:, 1] == 8)])/len(Water7)
# print('PR = '+str(WR))
# print('PH = '+str(WH))
# print('PF = '+str(WF))
# print('PT = '+str(WT))
# print('PG = '+str(WG))
# print('PG = '+str(WW))
# print('PP = '+str(WP))
# Power8 = returnData[np.where(returnData[:, 0] == 8)]
# PR = len(Power8[np.where(Power8[:, 1] == 1)])/len(Power8)
# PH = len(Power8[np.where(Power8[:, 1] == 2)])/len(Power8)
# PF = len(Power8[np.where(Power8[:, 1] == 3)])/len(Power8)
# PT = len(Power8[np.where(Power8[:, 1] == 4)])/len(Power8)
# PG = len(Power8[np.where(Power8[:, 1] == 6)])/len(Power8)
# PW = len(Power8[np.where(Power8[:, 1] == 7)])/len(Power8)
# PP = len(Power8[np.where(Power8[:, 1] == 8)])/len(Power8)
# print('PR = '+str(PR))
# print('PH = '+str(PH))
# print('PF = '+str(PF))
# print('PT = '+str(PT))
# print('PG = '+str(PG))
# print('PW = '+str(PW))
# print('PP = '+str(PP))
#
# array = [[RR,RH,RF,RT,RG,RW,RP],
#          [HR,HH,HF,HT,HG,HW,HP],
#          [FR,FH,FF,FT,FG,FW,FP],
#          [TR,TH,TF,TT,TG,TW,TP],
#          [GR,GH,GF,GT,GG,GW,GP],
#          [WR,WH,WF,WT,WG,WW,WP],
#          [PR,PH,PF,PT,PG,PW,PP]]
# df_cm = pd.DataFrame(array, range(7), range(7))
# # plt.figure(figsize=(10,7))
# sn.set(font_scale=1.0) # for label size
# ax = sn.heatmap(df_cm, annot=True, fmt='.3f', annot_kws={"size": 12}, cmap='Blues', vmax=1.0)  # font size
# ax.yaxis.set_ticklabels(['Road','House','Fence','Tree','Grass','Water','Power Line'], rotation=45)
# ax.xaxis.set_ticklabels(['Road','House','Fence','Tree','Grass','Water','Power Line'], rotation=45)
# ax.set_xlabel('Predicted label', labelpad=0)
# ax.set_ylabel('True label', labelpad=0)
# plt.show()






# # 添加 predicted label
# path_train = 'Data/cutArea/train_test/'
# raw_data = MyFileOperator.readData_10(path_train + 'L1C2_addC1C3_train_test.txt')
# path = 'Data/cutArea/MyMaxEnt/'
# label = MyFileOperator.readData_2(path + '3RandomForests_labelResult_ch1.txt')
# data_label = raw_data
# j = 0
# for k in range(len(raw_data)):
#     if raw_data[k, 5] != 0:
#         data_label[k, 5] = label[j, 1]
#         j = j + 1
#
# path_w = 'Data/cutArea/MyMaxEnt/'
# writefilePosition = open(path_w + '3RandomForests_dataAddLabel_ch1.txt', "a")
# writefilePosition.seek(0)
# writefilePosition.truncate()
# for j in range(len(data_label)):
#     writefilePosition.writelines([str(data_label[j, 0]), ', ', str(data_label[j, 1]), ', ', str(data_label[j, 2]),
#                                   ', ', str(data_label[j, 3]), ', ', str(data_label[j, 4]), ', ', str(data_label[j, 5]),
#                                   ', ', str(data_label[j, 6]), ', ', str(data_label[j, 7]), ', ', str(data_label[j, 8]),
#                                   ', ', str(data_label[j, 9]),  '\n'])
# writefilePosition.close()
