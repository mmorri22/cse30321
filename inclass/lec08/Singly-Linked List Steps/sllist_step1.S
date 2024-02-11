# Author: Prof. Matthew Morrison
# Email : matt.morrison@nd.edu
# File Name: sllist_step1 - first calloc and free - fix.S
#
# Architecture : RISC-V Assembly
# interpreter  : https://www.cs.cornell.edu/courses/cs3410/2019sp/riscv/interpreter
#
# Part 1 - Test to make sure you calloc and free the sllist struct
#
#####################################################################
# Modifications from sllist_step0 - return 0.S:
#
# Step 1 - Line 37 - x18 points to address 0x051a6110
# Step 2 - Line 41 - Call the function calloc for the sllist struct
# Step 3 - Line 58 - Allocate the memory for the sllist struct
# Step 4 - Line 48 - Free the sllist struct main call
# Step 5 - Line 73 - Free the sllist Procedure
#####################################################################
#
# This is the equivalent of:
#
#typedef struct sllist{
#	struct sll_node* head_ptr;
#}sllist;
#
#int main(){
#	sllist* the_list = ( sllist* )calloc( 1, sizeof(sllist) );
#	
#	free(the_list);
#	return 0;
#}



MAIN:

# Step 1 - x18 points to address 0x051a6110
lui x5, 0x051a6
addi x18, x5, 0x110

# Step 2 - Call the function calloc for the sllist struct
# 2-1 - Must pass a *copy* of the pointer to the function. Use Function arguments (leave a0, a1)
add x12, x18, x0
jal x1, CALLOC_SLLIST
add x12, x0, x0    # Empty x12 since it is out of scope


# Step 4 - Free the sllist struct main call
add x12, x18, x0    # Pointer to the_list is copied to x12
jal x1, FREE_SLLIST # free(the_list);
add x12, x0, x0    # Empty x12
add x18, x0, x0     # x18 is no longer pointing to the memory

# Step 0 - Return 0
beq x0, x0, END


# Step 3 - Allocate the memory for the sllist struct
# Note: Input is in x12 from MAIN
CALLOC_SLLIST:

# 3-1 - calloc overwrites the memory at that location with 0
# Note - Problem says every 96 bits must be cleared, which is 12 bytes
sw x0, 0(x12)   # Clears bytes 0-3
sw x0, 4(x12)   # Clears bytes 4-6
sw x0, 8(x12)   # Clears bytes 7-9

# 3-2 Jump and link back to main
jalr x0, x1, 0



# Step 5 - Free the sllist Procedure
FREE_SLLIST:

# 5-1 Must clear the memory pointed to by x12
sw x0, 0(x12)   # Clears bytes 0-3
sw x0, 4(x12)   # Clears bytes 4-6
sw x0, 8(x12)   # Clears bytes 7-9

# 5-2 Jump and link back to main
jalr x0, x1, 0

END:
quit