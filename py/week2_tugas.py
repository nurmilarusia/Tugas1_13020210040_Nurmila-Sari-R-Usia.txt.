from mpi4py import MPI
import os

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
home_dir =os.path.expanduser('~')

if rank % 2 == 0:
    print("Anda prosses Genap jika", "Rank",comm.rank,home_dir)
else:
    print("Anda prosses Genap jika", "Rank",comm.rank,home_dir)
