from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
from datetime import datetime
import Step1_MultiScale_Cylindrical_train
import Step1_MultiScale_Cylindrical_test
import Step1_MultiScale_Spherical_train
import Step1_MultiScale_Spherical_test
import Step1_MultiScale_KNN_train
import Step1_MultiScale_KNN_test


start_time = datetime.now()
# print('----------------MPI_test_0:-----start time : {} -----------------------------'.format(start_time))

path_r_train = 'Data/cutArea/train_test/train/{bulk}/'
path_r_test = 'Data/cutArea/train_test/test/{bulk}/'


# path_KNN_train = 'Data/cutArea/MultiScaleKNN/train/{bulk}/'
# i = 0
# KNN_train_flag = 9
# if rank == i:  # i = 0
#     rank_new = rank + KNN_train_flag
#     print('train_MultiScaleKNN_0: ' + str(rank_new))
#     Step1_MultiScale_KNN_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_KNN_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 1
#     rank_new = rank - KNN_train_flag
#     print('train_MultiScaleKNN_1: ' + str(rank))
#     Step1_MultiScale_KNN_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_KNN_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 2
#     rank_new = rank - KNN_train_flag
#     print('train_MultiScaleKNN_2: ' + str(rank))
#     Step1_MultiScale_KNN_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_KNN_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 3
#     rank_new = rank - KNN_train_flag
#     print('train_MultiScaleKNN_3: ' + str(rank))
#     Step1_MultiScale_KNN_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_KNN_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 4
#     rank_new = rank - KNN_train_flag
#     print('train_MultiScaleKNN_4: ' + str(rank))
#     Step1_MultiScale_KNN_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_KNN_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 5
#     rank_new = rank - KNN_train_flag
#     print('train_MultiScaleKNN_5: ' + str(rank))
#     Step1_MultiScale_KNN_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_KNN_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 6
#     rank_new = rank - KNN_train_flag
#     print('train_MultiScaleKNN_6: ' + str(rank))
#     Step1_MultiScale_KNN_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_KNN_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 7
#     rank_new = rank - KNN_train_flag
#     print('train_MultiScaleKNN_7: ' + str(rank))
#     Step1_MultiScale_KNN_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_KNN_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 8
#     rank_new = rank - KNN_train_flag
#     print('train_MultiScaleKNN_8: ' + str(rank))
#     Step1_MultiScale_KNN_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_KNN_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 9
#     rank_new = rank - KNN_train_flag
#     print('train_MultiScaleKNN_9: ' + str(rank))
#     Step1_MultiScale_KNN_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_KNN_train.format(bulk=rank_new))
#
#
path_KNN_test = 'Data/cutArea/MultiScaleKNN/test/{bulk}/'
KNN_test_flag = 9
i = 0
if rank == i:
    rank_new = rank + KNN_test_flag
    print('test_MultiScaleKNN_0: ' + str(rank_new))
    Step1_MultiScale_KNN_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_KNN_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - KNN_test_flag
#     print('test_MultiScaleKNN_1: ' + str(rank))
#     Step1_MultiScale_KNN_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_KNN_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - KNN_test_flag
#     print('test_MultiScaleKNN_2: ' + str(rank))
#     Step1_MultiScale_KNN_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_KNN_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - KNN_test_flag
#     print('test_MultiScaleKNN_3: ' + str(rank))
#     Step1_MultiScale_KNN_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_KNN_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - KNN_test_flag
#     print('test_MultiScaleKNN_4: ' + str(rank))
#     Step1_MultiScale_KNN_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_KNN_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - KNN_test_flag
#     print('test_MultiScaleKNN_5: ' + str(rank))
#     Step1_MultiScale_KNN_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_KNN_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - KNN_test_flag
#     print('test_MultiScaleKNN_6: ' + str(rank))
#     Step1_MultiScale_KNN_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_KNN_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - KNN_test_flag
#     print('test_MultiScaleKNN_7: ' + str(rank))
#     Step1_MultiScale_KNN_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_KNN_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - KNN_test_flag
#     print('test_MultiScaleKNN_8: ' + str(rank))
#     Step1_MultiScale_KNN_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_KNN_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - KNN_test_flag
#     print('test_MultiScaleKNN_9: ' + str(rank))
#     Step1_MultiScale_KNN_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_KNN_test.format(bulk=rank_new))

