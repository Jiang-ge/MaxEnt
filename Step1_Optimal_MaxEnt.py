import math
import MyFileOperator
import numpy as np
from sklearn.neighbors import NearestNeighbors
import Step2_CalculateFeatureVector
from datetime import datetime
import f_homogeneous_e213
import f_homogeneous

def mpi_entrance(path_r, path_w):
    channel2_data = MyFileOperator.readData_10(path_r+'L1C2_addC1C3_train.txt')
    start_time = datetime.now()
    featureVectorList_e213 = []
    featureVectorList_e = []
    featureVectorList_ch2 = []
    featureVectorList_ch1 = []
    featureVectorList_ch3 = []
    optimalNeighbor_e213_len = []
    optimalNeighbor_e_len = []
    optimalNeighbor_ch2_len = []
    optimalNeighbor_ch1_len = []
    optimalNeighbor_ch3_len = []
    nbrs = NearestNeighbors(n_neighbors=1000, algorithm='kd_tree').fit(channel2_data[:, 1:4])
    distances, indices = nbrs.kneighbors(channel2_data[:, 1:4])
    for n in range(len(channel2_data)):
        centerPoint = np.array([channel2_data[n, :]])
        neighbor = channel2_data[indices[n, :]]

        optimalNeighbor_e_refine = f_homogeneous.homogeneousPointsSearch(neighbor, 3, centerPoint)
        optimalNeighbor_e_len.append(len(optimalNeighbor_e_refine))
        featureVectorList_e.append(
            Step2_CalculateFeatureVector.calculateFeatureVector(optimalNeighbor_e_refine, centerPoint))
        optimalNeighbor_ch2_refine = f_homogeneous.homogeneousPointsSearch(neighbor, 4, centerPoint)
        optimalNeighbor_ch2_len.append(len(optimalNeighbor_ch2_refine))
        featureVectorList_ch2.append(
            Step2_CalculateFeatureVector.calculateFeatureVector(optimalNeighbor_ch2_refine, centerPoint))
        optimalNeighbor_ch1_refine = f_homogeneous.homogeneousPointsSearch(neighbor, 7, centerPoint)
        optimalNeighbor_ch1_len.append(len(optimalNeighbor_ch1_refine))
        featureVectorList_ch1.append(
            Step2_CalculateFeatureVector.calculateFeatureVector(optimalNeighbor_ch1_refine, centerPoint))
        optimalNeighbor_ch3_refine = f_homogeneous.homogeneousPointsSearch(neighbor, 9, centerPoint)
        optimalNeighbor_ch3_len.append(len(optimalNeighbor_ch3_refine))
        featureVectorList_ch3.append(
            Step2_CalculateFeatureVector.calculateFeatureVector(optimalNeighbor_ch3_refine, centerPoint))

        optimalNeighbor_e213_refine = f_homogeneous_e213.homogeneousPointsSearch(optimalNeighbor_e_refine,
                                                                                 optimalNeighbor_ch2_refine,
                                                                                 optimalNeighbor_ch1_refine,
                                                                                 optimalNeighbor_ch3_refine)
        if len(optimalNeighbor_e213_refine) < 10:
            nbrs_small = NearestNeighbors(n_neighbors=15, algorithm='kd_tree').fit(neighbor[:, 1:4])
            dis, ind = nbrs_small.kneighbors(np.array([centerPoint[0, 1:4]]))
            optimalNeighbor_e213_refine = neighbor[ind[0, :]]
        if centerPoint[0, 3] < 0.2:
            optimalNeighbor_e213_refine = optimalNeighbor_e213_refine[np.where(optimalNeighbor_e213_refine[:, 3] < 0.2)]
        elif centerPoint[0, 3] > 0.64 and centerPoint[0, 3] < 2.35:
            optimalNeighbor_e213_refine1 = optimalNeighbor_e213_refine[
                np.where(optimalNeighbor_e213_refine[:, 3] > (centerPoint[0, 3] - 0.5))]
            optimalNeighbor_e213_refine = optimalNeighbor_e213_refine1[
                np.where(optimalNeighbor_e213_refine1[:, 3] < (centerPoint[0, 3] + 0.5))]
        elif centerPoint[0, 3] > 2.5:
            optimalNeighbor_e213_refine = optimalNeighbor_e213_refine[np.where(optimalNeighbor_e213_refine[:, 3] > 2.5)]
        optimalNeighbor_e213_len.append(len(optimalNeighbor_e213_refine))
        featureVectorList_e213.append(
            Step2_CalculateFeatureVector.calculateFeatureVector(optimalNeighbor_e213_refine, centerPoint))

    featureVector_e213 = np.array(featureVectorList_e213)
    optimalNeighbor_e213_len = np.array(optimalNeighbor_e213_len)
    writefilePosition = open(path_w + 'featureVector_e213.txt', "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(featureVector_e213)):
        writefilePosition.writelines(
            [str(featureVector_e213[i, 0]), ', ', str(featureVector_e213[i, 1]), ', ', str(featureVector_e213[i, 2]),
             ', ', str(featureVector_e213[i, 3]), ', ', \
             str(featureVector_e213[i, 4]), ', ', str(featureVector_e213[i, 5]), ', ', str(featureVector_e213[i, 6]),
             ', ', str(featureVector_e213[i, 7]), ', ', \
             str(featureVector_e213[i, 8]), ', ', str(featureVector_e213[i, 9]), ', ', str(featureVector_e213[i, 10]),
             ', ', str(featureVector_e213[i, 11]), ', ', \
             str(featureVector_e213[i, 12]), ', ', str(featureVector_e213[i, 13]), ', ', str(featureVector_e213[i, 14]),
             ', ', str(featureVector_e213[i, 15]), ', ', \
             str(featureVector_e213[i, 16]), ', ', str(optimalNeighbor_e213_len[i]), '\n'])
    writefilePosition.close()

    featureVector_e = np.array(featureVectorList_e)
    optimalNeighbor_e_len = np.array(optimalNeighbor_e_len)
    writefilePosition = open(path_w + 'featureVector_e.txt', "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(featureVector_e)):
        writefilePosition.writelines(
            [str(featureVector_e[i, 0]), ', ', str(featureVector_e[i, 1]), ', ', str(featureVector_e[i, 2]), ', ',
             str(featureVector_e[i, 3]), ', ', \
             str(featureVector_e[i, 4]), ', ', str(featureVector_e[i, 5]), ', ', str(featureVector_e[i, 6]), ', ',
             str(featureVector_e[i, 7]), ', ', \
             str(featureVector_e[i, 8]), ', ', str(featureVector_e[i, 9]), ', ', str(featureVector_e[i, 10]), ', ',
             str(featureVector_e[i, 11]), ', ', \
             str(featureVector_e[i, 12]), ', ', str(featureVector_e[i, 13]), ', ', str(featureVector_e[i, 14]), ', ',
             str(featureVector_e[i, 15]), ', ', \
             str(featureVector_e[i, 16]), ', ', str(optimalNeighbor_e_len[i]), '\n'])
    writefilePosition.close()

    featureVector_ch2 = np.array(featureVectorList_ch2)
    optimalNeighbor_ch2_len = np.array(optimalNeighbor_ch2_len)
    writefilePosition = open(path_w + 'featureVector_ch2.txt', "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(featureVector_ch2)):
        writefilePosition.writelines(
            [str(featureVector_ch2[i, 0]), ', ', str(featureVector_ch2[i, 1]), ', ', str(featureVector_ch2[i, 2]), ', ',
             str(featureVector_ch2[i, 3]), ', ', \
             str(featureVector_ch2[i, 4]), ', ', str(featureVector_ch2[i, 5]), ', ', str(featureVector_ch2[i, 6]), ', ',
             str(featureVector_ch2[i, 7]), ', ', \
             str(featureVector_ch2[i, 8]), ', ', str(featureVector_ch2[i, 9]), ', ', str(featureVector_ch2[i, 10]),
             ', ', str(featureVector_ch2[i, 11]), ', ', \
             str(featureVector_ch2[i, 12]), ', ', str(featureVector_ch2[i, 13]), ', ', str(featureVector_ch2[i, 14]),
             ', ', str(featureVector_ch2[i, 15]), ', ', \
             str(featureVector_ch2[i, 16]), ', ', str(optimalNeighbor_ch2_len[i]), '\n'])
    writefilePosition.close()

    featureVector_ch1 = np.array(featureVectorList_ch1)
    optimalNeighbor_ch1_len = np.array(optimalNeighbor_ch1_len)
    writefilePosition = open(path_w + 'featureVector_ch1.txt', "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(featureVector_ch1)):
        writefilePosition.writelines(
            [str(featureVector_ch1[i, 0]), ', ', str(featureVector_ch1[i, 1]), ', ', str(featureVector_ch1[i, 2]), ', ',
             str(featureVector_ch1[i, 3]), ', ', \
             str(featureVector_ch1[i, 4]), ', ', str(featureVector_ch1[i, 5]), ', ', str(featureVector_ch1[i, 6]), ', ',
             str(featureVector_ch1[i, 7]), ', ', \
             str(featureVector_ch1[i, 8]), ', ', str(featureVector_ch1[i, 9]), ', ', str(featureVector_ch1[i, 10]),
             ', ', str(featureVector_ch1[i, 11]), ', ', \
             str(featureVector_ch1[i, 12]), ', ', str(featureVector_ch1[i, 13]), ', ', str(featureVector_ch1[i, 14]),
             ', ', str(featureVector_ch1[i, 15]), ', ', \
             str(featureVector_ch1[i, 16]), ', ', str(optimalNeighbor_ch1_len[i]), '\n'])
    writefilePosition.close()

    featureVector_ch3 = np.array(featureVectorList_ch3)
    optimalNeighbor_ch3_len = np.array(optimalNeighbor_ch3_len)
    writefilePosition = open(path_w + 'featureVector_ch3.txt', "a")
    writefilePosition.seek(0)
    writefilePosition.truncate()
    for i in range(len(featureVector_ch3)):
        writefilePosition.writelines(
            [str(featureVector_ch3[i, 0]), ', ', str(featureVector_ch3[i, 1]), ', ', str(featureVector_ch3[i, 2]), ', ',
             str(featureVector_ch3[i, 3]), ', ', \
             str(featureVector_ch3[i, 4]), ', ', str(featureVector_ch3[i, 5]), ', ', str(featureVector_ch3[i, 6]), ', ',
             str(featureVector_ch3[i, 7]), ', ', \
             str(featureVector_ch3[i, 8]), ', ', str(featureVector_ch3[i, 9]), ', ', str(featureVector_ch3[i, 10]),
             ', ', str(featureVector_ch3[i, 11]), ', ', \
             str(featureVector_ch3[i, 12]), ', ', str(featureVector_ch3[i, 13]), ', ', str(featureVector_ch3[i, 14]),
             ', ', str(featureVector_ch3[i, 15]), ', ', \
             str(featureVector_ch3[i, 16]), ', ', str(optimalNeighbor_ch3_len[i]), '\n'])
    writefilePosition.close()
    end_time = datetime.now()
    print('--------------All done : {} : {}------------end time: {}----------------'.format(path_w, end_time - start_time, end_time))















