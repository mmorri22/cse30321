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

def time_loop_sort( data, arraySize, num_loops ):
    
    sum = 0

    data_sorted = sorted(data)
    
    for i in range(0, num_loops):
        
        for c in range(0, arraySize):
            
            if data_sorted[c] >= 128:
                
                sum += data_sorted[c]

    print('sum = ', sum)

data = get_data(arraySize)'''

mystmt='''time_loop_sort( data, arraySize, num_loops )'''

time = timeit.timeit(setup=mysetup,stmt=mystmt, number=1)

print(time, 'sec')