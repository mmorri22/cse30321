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

MAIN:

addi x8, x8, 4
addi x9, x9, 2
addi x18, x18, 6
addi x19, x19, 3

# Write the Solution Here
# 1) Use the function argument registers to pass by value


# Call the function


# Store the result in the main function result


# Return 0


# Name the function call


# Add the passed by value copies


# When we set it up correctly, we can use the exact same code!
add x7, x0, x0   # Iterator is in x7
add x28, x0, x0  # Multiplication Sum is x28

MUL_LOOP:
sub x29, x7, x6  # We stop when i - x6 = 0
beq x29, x0, PRINT_SUM  # Branch to print sum when done
add x28, x28, x5
addi x7, x7, 1
beq x28, x28, MUL_LOOP

# Put the result in one of the return registers
PRINT_SUM:


# Jump and link back to main


# Terminate the program