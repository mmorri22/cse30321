# Author: Prof. Matthew Morrison
# Email : matt.morrison@nd.edu
# File Name: sllist_step3 - insertion for loop allocation.S
#
# Architecture : RISC-V Assembly
# interpreter  : https://www.cs.cornell.edu/courses/cs3410/2019sp/riscv/interpreter
#
#######################################################################################
# Part 3 - In this portion, we are performing the task of inserting into an empty list
# Lines 69-100 contain the changes and comments from sllist_step2
# Note the ELSE set up at Line 87, which is empty now and will be addressed in future files
#######################################################################################
#
# This is the equivalent of:
#
# include <stdlib.h>
#
# typedef struct sllist{
#	struct sll_node* head_ptr;
# }sllist;
#
# typedef struct sll_node{
#	int value;
#	struct sll_node* next_ptr;
# }sll_node;
#
# int main(){
#	sllist* the_list = ( sllist* )calloc( 1, sizeof(sllist) );
#
#   for(int x = 0; x <= 5; ++x){
#		if(the_list->head_ptr == NULL){
# 			sll_node* made_node = ( sll_node* )calloc( 1, sizeof(sll_node) );
#			made_node->value = x;
#			the_list->head_ptr = made_node; 
#		}
#	}
# 	
#	free(the_list);
#	return 0;
# }



MAIN:

# Step 1 - x18 points to address 0x051a6110
lui x5, 0x051a6
addi x18, x5, 0x110
add x5, x0, x0

# Step 2 - Call the function calloc for the sllist struct
# 2-1 - Must pass a *copy* of the pointer to the function. Use Function arguments (leave a0, a1)
add x12, x18, x0
jal x1, CALLOC_SLLIST 
add x1, x0, x0     # FIX 1 - Empty x0 since we returned from the function call
add x12, x0, x0    # Empty x12 since it is out of scope


# Step 6 - Setting up the first main loop
addi x19, x0, 1   # x = 1
addi x5, x0, 5    # Reuse x5 = 5

BEGIN_FOR: 
sub x6, x5, x19 
blt x6, x0, END_FOR

####################################################
#### THE CHANGE FOR THE LIST INSERT STARTS HERE ####
####################################################

# Step 7 - Set up the looop
# 7.1 - Check if(the_list->head_node == NULL)
IF: 
lw x7, 0(x18)
bne x7, x0, ELSE

# 7.2 - Get the address of x18 + 12 bytes
addi x28, x18, 12
sw x0, 0(x28)
sw x0, 4(x28)
sw x0, 8(x28)


# 7.3 - Clear local registersand branch to END_IF
add x28, x0, x0  # x28 goes out of scope before ELSE_IF
beq x0, x0, END_IF

# We will add ELSE here, but nothing else before step 7.4
ELSE:

# Do nothing so far

# 7.4 - Clear x7, increment ++x, and branch back to BEGIN_FOR
END_IF:
add x7, x0, x0   # Clear x7 since it is about to go out of scope

addi x19, x19, 1      # ++x;
beq x0, x0, BEGIN_FOR # Go back to the beginning of the loop

END_FOR:
add x6, x0, x0
add x5, x0, x0

###########################################
#### THE CHANGE FOR THE LOOP ENDS HERE ####
#### Check the return 0 comment as well####
###########################################

# Step 4 - Free the sllist struct main call
add x12, x18, x0    # Pointer to the_list is copied to x12
jal x1, FREE_SLLIST # free(the_list);
add x1, x0, x0      # Empty x0 since we returned from the function call
add x12, x0, x0     # Empty x12
add x18, x0, x0     # x18 is no longer pointing to the memory


# Step 0 - Return 0
add x19, x0, x0    # Reset i to 0
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