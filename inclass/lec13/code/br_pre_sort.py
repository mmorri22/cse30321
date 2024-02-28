import timeit

mysetup='''import random
import timeit

arraySize = 32768
# num_loops = 1000
num_loops = 100000

def get_data( arraySize ):

    data = []

    for c in range(0, arraySize):

        data.append( random.randint(0,256) )
        
    return data

def time_loop_no_sort( data, arraySize, num_loops ):
    
    sum = 0
    
    for i in range(0, num_loops):
        
        for c in range(0, arraySize):
            
            if data[c] >= 128:
                
                sum += data[c]

    print('sum = ', sum)

data = get_data(arraySize)
data_sorted = sorted(data)'''

mystmt='''time_loop_no_sort( data_sorted, arraySize, num_loops )'''

time = timeit.timeit(setup=mysetup,stmt=mystmt, number=1)

print(time, 'sec')