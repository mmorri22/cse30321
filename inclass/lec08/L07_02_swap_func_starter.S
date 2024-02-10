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
# For simplicity, store A at 0x7fff1a10 for pass by reference
# For simplicity, store B at 0x7fff1a18 for pass by reference
#
# You are permitted to use labels in this problem

# Starter Code
MAIN:

addi x18, x18, 10
addi x19, x19, 17

# Write the Solution Here
# 1) Use the function argument registers to pass by value


# Call the function - SWAP_FUNC


# Load the results back into the local registers 


# Return 0


# Name the function call


# int temp = *A;


# *A = *B;


# *B = temp;


# Jump and link back to main


# Terminate the program
END:
quit