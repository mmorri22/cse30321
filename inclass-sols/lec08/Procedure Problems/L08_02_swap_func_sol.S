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

addi x18, x0, 10
addi x19, x0, 17

# Write the Solution Here
# 1) Use the function argument registers to pass by value
lui x10, 0x7fff1
lui x11, 0x7fff1
addi x10, x10, 0xa10
addi x11, x11, 0xa18
sw x18, 0(x10)
sw x19, 0(x11)

# Call the function
jal x1, SWAP_FUNC

# Load the results back into the local registers 
lw x18, 0(x10)
lw x19, 0(x11)

# Return 0
beq x0, x0, END

# Name the function call
SWAP_FUNC:

# int temp = *A;
lw x5, 0(x10)

# *A = *B;
lw x6, 0(x11)
sw x6, 0(x10)

# *B = temp;
sw x5, 0(x11)

# Jump and link back to main
jalr x0, x1, 0

# Terminate the program
END:
quit