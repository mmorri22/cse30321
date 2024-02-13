# Given the mapping of registers to variables below, 
# write a program to implement the following expression:
#
# void swap(int* A, int* B){
#		int temp = *A;
#		*A = *B;
#		*B = temp;
# }
#
# int main(){
# 		int A=10, B=7;
#		swap(&A, &B);
# 		return 0;
# }
#
# Registers in main are A=x18, B=19
# For simplicity, store A at 0x7fff1310 for pass by reference
# For simplicity, store B at 0x7fff1318 for pass by reference
#
# You are permitted to use labels in this problem
#
# Ensure all garbage is properly collected at the end of the program.

# Starter Code
MAIN:

addi x18, x0, 10
addi x19, x0, 17

# Write the Solution Here
# 1) Use the function argument registers to pass by value
lui x5, 0x7fff1
addi x12, x5, 0x310
addi x13, x5, 0x318
sw x18, 0(x12)
sw x19, 0(x13)

# Call the function SWAP_FUNC and then clear x1
jal x1, SWAP_FUNC
add x1, x0, x0

# Load the results back into the local registers 
lw x18, 0(x12)
lw x19, 0(x13)

# Free the function arguments for the function - now out of scope
add x13, x0, x0
add x12, x0, x0

# Clear remaining variables and Return 0
add x13, x0, x0
add x12, x0, x0
add x19, x0, x0
add x18, x0, x0 
beq x0, x0, END

# Name the function call
##########################################
# Procedure Name: SWAP_FUNC
# Pre-conditions: 
# x12 contains &A from MAIN
# x13 contains &B from MAIN
# Post-conditions: x1 contains the return address
#
# This procedure swaps the values pointed to 
# by x12 and x13 in the Data Memory
##########################################
SWAP_FUNC:

# int temp = *A;
lw x5, 0(x12)

# *A = *B;
lw x6, 0(x13)
sw x6, 0(x12)

# *B = temp;
sw x5, 0(x13)

# Clear temp registers in function call
add x6, x0, x0
add x5, x0, x0

# Jump and link back to main
jalr x0, x1, 0

# Terminate the program
END:
quit