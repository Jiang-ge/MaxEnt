import math
import MyFileOperator
import numpy as np
from scipy.spatial import cKDTree



import math
import MyFileOperator
import numpy as np
from sklearn.neighbors import NearestNeighbors
from datetime import datetime
from functools import reduce
from scipy.spatial.distance import cdist

def optimalNeighbor_filtering(channel2_data, pos, centerPoint):
    level_num = int(len(channel2_data) / 10)
    cut = int(len(channel2_data)/level_num)
    infor_diff = abs(channel2_data[:, pos] - centerPoint[0, pos])
    infor_max = max(infor_diff)
    infor_min = min(infor_diff)
    div = (infor_max - infor_min) / cut
    if div == 0:   # infor_max=infor_min
        return channel2_data
    else:
        level = np.empty(shape=(cut, 3), dtype=float)
        for i in range(len(level)):
            level[i, 0] = i
            level[i, 1] = 0

        for j in range(len(infor_diff)):
            groupNum = int(infor_diff[j] / div)
            if groupNum > (cut - 1):
                level[(cut - 1), 1] = level[(cut - 1), 1] + 1
            else:
                level[groupNum, 1] = level[groupNum, 1] + 1

        # pointSum = 0
        # for t in range(len(level)):
        #     pointSum = pointSum + level[t, 1]
        #     ratio = pointSum / (t+1)
        #     level[t, 2] = ratio


        stopIndex = np.argmax(level[:, 1])
        threshold = (stopIndex+1) * div
        neighborList = []
        for v in range(len(channel2_data)):
            if abs(channel2_data[v, pos] - centerPoint[0, pos]) < threshold:
                neighborList.append(channel2_data[v, :])
        filteredNeighbor = np.array(neighborList)
        return filteredNeighbor

def optimalNeighbor_ch123(lastOptimalNeighbor, pos, centerPoint):
    cut = int(len(lastOptimalNeighbor)/100)
    infor_diff = abs(lastOptimalNeighbor[:, pos] - centerPoint[0, pos])
    infor_max = max(infor_diff)
    infor_min = min(infor_diff)
    div = (infor_max - infor_min) / cut
    if div == 0:   # infor_max=infor_min
        return lastOptimalNeighbor
    else:
        level = np.empty(shape=(cut, 3), dtype=float)
        for i in range(len(level)):
            level[i, 0] = i
            level[i, 1] = 0
            level[i, 2] = 0

        for j in range(len(infor_diff)):
            groupNum = int(infor_diff[j] / div)
            if groupNum > (cut - 1):
                level[(cut - 1), 1] = level[(cut - 1), 1] + 1
            else:
                level[groupNum, 1] = level[groupNum, 1] + 1

        for t in range(len(level)):
            entropy_left = 0
            entropy_right = 0
            if t > 0:
                sum_left = np.sum(level[0:t, 1])
                sum_right = np.sum(level[t:, 1])
                for t_left in range(t):
                    if level[t_left, 1] != 0:
                        p_left = level[t_left, 1] / sum_left
                        entropy_left = entropy_left - p_left * math.log(p_left)
                for t_right in range(cut - t):
                    t_right = t_right + t
                    if level[t_right, 1] != 0:
                        p_right = level[t_right, 1] / sum_right
                        entropy_right = entropy_right - p_right * math.log(p_right)
                entropy_sum = entropy_left + entropy_right
                level[t-1, 2] = entropy_sum
        maxIndex = np.argmax(level[:, 2]) + 1
        threshold = maxIndex * div
        neighborList = []
        for v in range(len(lastOptimalNeighbor)):
            if abs(lastOptimalNeighbor[v, pos] - centerPoint[0, pos]) < threshold:
                neighborList.append(lastOptimalNeighbor[v, :])
        optimalNeighbor = np.array(neighborList)
        # del level
        return optimalNeighbor



def homogeneousPointsSearch(data, centerPoint):
    # filter_ch3 = optimalNeighbor_filtering(data, 9, centerPoint)
    homogeneous_ch3 = optimalNeighbor_ch123(data, 9, centerPoint)
    return homogeneous_ch3
















