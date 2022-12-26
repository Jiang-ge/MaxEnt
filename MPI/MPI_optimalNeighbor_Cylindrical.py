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


path_r_train = 'Data/cutArea/train_test/train/{bulk}/'
path_r_test = 'Data/cutArea/train_test/test/{bulk}/'

path_Cylindrical_train = 'Data/cutArea/MultiScaleCylindrical/train/{bulk}/'
i = 0
if rank == i:  # i = 0
    rank_new = rank
    print('train_MultiScaleCylindrical_0: ' + str(rank))
    Step1_MultiScale_Cylindrical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Cylindrical_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank
    print('train_MultiScaleCylindrical_1: ' + str(rank))
    Step1_MultiScale_Cylindrical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Cylindrical_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank
    print('train_MultiScaleCylindrical_2: ' + str(rank))
    Step1_MultiScale_Cylindrical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Cylindrical_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank
    print('train_MultiScaleCylindrical_3: ' + str(rank))
    Step1_MultiScale_Cylindrical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Cylindrical_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank
    print('train_MultiScaleCylindrical_4: ' + str(rank))
    Step1_MultiScale_Cylindrical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Cylindrical_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank
    print('train_MultiScaleCylindrical_5: ' + str(rank))
    Step1_MultiScale_Cylindrical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Cylindrical_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank
    print('train_MultiScaleCylindrical_6: ' + str(rank))
    Step1_MultiScale_Cylindrical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Cylindrical_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank
    print('train_MultiScaleCylindrical_7: ' + str(rank))
    Step1_MultiScale_Cylindrical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Cylindrical_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank
    print('train_MultiScaleCylindrical_8: ' + str(rank))
    Step1_MultiScale_Cylindrical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Cylindrical_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank
    print('train_MultiScaleCylindrical_9: ' + str(rank))
    Step1_MultiScale_Cylindrical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Cylindrical_train.format(bulk=rank_new))


# path_Cylindrical_test = 'Data/cutArea/MultiScaleCylindrical/test/{bulk}/'
# Cylindrical_flag = 10
# i = i + 1
# if rank == i:
#     rank_new = rank - Cylindrical_flag  # 0
#     print('test_MultiScaleCylindrical_0: ' + str(rank))
#     Step1_MultiScale_Cylindrical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Cylindrical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Cylindrical_flag
#     print('test_MultiScaleCylindrical_1: ' + str(rank))
#     Step1_MultiScale_Cylindrical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Cylindrical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Cylindrical_flag
#     print('test_MultiScaleCylindrical_2: ' + str(rank))
#     Step1_MultiScale_Cylindrical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Cylindrical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Cylindrical_flag
#     print('test_MultiScaleCylindrical_3: ' + str(rank))
#     Step1_MultiScale_Cylindrical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Cylindrical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Cylindrical_flag
#     print('test_MultiScaleCylindrical_4: ' + str(rank))
#     Step1_MultiScale_Cylindrical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Cylindrical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Cylindrical_flag
#     print('test_MultiScaleCylindrical_5: ' + str(rank))
#     Step1_MultiScale_Cylindrical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Cylindrical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Cylindrical_flag
#     print('test_MultiScaleCylindrical_6: ' + str(rank))
#     Step1_MultiScale_Cylindrical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Cylindrical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Cylindrical_flag
#     print('test_MultiScaleCylindrical_7: ' + str(rank))
#     Step1_MultiScale_Cylindrical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Cylindrical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Cylindrical_flag
#     print('test_MultiScaleCylindrical_8: ' + str(rank))
#     Step1_MultiScale_Cylindrical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Cylindrical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Cylindrical_flag  # 9
#     print('test_MultiScaleCylindrical_9: ' + str(rank))
#     Step1_MultiScale_Cylindrical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Cylindrical_test.format(bulk=rank_new))








