# Given the mapping of registers to variables below, 
# write a program to implement the following expression:
#
# int func(int A, int B, int C, int D){
#		return (A+B)*(C-D);
# }
#
# int main(){
# 		int A=4, B=2, C=6, D=3;
#		int z = func(A, B, C, D);
# 		return 0;
# }
#
# Registers in main are A=x8, B=9, C=x18, D=x19, Z=x20
#
# You are permitted to use labels in this problem

# Starter Code
MAIN:

addi x8, x8, 4
addi x9, x9, 2

# Write the Solution Here
# 1) Use the function argument registers to pass by value
add x12, x8, x0  # x12 is A passed by value
add x13, x9, x0  # x13 is B passed by value

# Call the function
jal x1, SUM_FUNC

# Store the result in the main function result
add x20, x10, x0

# Return 0
beq x0, x0, END

# Name the function call
SUM_FUNC:

# Add the passed by value copies
add x5, x12, x13

# # Put the result in one of the return registers
add x10, x5, x0

# Jump and link back to main
jalr x0, x1, 0

# Terminate the program
END:
quit