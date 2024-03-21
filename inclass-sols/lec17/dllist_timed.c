#include <stdio.h>
#include <time.h>
#include <stdlib.h>

typedef struct dll_node{
	int data;
	struct dll_node* prev_node;	
	struct dll_node* next_node;	
}dll_node;


typedef struct dllist{
	struct dll_node* head_node;
	struct dll_node* tail_node;
}dllist;




// Step 13 - Push Front 
void push_front( dllist* the_list, int the_value ){
	
	// Create a dll_node pointer called insert_node
	dll_node* insert_node = (dll_node*)malloc( sizeof(dll_node) );
	
	// Set the insert_node's data to the_value and next_node to NULL 
	insert_node->data = the_value;
	insert_node->prev_node = NULL;
	insert_node->next_node = NULL;
	
	// Dr. Morrison's Golden Rule of Pointers 
	if( the_list->head_node == NULL ){
		
		// Set the head node equal to insert_node 
		the_list->head_node = insert_node;
		the_list->tail_node = insert_node;
		
		return;
	}
	
	// Otherwise, we perform the pointer arithmetic
	dll_node* reference = the_list->head_node;
	
	// Set the head_node to the new node 
	the_list->head_node = insert_node;
	
	// Set the new head_node's next to the reference 
	the_list->head_node->next_node = reference;
	reference->prev_node = the_list->head_node;
	
}

// Step 13 - Push Front 
void push_back( dllist* the_list, int the_value ){
	
	// Create a dll_node pointer called insert_node
	dll_node* insert_node = (dll_node*)malloc( sizeof(dll_node) );
	
	// Set the insert_node's data to the_value and next_node to NULL 
	insert_node->data = the_value;
	insert_node->prev_node = NULL;
	insert_node->next_node = NULL;
	
	// Dr. Morrison's Golden Rule of Pointers 
	// Check if the list is empty
	if( the_list->tail_node == NULL ){
		
		// Set the head node equal to insert_node 
		the_list->head_node = insert_node;
		the_list->tail_node = insert_node;
		
		// And return
		return;
	}
	
	// 13-2 Now we just need to use a reference pointer and put them in front
	dll_node* reference = the_list->tail_node;
	
	// Set the head_node to the new node 
	the_list->tail_node = insert_node;
	
	// Set the new head_node's next to the reference 
	the_list->tail_node->prev_node = reference;
	reference->next_node = the_list->tail_node;
	
}


// Step 10 - Free all the elements 
void destructor( dll_node* curr_ptr ){
	
	// Dr. Morrison's Golden Rule of Pointers 
	if( curr_ptr == NULL )
		return;
	

	// Recursively call destructor on the next node  
	destructor( curr_ptr->next_node );
		
	// Free the current pointer 
	free( curr_ptr );
	
}


// Step 15 - Pop Front 
// Step 15 - Pop Front 
void pop_front( dllist* the_list ){
	
	// Check if the list is not empty
	if( the_list->head_node == NULL )
		return;
	
	else if( the_list->head_node == the_list->tail_node ){
		
		// free( the_list->head_node );
		
		dll_node* reference = the_list->head_node;
		
		the_list->head_node = NULL;
		the_list->tail_node = NULL;
		
		free( reference );
		
		return;
	}
	
	// Otherwise, move the node and free
	// Set a reference pointer to head_node
	dll_node* reference = the_list->head_node;
	
	// Set the head_node to head_node's next_node;
	the_list->head_node = reference->next_node;
	the_list->head_node->prev_node = NULL;

	
	// Free the reference 
	free( reference );
	
}


// Step 15 - Pop Front 
void pop_back( dllist* the_list ){
	
	// Check if the list is not empty
	if( the_list->head_node == NULL )
		return;
	
	else if( the_list->head_node == the_list->tail_node ){
		
		free( the_list->head_node );
		
		the_list->head_node = NULL;
		the_list->tail_node = NULL;
		
		return;
	}
	
	// Otherwise, move the node and free
	// Set a reference pointer to head_node
	dll_node* reference = the_list->tail_node;
	
	// Set the head_node to head_node's next_node;
	the_list->tail_node = reference->prev_node;
	the_list->tail_node->next_node = NULL;

	
	// Free the reference 
	free( reference );
	
}

void delete_node( dllist* the_list, int delete_num ){

	if( the_list->head_node == NULL || the_list->tail_node == NULL )
		return;

	if( the_list->head_node != NULL && the_list->head_node->data == delete_num )
		pop_front( the_list );

	else if( the_list->tail_node != NULL && the_list->tail_node->data == delete_num )
		pop_back( the_list );

	else{
		dll_node* curr_ptr = the_list->head_node;

		while( curr_ptr != NULL && curr_ptr->data != delete_num ){
			curr_ptr = curr_ptr->next_node;
		}

		if( curr_ptr != NULL ){
			curr_ptr->prev_node->next_node = curr_ptr->next_node;
			curr_ptr->next_node->prev_node = curr_ptr->prev_node;

			free( curr_ptr );
		}
	}

}


int main( const int argc, const char* argv[] ){

	if( argc != 3 ){
		fprintf(stdout, "Error: ./dllist_timed [num_items] [num_tests]");
		return EXIT_FAILURE;
	}

	int num_items = atoi(argv[1]);
	int num_tests = atoi(argv[2]);

	srand(time(0));

	dllist* the_list = (dllist *)malloc( sizeof( dllist ) );
	
	the_list->head_node = NULL;
	the_list->tail_node = NULL;
	
	
	// Call push_front with as many as we want to insert
	clock_t start_inserts = clock();
	int iter;
	for( iter = 0; iter < num_items; ++iter ){
		
		int the_value = rand() % num_items;
		
		push_back( the_list, the_value );
		
	}

    clock_t end_inserts = clock();
    
    double total_inserts = (double)(end_inserts - start_inserts) / (double)(CLOCKS_PER_SEC);

	clock_t start_tests = clock();

	int loop_tests = 0;
	for(loop_tests = 0; loop_tests < 100; ++loop_tests){

		int curr_test = 0;
		while( curr_test < num_tests ){

			int delete_num = rand() % num_items;

			delete_node( the_list, delete_num );

			int insert_num  = rand() % num_items;
			push_back( the_list, insert_num );

			++curr_test;
		}

	}

    clock_t end_tests = clock();
    
    double total_tests = (double)(end_tests - start_tests) / (double)(CLOCKS_PER_SEC * loop_tests);
    
    fprintf( stdout, "--------------------------------\n");
    fprintf( stdout, "Linked List Size       : %d\n", num_items);
	fprintf( stdout, "Clocks Per Second      : %ld\n", CLOCKS_PER_SEC );
	fprintf( stdout, "Clocks for all inserts : %ld\n", end_inserts - start_inserts);
	fprintf( stdout, "Average time per insert: %.6lf us\n", total_inserts / (double)num_tests * 1000000 );
	fprintf( stdout, "Number of tests        : %d\n", num_tests);
    fprintf( stdout, "Clocks for all tests   : %ld\n", end_tests - start_tests );
    fprintf( stdout, "Average time per tests : %.6lf us\n", total_tests / (double)num_tests * 1000000 );
    fprintf( stdout, "--------------------------------\n");

	// Call the destructor
	destructor( the_list->head_node );
	
	// Free the dllist 
	free( the_list );
	
	return EXIT_SUCCESS;
}