#include <stdio.h>
#include <stdlib.h>

typedef struct dll_node{
    int the_int;
    struct dll_node* prev_node;
    struct dll_node* next_node;
}dll_node;

typedef struct dllist{
    struct dll_node* head_ptr;
    struct dll_node* tail_ptr;
}dllist;

void print_list( dllist* the_list ){
	
    dll_node* curr_ptr = the_list->head_ptr;

    while( curr_ptr != NULL ){

		fprintf(stdout, "Node Base Address: %p\n", curr_ptr);
		fprintf(stdout, "The int (addr, val): %p, %d\n", &curr_ptr->the_int, curr_ptr->the_int);
		fprintf(stdout, "prev_node (addr, val): %p, %p\n", &curr_ptr->prev_node, curr_ptr->prev_node);
		fprintf(stdout, "next_node (addr, val): %p, %p\n\n", &curr_ptr->next_node, curr_ptr->next_node);
		
		curr_ptr = curr_ptr->next_node;
	}	

	fprintf(stdout, "---------------------------------------------\n");
	
}

void delete_node( dllist* the_list, int delete_val){

    dll_node* curr_ptr = the_list->head_ptr;

    while( curr_ptr != NULL ){
    
        if( curr_ptr->the_int == delete_val ){
        
            if( the_list->head_ptr == the_list->tail_ptr ){
                the_list->head_ptr = NULL;
                the_list->tail_ptr = NULL;
            }
            else if( curr_ptr == the_list->head_ptr ){
                the_list->head_ptr = curr_ptr->next_node;
                the_list->head_ptr->prev_node = NULL;
            }
            else if( curr_ptr == the_list->tail_ptr ){
                the_list->tail_ptr = curr_ptr->prev_node;
                the_list->tail_ptr->next_node = NULL;
            }
            else{
                curr_ptr->prev_node->next_node = curr_ptr->next_node;
                curr_ptr->next_node->prev_node = curr_ptr->prev_node;
            }
            
            free( curr_ptr );
        }
        
        curr_ptr = curr_ptr->next_node;
    }
    
}

int main(){
    
    dllist* the_list = ( dllist* )calloc( 1, sizeof(dllist) );
    
    // Added
    fprintf(stdout, "Register - the_list: %p\n", &the_list);
    fprintf(stdout, "DM - the_list      : %p\n", &the_list->head_ptr);
    fprintf(stdout, "DM - the_list head : %p\n", &the_list->tail_ptr);
    fprintf(stdout, "--------------------------------------------\n");

    for(int y = 3; y >= 0; --y){
        if(the_list->head_ptr == NULL){
            dll_node* made_node = ( dll_node* )calloc( 1, sizeof(dll_node) );
            made_node->the_int = y;
            the_list->head_ptr = made_node; 
            the_list->tail_ptr = made_node; 
        }
        else{
            dll_node* curr_ptr = the_list->head_ptr;
            while( curr_ptr->next_node != NULL ){
                curr_ptr = curr_ptr->next_node;
            }
            dll_node* made_node = ( dll_node* )calloc( 1, sizeof(dll_node) );
            made_node->the_int = y;
            curr_ptr->next_node = made_node;
            made_node->prev_node = curr_ptr;
            the_list->tail_ptr = made_node;
        }
    }
    
    /****** Added - Print the addresses **********/
	fprintf( stdout, "Before deletion:\n" );
	print_list( the_list );
    
    int delete_val = 2;
    delete_node( the_list, delete_val );
	
    /****** Added - Print the addresses **********/
	fprintf( stdout, "After deletion:\n" );
	print_list( the_list );

    dll_node* curr_ptr = the_list->head_ptr;
    dll_node* next_ptr = curr_ptr->next_node;
    while( curr_ptr != NULL ){
        free(curr_ptr);
        curr_ptr = next_ptr;
		
		if( curr_ptr != NULL ){
			next_ptr = curr_ptr->next_node;
		}
    }

    free(the_list);
    return 0;
}
