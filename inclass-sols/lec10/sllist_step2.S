# Author: Prof. Matthew Morrison
# Email : matt.morrison@nd.edu
# File Name: sllist_step2 - insertion for loop example.S
#
# Architecture : RISC-V Assembly
# interpreter  : https://www.cs.cornell.edu/courses/cs3410/2019sp/riscv/interpreter
#
########################################################################################
# Part 2 - In this portion, the loop is set up for the sllist insertions
# We check at this stage to ensure we are properly freeing and 0-ing out all registers
#
# This file contains a fix of sllist_step1 - first calloc and free - fix.S 
# Primary changes occur on lines 49-69
# Another change at Line 82 to ensure registers are cleared
########################################################################################
#
# This is the equivalent of:
#
# #include <stdlib.h>
#
# typedef struct sllist{
#	struct sll_node* head_ptr;
# }sllist;
#
# int main(){
#	sllist* the_list = ( sllist* )calloc( 1, sizeof(sllist) );
#
#   for(int i = 0; i <= 5; ++i){
#		// Do nothing
#	}
# 	
#	free(the_list);
#	return 0;
# }



MAIN:

# Step 1 - x18 points to address 0x051a6110
lui x5, 0x051a6
addi x18, x5, 0x110

# Step 2 - Call the function calloc for the sllist struct
# 2-1 - Must pass a *copy* of the pointer to the function. Use Function arguments (leave a0, a1)
add x12, x18, x0
jal x1, CALLOC_SLLIST 
add x1, x0, x0     # FIX 1 - Empty x0 since we returned from the function call
add x12, x0, x0    # Empty x12 since it is out of scope

#############################################
#### THE CHANGE FOR THE LOOP STARTS HERE ####
#############################################

# Step 6 - Setting up the first main loop
addi x19, x0, 1   # i = 1
addi x5, x0, 5    # Reuse x5 = 5

BEGIN_FOR: 
sub x6, x5, x19 
blt x6, x0, END_FOR

addi x19, x19, 1      # ++i;
beq x0, x0, BEGIN_FOR # Go back to the beginning of the loop

END_FOR:

###########################################
#### THE CHANGE FOR THE LOOP ENDS HERE ####
#### Check the return 0 comment as well####
###########################################

# Step 4 - Free the sllist struct main call
add x12, x18, x0    # Pointer to the_list is copied to x12
jal x1, FREE_SLLIST # free(the_list);
add x1, x0, x0     # FIX 2 - Empty x0 since we returned from the function call
add x12, x0, x0    # Empty x12
add x18, x0, x0     # x18 is no longer pointing to the memory


# Step 0 - Return 0
add x19, x0, x0    ######## <---- Reset i to 0
add x6, x0, x0     ######## <---- Reset x6 to 0
add x5, x0, x0     # FIX 3 - Set temp x5 to 0 to return 0;
beq x0, x0, END


# Step 3 - Allocate the memory for the sllist struct
##########################################
# Procedure Name: CALLOC_SLLIST
# Pre-conditions: x12 contains the base address of an sll_node
# Post-conditions: x1 contains the return address of the calling procedure
#
# This procedure clears 96 bits (12 bytes) of memory 
# to be allocated to a sll_node
##########################################
CALLOC_SLLIST:

# 3-1 - calloc overwrites the memory at that location with 0
# Note - Problem says every 96 bits must be cleared, which is 12 bytes
sw x0, 0(x12)   # Clears bytes 0-3
sw x0, 4(x12)   # Clears bytes 4-6
sw x0, 8(x12)   # Clears bytes 7-9

# 3-2 Jump and link back to main
jalr x0, x1, 0



# Step 5 - Free the sllist Procedure
##########################################
# Procedure Name: FREE_SLLIST
# Pre-conditions: x12 contains the base address of an sll_node
# Post-conditions: 
#
# This procedure clears 96 bits (12 bytes) of memory 
# previously allocated to a sll_node
##########################################
FREE_SLLIST:

# 5-1 Must clear the memory pointed to by x12
sw x0, 0(x12)   # Clears bytes 0-3
sw x0, 4(x12)   # Clears bytes 4-6
sw x0, 8(x12)   # Clears bytes 7-9

# 5-2 Jump and link back to main
jalr x0, x1, 0

END:
quit