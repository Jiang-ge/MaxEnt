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
import Step1_Optimal_Weinmann_train
import Step1_Optimal_Weinmann_test
import Step1_OptimalNeighbor_maxEnt_train_180
import Step1_OptimalNeighbor_maxEnt_test
import MyFileOperator

start_time = datetime.now()
# print('----------------MPI_test_0:-----start time : {} -----------------------------'.format(start_time))

path_r_train = 'Data/cutArea/train_test/train/{bulk}/'
path_r_test = 'Data/cutArea/train_test/test/{bulk}/'


path_w_train = 'Data/cutArea/OptimalWeinmann/train/{bulk}/'
i = 0
w_train_flag = 0
if rank == i:  # i = 0
    rank_new = rank - w_train_flag
    print('train_w_0: ' + str(rank))
    Step1_Optimal_Weinmann_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_w_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - w_train_flag
    print('train_w_1: ' + str(rank))
    Step1_Optimal_Weinmann_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_w_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - w_train_flag
    print('train_w_2: ' + str(rank))
    Step1_Optimal_Weinmann_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_w_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - w_train_flag
    print('train_w_3: ' + str(rank))
    Step1_Optimal_Weinmann_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_w_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - w_train_flag
    print('train_w_4: ' + str(rank))
    Step1_Optimal_Weinmann_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_w_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank - w_train_flag
    print('train_w_5: ' + str(rank))
    Step1_Optimal_Weinmann_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_w_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank - w_train_flag
    print('train_w_6: ' + str(rank))
    Step1_Optimal_Weinmann_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_w_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank - w_train_flag
    print('train_w_7: ' + str(rank))
    Step1_Optimal_Weinmann_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_w_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank - w_train_flag
    print('train_w_8: ' + str(rank))
    Step1_Optimal_Weinmann_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_w_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank - w_train_flag
    print('train_w_9: ' + str(rank))
    Step1_Optimal_Weinmann_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_w_train.format(bulk=rank_new))


path_w_test = 'Data/cutArea/OptimalKNN(Weinmann)/test/{bulk}/'
w_test_flag = 10
i = i + 1
if rank == i:
    rank_new = rank - w_test_flag
    print('test_w_0: ' + str(rank))
    Step1_Optimal_Weinmann_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_w_test.format(bulk=rank_new))
i = i + 1
if rank == i:
    rank_new = rank - w_test_flag
    print('test_w_1: ' + str(rank))
    Step1_Optimal_Weinmann_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_w_test.format(bulk=rank_new))
i = i + 1
if rank == i:
    rank_new = rank - w_test_flag
    print('test_w_2: ' + str(rank))
    Step1_Optimal_Weinmann_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_w_test.format(bulk=rank_new))
i = i + 1
if rank == i:
    rank_new = rank - w_test_flag
    print('test_w_3: ' + str(rank))
    Step1_Optimal_Weinmann_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_w_test.format(bulk=rank_new))
i = i + 1
if rank == i:
    rank_new = rank - w_test_flag
    print('test_w_4: ' + str(rank))
    Step1_Optimal_Weinmann_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_w_test.format(bulk=rank_new))
i = i + 1
if rank == i:
    rank_new = rank - w_test_flag
    print('test_w_5: ' + str(rank))
    Step1_Optimal_Weinmann_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_w_test.format(bulk=rank_new))
i = i + 1
if rank == i:
    rank_new = rank - w_test_flag
    print('test_w_6: ' + str(rank))
    Step1_Optimal_Weinmann_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_w_test.format(bulk=rank_new))
i = i + 1
if rank == i:
    rank_new = rank - w_test_flag
    print('test_w_7: ' + str(rank))
    Step1_Optimal_Weinmann_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_w_test.format(bulk=rank_new))
i = i + 1
if rank == i:
    rank_new = rank - w_test_flag
    print('test_w_8: ' + str(rank))
    Step1_Optimal_Weinmann_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_w_test.format(bulk=rank_new))
i = i + 1
if rank == i:
    rank_new = rank - w_test_flag
    print('test_w_9: ' + str(rank))
    Step1_Optimal_Weinmann_test.mpi_entrance(path_r_test.format(bulk=rank_new), path_w_test.format(bulk=rank_new))





