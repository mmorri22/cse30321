# Author: Prof. Matthew Morrison
# Email : matt.morrison@nd.edu
# File Name: sllist_step5 - Iterating to the end.S
#
# Architecture : RISC-V Assembly
# interpreter  : https://www.cs.cornell.edu/courses/cs3410/2019sp/riscv/interpreter
#
###################################################################################
# Part 5 - We will store the actual data element and then update the head pointer 
# The new changes and comments in this file occur in Lines 96-121 from sllist_step4
###################################################################################
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
#		else{
#			sll_node* curr_ptr = the_list->head_ptr;
#			while( curr_ptr->next_ptr != NULL ){
#				curr_ptr = curr_ptr->next_ptr;
#			}
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
sub x6, x5, x19       # x6 = 5 - x
blt x6, x0, END_FOR


# Step 7 - Set up the insertion loop
# 7.1 - Check if(the_list->head_node == NULL)
IF: 
lw x7, 0(x18)
bne x7, x0, ELSE

# 7.2 - Get the address of x18 + 12 bytes
addi x28, x18, 12
sw x0, 0(x28)
sw x0, 4(x28)
sw x0, 8(x28)


# 7.5 - Create the node itself
sw x19, 0(x28)   	# made_node->the_int = x;
sw x28, 0(x18)		# the_list->head_node = made_node;


# 7.3 - Clear local registersand branch to END_IF
add x28, x0, x0  # x28 goes out of scope before ELSE_IF

beq x0, x0, END_IF

ELSE:

######################################################
#### THE CHANGE FOR THE LIST ITERATOR STARTS HERE ####
######################################################

# Step 8 - Iterate through the list to find the next node location
# 8.1 - Get the location of the head nodr from head_ptr 
lw x28, 0(x18)	# sll_node* curr_ptr = the_list->head_node;

# 8.2 - Develop the while loop
WHILE:

lw x29, 4(x28)			# x29 = curr_ptr->next_node
beq x29, x0, END_WHILE	# Exit the while loop if curr_ptr->next_node == NULL

# 8.3 - These two instructions make up:
# curr_ptr = curr_ptr->next_node;
add x28, x29, x0		# Set x28 to x29
lw x29, 4(x28)			# Load the next 

beq x0, x0, WHILE

END_WHILE:

####################################################
#### THE CHANGE FOR THE LIST ITERATOR ENDS HERE ####
####################################################

# 7.4 - Clear x7, increment ++x, and branch back to BEGIN_FOR
END_IF:
add x7, x0, x0   # Clear x7 since it is about to go out of scope

addi x19, x19, 1      # ++i;
beq x0, x0, BEGIN_FOR # Go back to the beginning of the loop

END_FOR:
add x6, x0, x0
add x5, x0, x0


# Step 4 - Free the sllist struct main call
add x12, x18, x0    # Pointer to the_list is copied to x12
jal x1, FREE_SLLIST # free(the_list);
add x1, x0, x0     # FIX 2 - Empty x0 since we returned from the function call
add x12, x0, x0    # Empty x12
add x18, x0, x0     # x18 is no longer pointing to the memory


# Step 0 - Return 0
add x19, x0, x0    ######## <---- Reset i to 0
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