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
import Step1_Optimal_Belton_train
# import Step1_Optimal_Belton_test
import MyFileOperator

start_time = datetime.now()
# print('----------------MPI_test_0:-----start time : {} -----------------------------'.format(start_time))

path_r_train = 'Data/cutArea/train_test/train/0/{bulk}/'
path_r_test = 'Data/cutArea/train_test/test/{bulk}/'



path_OptimalBelton_train = 'Data/cutArea/OptimalBelton/train/0/{bulk}/'
i = 0
OptimalBelton_train_flag = 0
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_0: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_1: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_2: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_3: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_4: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_5: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_6: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_7: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_8: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_9: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))

# 10
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_10: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_11: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_12: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_13: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_14: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_15: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_16: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_17: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_18: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_19: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
    


# 20
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_20: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_21: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_22: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_23: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_24: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_25: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_26: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_27: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_28: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_29: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))



# 30
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_30: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_31: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_32: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_33: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_34: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_35: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_36: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_37: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_38: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_39: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))



# 40
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_40: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_41: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_42: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_43: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_44: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_45: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_46: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_47: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_48: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_49: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))



# 50
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_50: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_51: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_52: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_53: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_54: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_55: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_56: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_57: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_58: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_59: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))



# 60
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_60: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_61: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_62: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_63: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_64: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_65: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_66: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_67: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_68: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_69: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new), path_OptimalBelton_train.format(bulk=rank_new))




# 70
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_70: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_71: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_72: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_73: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_74: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_75: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_76: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_77: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_78: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_79: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))

# 80
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_80: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_81: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_82: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_83: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_84: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_85: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_86: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_87: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_88: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_89: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))

# 90
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_90: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_91: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_92: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_93: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_94: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_95: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_96: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_97: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_98: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_99: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))

# 100
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_100: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_101: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_102: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_103: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_104: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_105: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_106: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_107: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_108: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_109: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))


# 110
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_110: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_111: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_112: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_113: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_114: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_115: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_116: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_117: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_118: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_119: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))


# 120
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_120: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_121: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_122: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_123: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_124: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_125: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_126: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_127: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_128: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_129: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))


# 130
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_130: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_131: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_132: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_133: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_134: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_135: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_136: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_137: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_138: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_139: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))


# 140
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_140: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_141: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_142: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_143: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_144: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_145: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_146: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_147: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_148: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_149: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))


# 150
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_150: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_151: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_152: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_153: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_154: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_155: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_156: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_157: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_158: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_159: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))


# 160
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_160: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_161: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_162: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_163: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_164: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_165: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_166: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_167: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_168: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_169: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))


# 170
i = i + 1
if rank == i:  # i = 0
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_170: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 1
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_171: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 2
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_172: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 3
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_173: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 4
    rank_new = rank - OptimalBelton_train_flag
    print('train_OptimalBelton_174: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 5
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_175: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 6
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_176: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 7
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_177: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 8
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_178: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))
i = i + 1
if rank == i:  # i = 9
    rank_new = rank + OptimalBelton_train_flag
    print('train_OptimalBelton_179: ' + str(rank))
    Step1_Optimal_Belton_train.mpi_entrance(path_r_train.format(bulk=rank_new),
                                                    path_OptimalBelton_train.format(bulk=rank_new))

