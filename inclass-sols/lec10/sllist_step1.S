# Author: Prof. Matthew Morrison
# Email : matt.morrison@nd.edu
# File Name: sllist_step1.S
#
# Architecture : RISC-V Assembly
# interpreter  : https://www.cs.cornell.edu/courses/cs3410/2019sp/riscv/interpreter
#
# Part 1 - Test to make sure you calloc and free the sllist struct
#
#####################################################################
# Modifications from sllist_step0.S:
#
# Step 1 - x18 points to address 0x051a6110
# Step 2 - Call the function calloc for the sllist struct
# Step 3 - Allocate the memory for the sllist struct
# Step 4 - Free the sllist struct main call
# Step 5 - Free the sllist Procedure
#####################################################################
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
add x1, x0, x0     ############# <------- FIX 1 - Empty x0 since we returned from the function call
add x12, x0, x0    # Empty x12 since it is out of scope


# Step 4 - Free the sllist struct main call
add x12, x18, x0    # Pointer to the_list is copied to x12
jal x1, FREE_SLLIST # free(the_list);
add x1, x0, x0     ############# <-------- FIX 2 - Empty x0 since we returned from the function call
add x12, x0, x0    # Empty x12


# Step 0 - Return 0
add x18, x0, x0     # x18 is no longer pointing to the memory
add x5, x0, x0     ############# <-------- FIX 3 - Set temp x5 to 0 to return 0;
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
sw x0, 4(x12)   # Clears bytes 4-7
sw x0, 8(x12)   # Clears bytes 8-11

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
sw x0, 4(x12)   # Clears bytes 4-7
sw x0, 8(x12)   # Clears bytes 8-11

# 5-2 Jump and link back to main
jalr x0, x1, 0

END:
quit