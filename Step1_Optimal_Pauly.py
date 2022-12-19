import numpy as np
import MyFileOperator
import math
from sklearn.neighbors import NearestNeighbors
import Step2_CalculateFeatureVector
from datetime import datetime

def mpi_entrance(path_r, path_w):
    start_time = datetime.now()
    channel2_data = MyFileOperator.readData_10(path_r+'L1C2_addC1C3_train.txt')
    featureVectorList = []
    optimalNeighbor_len = []
    if len(channel2_data) == 1000:
        neighbor_num = 500
    else:
        neighbor_num = len(channel2_data)
    nbrs = NearestNeighbors(n_neighbors=neighbor_num, algorithm='kd_tree').fit(channel2_data[:, 1:4])
    distances, indices = nbrs.kneighbors(channel2_data[:, 1:4])
    for n in range(len(channel2_data)):
        centerPoint = np.array([channel2_data[n, :]])
        neighbor = channel2_data[indices[n, :]]
        curvatureArray = np.empty(shape=(neighbor_num-3, 3), dtype=float)
        k = 0
        neighborList = []
        neighborList.append(channel2_data[n, :])
        for j in range(neighbor_num):
            if neighbor[j, 0] - centerPoint[0, 0] != 0:
                neighborList.append(np.array(neighbor[j, :]))
            if j > 2:
                neighborArray = np.array(neighborList)
                neighborMatrix = neighborArray[:, 1:4]
                centerPointMatrix = np.tile(centerPoint[0, 1:4], (len(neighborMatrix), 1))
                try:
                    covMatrix = ((neighborMatrix - centerPointMatrix).T).dot(
                        (neighborMatrix - centerPointMatrix)) / len(neighborMatrix)
                    eigen_vals, eigen_vecs = np.linalg.eig(covMatrix)
                    # eigen_vals = sorted(eigen_vals, reverse=True)
                    if isinstance(eigen_vals[0], complex) or isinstance(eigen_vals[1], complex):
                        print(j)
                    else:
                        sum = eigen_vals[0] + eigen_vals[1] + eigen_vals[2]
                        eigen_vals_0_nor = eigen_vals[0] / sum
                        eigen_vals_1_nor = eigen_vals[1] / sum
                        eigen_vals_2_nor = eigen_vals[2] / sum

                        if eigen_vals_0_nor <= 0:
                            ln_0 = 0
                        else:
                            ln_0 = math.log(eigen_vals_0_nor)
                        if eigen_vals_1_nor <= 0:
                            ln_1 = 0
                        else:
                            ln_1 = math.log(eigen_vals_1_nor)
                        if eigen_vals_2_nor <= 0:
                            ln_2 = 0
                        else:
                            ln_2 = math.log(eigen_vals_2_nor)
                        curvature = eigen_vals_2_nor
                        curvatureArray[k, 0] = j
                        curvatureArray[k, 1] = curvature
                        if j == 3:
                            curvatureArray[k, 2] = 0
                        else:
                            curvatureArray[k, 2] = abs(curvature - lastCurvature)
                        lastCurvature = curvature

                except:
                    a = 0
                k = k + 1
        optimalNeighborNum = curvatureArray[np.argmax(curvatureArray[:, 2]), 0]
        optimalNeighbor = neighbor[0:int(optimalNeighborNum), :]
        optimalNeighbor_len.append(len(optimalNeighbor))
        featureVectorList.append(Step2_CalculateFeatureVector.calculateFeatureVector(optimalNeighbor, centerPoint))

    featureVector = np.array(featureVectorList)
    optimalNeighbor_len = np.array(optimalNeighbor_len)
    writefilePosition = open(path_w + 'featureVector.txt', "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(featureVector)):
        writefilePosition.writelines([str(featureVector[i, 0]), ', ', str(featureVector[i, 1]), ', ', str(featureVector[i, 2]), ', ', str(featureVector[i, 3]), ', ',\
                                  str(featureVector[i, 4]), ', ', str(featureVector[i, 5]), ', ', str(featureVector[i, 6]), ', ', str(featureVector[i, 7]), ', ',\
                                  str(featureVector[i, 8]), ', ', str(featureVector[i, 9]), ', ', str(featureVector[i, 10]), ', ', str(featureVector[i, 11]), ', ',\
                                  str(featureVector[i, 12]), ', ', str(featureVector[i, 13]), ', ', str(featureVector[i, 14]), ', ', str(featureVector[i, 15]), ', ',\
                                  str(featureVector[i, 16]), ', ', str(optimalNeighbor_len[i]), '\n'])
    writefilePosition.close()
    end_time = datetime.now()
    print('--------------All done : {} : {}------------end time: {}----------------'.format(path_w, end_time - start_time, end_time))
















