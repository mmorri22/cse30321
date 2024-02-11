# Author: Prof. Matthew Morrison
# Email : matt.morrison@nd.edu
# File Name: sllist_step0 - return 0.S
#
# Architecture : RISC-V Assembly
# interpreter  : https://www.cs.cornell.edu/courses/cs3410/2019sp/riscv/interpreter
#
# Part 0 - Test to make sure you can do the return 0
# This is the equivalent of:
#
# int main(){
#     return 0;
# }; 


MAIN:

# Step 0 - Return 0
beq x0, x0, END


END:
quit