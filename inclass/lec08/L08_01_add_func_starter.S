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

MAIN:

addi x8, x0, 4
addi x9, x0, 2

# Write the Solution Here
# 1) Use the function argument registers to pass by value


# Call the function


# Store the result in the main function result


# Return 0


# Name the function call and write the procedure header


# Add the passed by value copies


# Put the result in one of the return registers


# Jump and link back to main


# Terminate the program