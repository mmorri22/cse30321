# Author: Prof. Matthew Morrison
# Email : matt.morrison@nd.edu
# File Name: dllist_final.S - Individual deletion
#
# Architecture : RISC-V Assembly
# interpreter  : https://www.cs.cornell.edu/courses/cs3410/2019sp/riscv/interpreter
#
#
# This is the equivalent of:
#
# #include <stdlib.h>
# 
# typedef struct dll_node{
#     int the_int;
#     struct dll_node* prev_node;
#     struct dll_node* next_node;
# }dll_node;
# 
# typedef struct dllist{
#    struct dll_node* head_ptr;
#    struct dll_node* tail_ptr;
# }dllist
#
#
#   void delete_node( dllist* the_list, delete_val){
#    
#       dll_node* curr_ptr = the_list->head_node;
#   
#       while( curr_ptr != NULL ){
#        
#           if( curr_node->the_int == delete_val ){
#           
#               if( the_list->head_node == the_list->tail_node ){
#                   the_list->head_node = NULL;
#                   the_list->tail_node = NULL;
#               }
#               else if( curr_ptr == the_list->head_node ){
#                   the_list->head_node = curr_ptr->next_node;
#                   the_list->head_node->prev_node = NULL;
#               }
#               else if( curr_ptr == the_list->tail_node ){
#                   the_list->tail_node = curr_ptr->prev_node;
#                   the_list->tail_node->next_node = NULL;
#               }
#               else{
#                   curr_ptr->prev_node->next_node = curr_ptr->next_node;
#                   curr_ptr->next_node->prev_node = curr_ptr->prev_node;
#               }
#               
#               free( curr_ptr );
#				return;
#           }
#			curr_ptr = curr_ptr->next_ptr;
#       }
# }
#	
# int main(){
#	dllist* the_list = ( dllist* )calloc( 1, sizeof(dllist) );
#
#   for(int x = 0; x <= 5; ++x){
#		if(the_list->head_ptr == NULL){
# 			dll_node* made_node = ( dll_node* )calloc( 1, sizeof(dll_node) );
#			made_node->value = x;
#			the_list->head_ptr = made_node;
#			the_list->tail_ptr = made_node; 
#		}
#		else{
#			sll_node* curr_ptr = the_list->head_ptr;
#			while( curr_ptr->next_ptr != NULL ){
#				curr_ptr = curr_ptr->next_ptr;
#			}
# 			dll_node* made_node = ( dll_node* )calloc( 1, sizeof(dll_node) );
#			made_node->value = x;
#			curr_ptr->next_ptr = made_node; 
#           made_node->prev_ptr = curr_ptr; 
#			the_list->tail_ptr = made_node; 
#		}
#	}
#
#   /***********************************/
#   /**** Delete an individual node ****/
#   /***********************************/
#   int delete_val = 3;   // test by changing the value to 0, 2, and -1
#   delete_node( the_list, delete_val);
#
#   dll_node* curr_ptr = the_list->head_ptr;
#   dll_node* next_ptr = curr_ptr->next_ptr;
#   while( curr_ptr != NULL ){
#       free(curr_ptr);
#       curr_ptr = next_ptr;
#       next_ptr = curr_ptr->next_ptr;
#   }
#
#	free(the_list);
#	return 0;
# }



MAIN:

# Step 1 - x18 points to address 0x051a6110
lui x5, 0x7ffff
addi x18, x5, 0x620
add x5, x0, x0

# Step 2 - Call the function calloc for the sllist struct
# 2-1 - Must pass a *copy* of the pointer to the function. Use Function arguments (leave a0, a1)
add x12, x18, x0
jal x1, CALLOC_DLLIST 
add x1, x0, x0     # FIX 1 - Empty x0 since we returned from the function call
add x12, x0, x0    # Empty x12 since it is out of scope


# Step 6 - Setting up the first main loop
addi x19, x0, 3   # y = 3

BEGIN_FOR: 
blt x19, x0, END_FOR

# Step 7 - Set up the looop
# 7.1 - Check if(the_list->head_node == NULL)
IF: 
lw x7, 0(x18)
bne x7, x0, ELSE

# 7.2 - Get the address of x18 + 16 bytes
addi x28, x18, 0x10	# Students may still have this as 12 or 0xc
sw x0, 0(x28)
sw x0, 4(x28)
sw x0, 8(x28)
sw x0, 12(x28)		# Must clear for credit for segmentation

# 7.5 - Create the node itself
sw x19, 0(x28)   	# made_node->the_int = x;
sw x28, 0(x18)		# the_list->head_node = made_node;
sw x28, 4(x18)		# the_list->tail_node = made_node;


# 7.3 - Clear local registersand branch to END_IF
add x28, x0, x0  # x28 goes out of scope before ELSE_IF
beq x0, x0, END_IF

# We will add ELSE here, but nothing else before step 7.4
ELSE:

# Step 8 - Iterate through the list to find the next node location
# 8.1 - Get the location of the head nodr from head_ptr 
lw x28, 0(x18)	# sll_node* curr_ptr = the_list->head_node;

# 8.2 - Develop the while loop
WHILE:

lw x29, 8(x28)			# x29 = curr_ptr->next_node
beq x29, x0, END_WHILE	# Exit the while loop if curr_ptr->next_node == NULL

# 8.3 - These two instructions make up:
# curr_ptr = curr_ptr->next_node;
add x28, x29, x0		# Set x28 to x29
lw x29, 8(x28)			# Load the next node (This will need to be updated from 4 to 8)

beq x0, x0, WHILE

END_WHILE:

# 9.1 - dll_node* made_node = ( dll_node* )calloc( 1, sizeof(dll_node) );
addi x29, x28, 0x10		# Students may be still adding 12 instead of 16 (if they have 0xc)
sw x0, 0(x29)
sw x0, 4(x29)
sw x0, 8(x29)
sw x0, 12(x29)

# 9.2 - made_node->the_int = x;
sw x19, 0(x29)

# 9.3 - curr_ptr->next_node = made_node;
sw x29, 8(x28)

# 9.4 - made_node->prev_ptr = curr_ptr;
sw x28, 4(x29)

# 9.5 - the_list->tail_ptr = made_node; 
sw x29, 4(x18)

# 9.6 - Clear x29 and x28
add x29, x0, x0
add x28, x0, x0

# 7.4 - Clear x7, decrement --y, and branch back to BEGIN_FOR
END_IF:
add x7, x0, x0   # Clear x7 since it is about to go out of scope

addi x19, x19, -1      # --y;
beq x0, x0, BEGIN_FOR # Go back to the beginning of the loop

END_FOR:
add x6, x0, x0
add x5, x0, x0


##########################################
#
# Changes from dllist_step4.S in main start here
#
##########################################

addi x20, x0, 2   	# This is the int delete_val = 3; MUST BE DONE! Cannot put in function argument only

# Step 11.1 - Set up the function arguments
add x12, x18, x0
add x13, x20, x0
jal x1, DELETE_NODE
add x1, x0, x0
add x13, x0, x0
add x12, x0, x0

##########################################
#
# Changes from dllist_step4.S in main end here
#
##########################################


# Step 10 - Free the Nodes at the end of main
# 10.1 - Set up the curr_ptr and next_ptr

lw x7, 0(x18)	# dll_node* curr_ptr = the_list->head_ptr;
lw x28, 8(x7)	# dll_node* next_ptr = curr_ptr->next_ptr;


# 10.2-1 - Set up the FREE_NODE_LOOP
FREE_NODE_LOOP:

beq x7, x0, END_FREE_NODE_LOOP  # while( curr_ptr != NULL ) - Branch if curr_ptr == NULL

# 10.3 - Free the current pointer - free(curr_ptr)
sw x0, 0(x7)
sw x0, 4(x7)
sw x0, 8(x7)
sw x0, 12(x7)


# 10.4 - Update the pointers in the loop 
add x7, x28, x0		# curr_ptr = next_ptr;
lw x28, 8(x7) 		# next_ptr = curr_ptr->next_ptr;


# 10.2-3 - End the FREE_NODE_LOOP
beq x0, x0, FREE_NODE_LOOP

# 10.2-3 - End the FREE_NODE_LOOP
END_FREE_NODE_LOOP:


# Step 4 - Free the dllist struct main call
add x12, x18, x0    # Pointer to the_list is copied to x12
jal x1, FREE_DLLIST # free(the_list);
add x1, x0, x0      # Empty x0 since we returned from the function call
add x12, x0, x0     # Empty x12
add x18, x0, x0     # x18 is no longer pointing to the memory


# Step 0 - Return 0
add x20, x0, x0		# Set the delete_node in main to 0 <---- Will need to update for full credit
add x19, x0, x0    # Reset i to 0
add x6, x0, x0     # Reset x6 to 0
add x5, x0, x0     # Set temp x5 to 0 to return 0;
beq x0, x0, END


# Step 3 - Allocate the memory for the sllist struct
##########################################
# Procedure Name: CALLOC_DLLIST
# Pre-conditions: x12 contains the base address of an sll_node
# Post-conditions: x1 contains the return address of the calling procedure
#
# This procedure clears 128 bits (16 bytes) of memory 
# to be allocated to a dll_node
##########################################
CALLOC_DLLIST:

# 3-1 - calloc overwrites the memory at that location with 0
# Note - Problem says every 96 bits must be cleared, which is 12 bytes
sw x0, 0(x12)   # Clears bytes 0-3
sw x0, 4(x12)   # Clears bytes 4-6
sw x0, 8(x12)   # Clears bytes 7-9
sw x0, 12(x12)   # Clears bytes 10-13

# 3-2 Jump and link back to main
jalr x0, x1, 0



# Step 5 - Free the sllist Procedure
##########################################
# Procedure Name: FREE_DLLIST
# Pre-conditions: x12 contains the base address of an sll_node
# Post-conditions: 
#
# This procedure clears 128 bits (16 bytes) of memory 
# previously allocated to a sll_node
##########################################
FREE_DLLIST:

# 5-1 Must clear the memory pointed to by x12
sw x0, 0(x12)   # Clears bytes 0-3
sw x0, 4(x12)   # Clears bytes 4-7
sw x0, 8(x12)   # Clears bytes 9-11
sw x0, 12(x12)   # Clears bytes 12-15

# 5-2 Jump and link back to main
jalr x0, x1, 0



# Step 12 - Delete Node 
##########################################
# Procedure Name: FREE_DLLIST
# Pre-conditions: x12 contains the dllist* pointer 
# x13 contains the value sought to delete 
#
# Post-conditions: 
# x1 contains the jalr retrun adress
#
# This procedure clears 128 bits (16 bytes) of memory 
# previously allocated to a sll_node
##########################################

DELETE_NODE:

lw x28, 0(x12)		# dll_node* curr_ptr = the_list->head_node;

# while( curr_ptr != NULL )
DELETE_WHILE:
beq x28, x0, DELETE_END_WHILE

# if( curr_node->the_int == delete_val )
DELETE_OUTER_IF:

lw x29, 0(x28)				# x29 = curr_node->the_int
bne x29, x13, DELETE_END_IF	# Branch if curr_node->the_int != delete_val
add x29, x0, x0				# curr_node->the_int goes out of scope
         
#               if( the_list->head_node == the_list->tail_node )
DELETE_INNER_IF:
lw x30, 0(x12)		# x30 = the_list->head_node
lw x31, 4(x12)		# x31 = the_list->tail_node
bne x30, x31, DELETE_ELSE_IF_1

sw x0, 0(x12)	# the_list->head_node = NULL;
sw x0, 4(x12)	# the_list->tail_node = NULL;

#               }
beq x0, x0, DELETE_END_INNER_IF


# else if( curr_ptr == the_list->head_node ){
DELETE_ELSE_IF_1:
bne x28, x30, DELETE_ELSE_IF_2	# Branch if curr_ptr != the_list->head_node

# the_list->head_node = curr_ptr->next_node;
lw x5, 8(x28)	# x5 = curr_ptr->next_node
sw x5, 0(x12)	# the_list->head_node (0(x12)) = x5
add x5, x0, x0	# Reset x5 to 0

# the_list->head_node->prev_node = NULL;
lw x5, 0(x12)	# x5 = the_list->head_node
addi x5, x5, 4	# x5 = the_list->head_node->prev_node
sw x0, 0(x5)	# the_list->head_node->prev_node = NULL

# }
add x31, x0, x0
add x30, x0, x0
add x5, x0, x0	# Reset x5 to 0
beq x0, x0, DELETE_END_INNER_IF


# else if( curr_ptr == the_list->tail_node ){
DELETE_ELSE_IF_2:
lw x5, 4(x12)   # x5 = the_list->tail_node
bne x28, x5, DELETE_ELSE

# the_list->tail_node = curr_ptr->prev_node;
lw x5, 4(x28)	# x5 = curr_ptr->prev_node
sw x5, 4(x12)	# the_list->tail_node (4(x12)) = curr_ptr->prev_node
add x5, x0, x0	# Reset x5 to 0

# the_list->tail_node->next_node = NULL;
lw x5, 4(x12)	# x5 = the_list->tail_node
addi x5, x5, 8	# x5 = the_list->tail_node->next_node
sw x0, 0(x5)	# the_list->tail_node->next_node = NULL

#               }
add x5, x0, x0	# Reset x5 to 0
beq x0, x0, DELETE_END_INNER_IF

DELETE_ELSE:

# curr_ptr->prev_node->next_node = curr_ptr->next_node;
lw x5, 8(x28)	# x5 = curr_ptr->next_node
lw x6, 4(x28)	# x6 = curr_ptr->prev_node
addi x6, x6, 8	# x6 = curr_ptr->prev_node->next_node
sw x5, 0(x6)	# curr_ptr->prev_node->next_node = curr_ptr->next_node
add x5, x0, x0
add x6, x0, x0

# curr_ptr->next_node->prev_node = curr_ptr->prev_node;
lw x5, 4(x28)	# x5 = curr_ptr->prev_node
lw x6, 8(x28)	# x6 = curr_ptr->next_node
addi x6, x6, 4	# x6 = curr_ptr->next_node->prev_node
sw x5, 0(x6)	# curr_ptr->prev_node->next_node = curr_ptr->next_node
add x5, x0, x0
add x6, x0, x0

DELETE_END_INNER_IF:            
#  free( curr_ptr );
sw x0, 0(x28)
sw x0, 4(x28)
sw x0, 8(x28)
sw x0, 12(x28)

add x28, x0, x0		# x28 has gone out of scope
jalr x0, x1, 0		# Go back to main

DELETE_END_IF:

# curr_ptr = curr_ptr->next_ptr;
lw x28, 8(x28)

# Branch back to while
beq x0, x0, DELETE_WHILE

DELETE_END_WHILE:

# 12-X Jump and link back to main
add x31, x0, x0
add x30, x0, x0
add x28, x0, x0		# x28 has gone out of scope
jalr x0, x1, 0		# Go back to main

END:
quit