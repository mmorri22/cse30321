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


# Call the function SWAP_FUNC and then clear x1


# Load the results back into the local registers 


# Free the function arguments for the function - now out of scope


# Clear remaining variables and Return 0


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


# int temp = *A;


# *A = *B;


# *B = temp;


# Clear temp registers in function call


# Jump and link back to main


# Terminate the program
END:
quit