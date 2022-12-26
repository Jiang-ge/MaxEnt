from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
from datetime import datetime
import Step1_MultiScale_Cylindrical_train
import Step1_MultiScale_Cylindrical_test
import Step1_MultiScale_Spherical_train
import Step1_MultiScale_Spherical_test

start_time = datetime.now()


path_r_train = 'Data/cutArea/train_test/train/{bulk}/'
path_r_test = 'Data/cutArea/train_test/test/{bulk}/'

# path_Spherical_train = 'Data/cutArea/MultiScaleSpherical/train/{bulk}/'
# Spherical_train_flag = 9
# i = 0
# Spherical_train_flag = 0
# if rank == i:  # i = 0
#     rank_new = rank + Spherical_train_flag
#     print('train_MultiScaleSpherical_0: ' + str(rank_new))
#     Step1_MultiScale_Spherical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Spherical_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 1
#     rank_new = rank - Spherical_train_flag
#     print('train_MultiScaleSpherical_1: ' + str(rank))
#     Step1_MultiScale_Spherical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Spherical_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 2
#     rank_new = rank - Spherical_train_flag
#     print('train_MultiScaleSpherical_2: ' + str(rank))
#     Step1_MultiScale_Spherical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Spherical_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 3
#     rank_new = rank - Spherical_train_flag
#     print('train_MultiScaleSpherical_3: ' + str(rank))
#     Step1_MultiScale_Spherical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Spherical_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 4
#     rank_new = rank - Spherical_train_flag
#     print('train_MultiScaleSpherical_4: ' + str(rank))
#     Step1_MultiScale_Spherical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Spherical_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 5
#     rank_new = rank - Spherical_train_flag
#     print('train_MultiScaleSpherical_5: ' + str(rank))
#     Step1_MultiScale_Spherical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Spherical_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 6
#     rank_new = rank - Spherical_train_flag
#     print('train_MultiScaleSpherical_6: ' + str(rank))
#     Step1_MultiScale_Spherical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Spherical_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 7
#     rank_new = rank - Spherical_train_flag
#     print('train_MultiScaleSpherical_7: ' + str(rank))
#     Step1_MultiScale_Spherical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Spherical_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 8
#     rank_new = rank - Spherical_train_flag
#     print('train_MultiScaleSpherical_8: ' + str(rank))
#     Step1_MultiScale_Spherical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Spherical_train.format(bulk=rank_new))
# i = i + 1
# if rank == i:  # i = 9
#     rank_new = rank - Spherical_train_flag
#     print('train_MultiScaleSpherical_9: ' + str(rank))
#     Step1_MultiScale_Spherical_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_Spherical_train.format(bulk=rank_new))
#
#
path_Spherical_test = 'Data/cutArea/MultiScaleSpherical/test/{bulk}/'
Spherical_test_flag = 9
i = 0
if rank == i:
    rank_new = rank + Spherical_test_flag
    print('test_MultiScaleSpherical_0: ' + str(rank_new))
    Step1_MultiScale_Spherical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Spherical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Spherical_test_flag
#     print('test_MultiScaleSpherical_1: ' + str(rank))
#     Step1_MultiScale_Spherical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Spherical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Spherical_test_flag
#     print('test_MultiScaleSpherical_2: ' + str(rank))
#     Step1_MultiScale_Spherical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Spherical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Spherical_test_flag
#     print('test_MultiScaleSpherical_3: ' + str(rank))
#     Step1_MultiScale_Spherical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Spherical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Spherical_test_flag
#     print('test_MultiScaleSpherical_4: ' + str(rank))
#     Step1_MultiScale_Spherical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Spherical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Spherical_test_flag
#     print('test_MultiScaleSpherical_5: ' + str(rank))
#     Step1_MultiScale_Spherical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Spherical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Spherical_test_flag
#     print('test_MultiScaleSpherical_6: ' + str(rank))
#     Step1_MultiScale_Spherical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Spherical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Spherical_test_flag
#     print('test_MultiScaleSpherical_7: ' + str(rank))
#     Step1_MultiScale_Spherical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Spherical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Spherical_test_flag
#     print('test_MultiScaleSpherical_8: ' + str(rank))
#     Step1_MultiScale_Spherical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Spherical_test.format(bulk=rank_new))
# i = i + 1
# if rank == i:
#     rank_new = rank - Spherical_test_flag
#     print('test_MultiScaleSpherical_9: ' + str(rank))
#     Step1_MultiScale_Spherical_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_Spherical_test.format(bulk=rank_new))




