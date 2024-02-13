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

lui x5, 0x7fff1
addi x18, x5, 0xa10

# Store the array elementd
addi x6, x0, 13
addi x7, x0, 7
addi x28, x0, -8
addi x29, x0, 4

sw x6, 0(x18)
sw x7, 4(x18)
sw x28, 8(x18)
sw x29, 12(x18)

# Store the length
addi x19, x0, 4

# Put in function inputs
addi x12, x18, 0
addi x13, x19, 0

# Call the function and clear function arguments
jal x1, ARRAY_SUM
add x1, x0, x0
add x13, x0, x0
add x12, x0, x0

# Load the results back into the local registers 
add x20, x10, x0
add x10, x0, x0

# Return 0
add x20, x0, x0
add x19, x0, x0
add x18, x0, x0
add x5, x0, x0
beq x0, x0, END

# Name the function call
##########################################
# Procedure Name: ARRAY_SUM
# Pre-conditions: 
# x12 contains the base address of array in main
# x13 contains a copy of the length (passed by value)
# Post-conditions: x1 contains the return address
#
# This procedure swaps the values pointed to 
# by x12 and x13 in the Data Memory
##########################################
ARRAY_SUM:

add x21, x0, x0		# x21 is the sum
add x22, x0, x0		# x22 is i

BEGIN_LOOP:
beq x22, x13, END_LOOP
slli x6, x22, 2
add x7, x12, x6
lw x28, 0(x7)
add x21, x21, x28
addi x22, x22, 1
beq x0, x0, BEGIN_LOOP

# Jump and link back to main
END_LOOP:

# Return result
add x10, x21, x0

# Clear local variables and go back to main
add x28, x0, x0
add x7, x0, x0
add x6, x0, x0
add x22, x0, x0
add x21, x0, x0
jalr x0, x1, 0

# Terminate the program
END:
quit