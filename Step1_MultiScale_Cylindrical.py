import numpy as np
import MyFileOperator
import math
from sklearn.neighbors import NearestNeighbors
import Step2_CalculateFeatureVector
from datetime import datetime
from scipy.spatial import cKDTree


meanPointSpacing_L1C2 = 0.547
radius_large = meanPointSpacing_L1C2 * 12
# radius_medium = meanPointSpacing_L1C2 * 2
# radius_small = meanPointSpacing_L1C2 * 1
def mpi_entrance(path_r, path_w):
    start_time = datetime.now()
    channel2_data = MyFileOperator.readData_10(path_r+'L1C2_addC1C3_train.txt')
    featureVectorList = []
    optimalNeighbor_len = []
    tree = cKDTree(channel2_data[:, 1:3])
    indices = tree.query_ball_point(channel2_data[:, 1:3], radius_large)
    for n in range(len(channel2_data)):
        centerPoint = np.array([channel2_data[n, :]])
        neighbor = channel2_data[np.array(indices[n])]
        # neighborList_small = []
        # neighborList_medium = []
        # neighborList_large = []
        # neighborList_small.append(channel2_data[n, :])
        # neighborList_medium.append(channel2_data[n, :])
        # neighborList_large.append(channel2_data[n, :])
        # for j in range(len(neighbor)):
            # dis = math.sqrt(math.pow((centerPoint[0, 1] - neighbor[j, 1]), 2) +
            #                 math.pow((centerPoint[0, 2] - neighbor[j, 2]), 2) +
            #                 math.pow((centerPoint[0, 3] - neighbor[j, 3]), 2))
            # if dis <= radius_small:
            #     neighborList_small.append(neighbor[j, :])
            #     neighborList_medium.append(neighbor[j, :])
            #     neighborList_large.append(neighbor[j, :])
            # elif dis <= radius_medium:
            #     neighborList_medium.append(neighbor[j, :])
            #     neighborList_large.append(neighbor[j, :])
            # else:
            # neighborList_large.append(neighbor[j, :])

        # smallNeighborArray = np.array(neighborList_small)
        # mediumNeighborArray = np.array(neighborList_medium)
        # largeNeighborArray = np.array(neighborList_large)

        # smallFeature = Step2_CalculateFeatureVector.calculateFeatureVector(smallNeighborArray, centerPoint)
        # mediumFeature = Step2_CalculateFeatureVector.calculateFeatureVector(mediumNeighborArray, centerPoint)
        optimalNeighbor_len.append(len(neighbor))
        largeFeature = Step2_CalculateFeatureVector.calculateFeatureVector(neighbor, centerPoint)
        # featureVector_each = np.concatenate([largeFeature])
        featureVectorList.append(largeFeature)

    featureVector = np.array(featureVectorList)
    optimalNeighbor_len = np.array(optimalNeighbor_len)
    # featureVector_addLabel = np.hstack((featureVector, np.array([channel2_data[:, 5]]).T))
    writefilePosition = open(path_w + 'featureVector.txt', "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(featureVector)):
        writefilePosition.writelines([str(featureVector[i, 0]), ', ', str(featureVector[i, 1]), ', ', str(featureVector[i, 2]), ', ', str(featureVector[i, 3]), ', ',\
                                  str(featureVector[i, 4]), ', ', str(featureVector[i, 5]), ', ', str(featureVector[i, 6]), ', ', str(featureVector[i, 7]), ', ',\
                                  str(featureVector[i, 8]), ', ', str(featureVector[i, 9]), ', ', str(featureVector[i, 10]), ', ', str(featureVector[i, 11]), ', ',\
                                  str(featureVector[i, 12]), ', ', str(featureVector[i, 13]), ', ', str(featureVector[i, 14]), ', ', str(featureVector[i, 15]), ', ', \
                                  str(featureVector[i, 16]), ', ', str(optimalNeighbor_len[i]),  '\n'])
        # ', ', str(featureVector[i, 18]), ', ', str(featureVector[i, 19]), ', ', \
        # str(featureVector[i, 20]), ', ', str(featureVector[i, 21]), ', ', str(featureVector[i, 22]), ', ', str(
        #     featureVector[i, 23]), ', ', \
        # str(featureVector[i, 24]), ', ', str(featureVector[i, 25]), ', ', str(featureVector[i, 26]), ', ', str(
        #     featureVector[i, 27]), ', ', \
        # str(featureVector[i, 28]), ', ', str(featureVector[i, 29]), ', ', str(featureVector[i, 30]), ', ', str(
        #     featureVector[i, 31]), ', ', \
        # str(featureVector[i, 32]), ', ', str(featureVector[i, 33]), ', ', str(featureVector[i, 34]), ', ', str(
        #     featureVector[i, 35]), ', ', \
        # str(featureVector[i, 36]), ', ', str(featureVector[i, 37]), ', ', str(featureVector[i, 38]), ', ', str(
        #     featureVector[i, 39]), ', ', \
        # str(featureVector[i, 40]), ', ', str(featureVector[i, 41]), ', ', str(featureVector[i, 42]), ', ', str(
        #     featureVector[i, 43]), ', ', \
        # str(featureVector[i, 44]), ', ', str(featureVector[i, 45]), ', ', str(featureVector[i, 46]), ', ', str(
        #     featureVector[i, 47]), ', ', \
        # str(featureVector[i, 48]),
    writefilePosition.close()
    end_time = datetime.now()
    print('--------------All done : {} : {}------------end time: {}----------------'.format(path_w, end_time - start_time, end_time))












