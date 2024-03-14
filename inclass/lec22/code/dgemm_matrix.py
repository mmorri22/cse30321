import time

# N is array size
# c = a * b
def dgemm_matrix( N, a_array, b_array, c_array ):  
    for i in range(N):
        for j in range(N):
            c_array[i][j] = 0
            for k in range(N):
                c_array[i][j] += a_array[i][k] * b_array[k][j]

N = 4

# a matrix:
# 1 7 3 4
# 2 1 8 5
# 2 6 2 1
# 4 3 4 7
a_matrix = [[1,7,3,4],[2,1,8,5],[2,6,2,1],[4,3,4,7]]

# b matrix
# 1 2 3 4
# 5 6 7 8
# 9 0 1 2
# 3 4 5 6
b_matrix = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6]]

# result matrix
c_matrix = [[0 for x in range(N)] for y in range(N)] 

start_time = time.time()
dgemm_matrix( N, a_matrix, b_matrix, c_matrix )
end_time = time.time()

# Total us
total_time = (end_time - start_time) * 100000

print("Time: Start = ",start_time, ", End = ", end_time)
print("Total Time: ",total_time, "us")