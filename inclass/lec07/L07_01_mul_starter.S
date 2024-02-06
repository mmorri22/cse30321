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