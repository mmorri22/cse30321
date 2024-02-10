# Given the mapping of registers to variables below, write a program to implement the following expression:
# 
# int array_sum(int* A, int length){
# 
# 	int sum = 0;
# 	for(int i = 0; i < length; ++i){
# 		sum += A[i];
#   }
#   return sum;
# }
# 
# int main(){
# 	int array[] = {13, 7, -8, 4};
# 	int array_len = 4;
# 	int result_sum = array_sum( array, array_len );
# 	return 0;
# }
# 
# In main, array is in x18 and points to 0x7fff1a10, array_len is in x19, and result_sum is in x20. 
# In array_sum, sum is in x21 and i is in x22.