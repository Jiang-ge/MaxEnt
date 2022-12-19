import numpy as np
import MyFileOperator
import math
from sklearn.neighbors import NearestNeighbors
import Step2_CalculateFeatureVector
from datetime import datetime

large_scale = 1200
# medium_scale = 100
# small_scale = 50
def mpi_entrance(path_r, path_w):
    start_time = datetime.now()
    channel2_data = MyFileOperator.readData_10(path_r + 'L1C2_addC1C3_train.txt')
    featureVectorList = []
    optimalNeighbor_len = []
    nbrs = NearestNeighbors(n_neighbors=large_scale, algorithm='kd_tree').fit(channel2_data[:, 1:4])
    distances, indices = nbrs.kneighbors(channel2_data[:, 1:4])
    for n in range(len(channel2_data)):
        centerPoint = np.array([channel2_data[n, :]])
        largeNeighbor = channel2_data[indices[n, :]]
        # mediumNeighbor = largeNeighbor[0:medium_scale, :]
        # smallNeighbor = largeNeighbor[0:small_scale, :]

        # smallFeature = Step2_CalculateFeatureVector.calculateFeatureVector(smallNeighbor, centerPoint)
        # mediumFeature = Step2_CalculateFeatureVector.calculateFeatureVector(mediumNeighbor, centerPoint)
        optimalNeighbor_len.append(len(largeNeighbor))
        largeFeature = Step2_CalculateFeatureVector.calculateFeatureVector(largeNeighbor, centerPoint)
        # featureVector_each = np.concatenate([smallFeature, mediumFeature[1:], largeFeature[1:]])
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






