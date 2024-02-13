# Given the mapping of registers to variables below, 
# write a program to implement the following expression:
#
# int sum(int A, int B){
#		return A+B;
# }
#
# int main(){
# 		int A=4, B=2;
#		int z = sum(A, B);
# 		return 0;
# }
#
# Registers in main are A=x8, B=9
#
# You are permitted to use labels in this problem
#
# Ensure all garbage is properly collected at the end of the program.

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
add x1, x0, x0
add x12, x0, x0
add x13, x0, x0

# Store the result in the main function result
add x20, x10, x0
add x10, x0, x0 # FIX - Clear x10. No longer needed

# Return 0
add x20, x0, x0 # Clear in reverse order (compiler call stack)
add x9, x0, x0
add x8, x0, x0
beq x0, x0, END

# Name the function call and write the procedure header
##########################################
# Procedure Name: SUM_FUNC
# Pre-conditions: x12 contains A, x13 contains B
# Post-conditions: x10 contains the sum, x1 contains the return address
#
# This procedure sums x12 and x13 and returns in x10
##########################################
SUM_FUNC:

# Add the passed by value copies
add x5, x12, x13

# # Put the result in one of the return registers
add x10, x5, x0

# Jump and link back to main
add x5, x0, x0 	# FIX - Clear the memory
jalr x0, x1, 0

# Terminate the program
END:
quit