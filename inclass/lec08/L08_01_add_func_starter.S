# Given the mapping of registers to variables below, 
# write a program to implement the following expression:
#
# int func(int A, int B, int C, int D){
#		return (A+B)*(C-D);
# }
#
# int main(){
# 		int A=4, B=2;
#		int z = sum(A, B, C, D);
# 		return 0;
# }
#
# Registers in main are A=x8, B=9, C=x18, D=x19, Z=x20
#
# You are permitted to use labels in this problem

MAIN:

addi x8, x0, 4
addi x9, x0, 2

# Write the Solution Here
# 1) Use the function argument registers to pass by value


# Call the function


# Store the result in the main function result


# Return 0


# Name the function call


# Add the passed by value copies


# Put the result in one of the return registers


# Jump and link back to main


# Terminate the program