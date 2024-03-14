# If you get the following error:
#   ModuleNotFoundError: No module named 'numpy'
# This is because you do not have numpy installed.
# To do so, from the command line, perform the following command:
#   pip3 install numpy
# You should only need to perform the command once

import time
import numpy

# N is array size
# c = a * b
def dgemm_matrix( N, a_array, b_array, c_array ):  
    for i in range(N):
        for j in range(N):
            cij = c_array[i][j]

            for k in range(N):
                cij += a_array[i][k] * b_array[k][j]
                
            c_array[i][j] = cij

print('Enter the matrix dimension:')
N = int(input())

# a matrix:
a_matrix = numpy.random.randn(N, N).astype(numpy.float32)
b_matrix = numpy.random.randn(N, N).astype(numpy.float32)

# result matrix
c_matrix = [[0 for x in range(N)] for y in range(N)] 

start_time = time.time()
dgemm_matrix( N, a_matrix, b_matrix, c_matrix )
end_time = time.time()

# Total us
total_time = (end_time - start_time) * 100000

print("Time: Start = ",start_time, ", End = ", end_time)
print("Total Time: ",total_time, "us")