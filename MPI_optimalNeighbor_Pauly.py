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
import Step1_Optimal_Pauly_train
# import Step1_Optimal_Pauly_test
import MyFileOperator

start_time = datetime.now()
# print('----------------MPI_test_0:-----start time : {} -----------------------------'.format(start_time))

path_r_train = 'Data/cutArea/train_test/train/0/{bulk}/'
path_r_test = 'Data/cutArea/train_test/test/{bulk}/'



path_OptimalPauly_train = 'Data/cutArea/OptimalPauly/train/0/{bulk}/'
i = 0
OptimalPauly_train_flag = 0
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_0: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_1: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_2: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_3: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_4: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_5: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_6: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_7: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_8: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_9: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))

# 10
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_10: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_11: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_12: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_13: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_14: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_15: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_16: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_17: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_18: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_19: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
    


# 20
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_20: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_21: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_22: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_23: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_24: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_25: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_26: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_27: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_28: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_29: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))



# 30
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_30: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_31: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_32: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_33: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_34: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_35: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_36: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_37: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_38: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_39: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))



# 40
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_40: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_41: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_42: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_43: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_44: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_45: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_46: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_47: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_48: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_49: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))



# 50
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_50: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_51: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_52: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_53: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_54: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_55: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_56: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_57: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_58: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_59: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))



# 60
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_60: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_61: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_62: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_63: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_64: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_65: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_66: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_67: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_68: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_69: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalPauly_train.format(bulk=rank_new))




# 70
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_70: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_71: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_72: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_73: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_74: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_75: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_76: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_77: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_78: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_79: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))

# 80
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_80: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_81: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_82: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_83: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_84: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_85: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_86: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_87: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_88: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_89: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))

# 90
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_90: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_91: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_92: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_93: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_94: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_95: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_96: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_97: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_98: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_99: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))

# 100
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_100: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_101: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_102: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_103: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_104: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_105: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_106: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_107: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_108: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_109: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))


# 110
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_110: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_111: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_112: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_113: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_114: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_115: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_116: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_117: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_118: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_119: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))


# 120
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_120: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_121: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_122: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_123: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_124: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_125: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_126: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_127: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_128: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_129: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))


# 130
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_130: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_131: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_132: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_133: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_134: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_135: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_136: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_137: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_138: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_139: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))


# 140
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_140: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_141: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_142: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_143: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_144: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_145: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_146: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_147: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_148: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_149: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))


# 150
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_150: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_151: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_152: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_153: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_154: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_155: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_156: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_157: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_158: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_159: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))


# 160
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_160: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_161: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_162: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_163: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_164: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_165: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_166: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_167: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_168: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_169: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))


# 170
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_170: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_171: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_172: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_173: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalPauly_train_flag
    print('train_OptimalPauly_174: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_175: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_176: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_177: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_178: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalPauly_train_flag
    print('train_OptimalPauly_179: ' + str(rank))
    Step1_Optimal_Pauly_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalPauly_train.format(bulk=rank_new))

