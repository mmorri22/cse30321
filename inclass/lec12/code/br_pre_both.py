import random
import timeit

def get_data( arraySize ):

    data = []

    for c in range(0, arraySize):

        data.append( random.randint(0,256) )
        
    return data


def time_loop_sort( data, arraySize ):
    
    data_sort = sorted(data)
    
    sum = 0
    
    for i in range(0, 100000):
        
        for c in range(0, arraySize):
            
            if data[c] >= 128:
                
                sum += data[c]

# Run the code and test
data = get_data(32768)

timeit( time_loop_sort( data, 32768 ) )