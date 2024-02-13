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


# Step 2 - Call the function calloc for the sllist struct
# 2-1 - Must pass a *copy* of the pointer to the function. Use Function arguments (leave a0, a1)



# Step 4 - Free the sllist struct main call


# Step 0 - Return 0
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


# 3-1 - calloc overwrites the memory at that location with 0
# Note - Problem says every 96 bits must be cleared, which is 12 bytes


# 3-2 Jump and link back to main




# Step 5 - Free the sllist Procedure
##########################################
# Procedure Name: FREE_SLLIST
# Pre-conditions: x12 contains the base address of an sll_node
# Post-conditions: 
#
# This procedure clears 96 bits (12 bytes) of memory 
# previously allocated to a sll_node
##########################################


# 5-1 Must clear the memory pointed to by x12


# 5-2 Jump and link back to main


END:
quit