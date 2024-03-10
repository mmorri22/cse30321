#include <iostream>
#include <cstdlib>
#include <set>

#define COUT std::cout
#define ENDL std::endl
#define CERR std::cerr

int main( const int argc, const char* argv[] ){
    
	int num_items = atoi(argv[1]);
	int num_tests = atoi(argv[2]);
	
	/* Call the STL Red-Black Tree */
	std::set<int> rbt_set;
    
    if( argc != 3 ){
        
		CERR << "Error: ./rbtree_timed [num_items] [num_tests]" << ENDL;
		
		return EXIT_FAILURE;
    }
    
    srand(time(0));
    
	// Call push_front with as many as we want to insert
	int iter;
	for( iter = 0; iter < num_items; ++iter ){
		
		int the_value = rand() % num_items;
		
		rbt_set.insert( the_value );
		
	}

	clock_t start_tests = clock();

	int loop_tests = 0;
	for(loop_tests = 0; loop_tests < 1000; ++loop_tests){

		int curr_test = 0;
		while( curr_test < num_tests ){

			int delete_num = rand() % num_items;
			
			rbt_set.erase( delete_num );

			int insert_num  = rand() % num_items;
			
			rbt_set.insert( insert_num );

			++curr_test;
		}

	}

    clock_t end_tests = clock();
    
    double total_tests = (double)(end_tests - start_tests) / (double)(CLOCKS_PER_SEC * loop_tests);
    
    fprintf( stdout, "--------------------------------\n");
    fprintf( stdout, "Red-Black Tree Size   : %d\n", num_items);
	fprintf( stdout, "Clocks Per Second     : %ld\n", CLOCKS_PER_SEC );
	fprintf( stdout, "Number of tests       : %d\n", num_tests);
    fprintf( stdout, "Clocks for all tests  : %ld\n", end_tests - start_tests );
    fprintf( stdout, "Average time per test : %.6lf us\n", total_tests / (double)num_tests * 1000000 );
    fprintf( stdout, "--------------------------------\n");

    
    return EXIT_SUCCESS;
}