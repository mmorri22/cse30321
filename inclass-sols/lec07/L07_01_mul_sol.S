# Given the mapping of registers to variables below, 
# write a program to implement the following expression:
# Z = (A+B) x (C-D)
#
# Values are:
# A=4, B=2, C=6, D=3
# Registers are A=x8, B=9, C=x18, D=x19, Z=x20
#
# You are permitted to use labels in this problem

addi x8, x8, 4
addi x9, x9, 2
addi x18, x18, 6
addi x19, x19, 3

# Write the Solution Here
add x5, x8, x9
sub x6, x18, x19

# No available mul instruction
# So we loop!
# Can only set the *final* solution to x20

add x7, x0, x0   # Iterator is in x7
add x28, x0, x0  # Multiplication Sum is x28

MUL_LOOP:
sub x29, x7, x6  # We stop when i - x6 = 0
beq x29, x0, PRINT_SUM  # Branch to print sum when done
add x28, x28, x5
addi x7, x7, 1
beq x28, x28, MUL_LOOP

PRINT_SUM:
add x20, x28, x0