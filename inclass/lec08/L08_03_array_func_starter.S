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
#
# Ensure all garbage is properly collected at the end of the program.

# Starter Code
MAIN:

# 1. Store the base address in x18 of 0x7fff1a10
lui x5, 0x7fff1
addi x18, x5, 0xa10

# 2. Store the array elements. 


# 3. Store the length


# 4. Put in function inputs


# 5. Call the function and clear function arguments


# 6. Load the results back into the local registers 


# 7. Return 0


# 10. Name the function call
##########################################
# Procedure Name: ARRAY_SUM
# Pre-conditions: x12 contains the base address of an sll_node
# Post-conditions: 
#
# This procedure clears 96 bits (12 bytes) of memory 
# previously allocated to a sll_node
##########################################
ARRAY_SUM:

# 11. Set the values of x21 and x22 to 0


# 12. Write the loop
BEGIN_LOOP:


# 13. Jump and link back to main
END_LOOP:

# 14. Return result


# 15. Clear local variables and go back to main


# 16. Terminate the program
END:
quit