/**************************************
 * File Name: top_down_splay.c
 * Author: Primary - Daniel Sleator, March 1992
 *         Modifier - Matthew Morrison, February 2023
 * 
 * This code is part of the public domain
 *
  "Splay trees", or "self-adjusting search trees" are a simple and
  efficient data structure for storing an ordered set.  The data
  structure consists of a binary tree, without parent pointers, and no
  additional fields.  It allows searching, insertion, deletion,
  deletemin, deletemax, splitting, joining, and many other operations,
  all with amortized logarithmic performance.  Since the trees adapt to
  the sequence of requests, their performance on real access patterns is
  typically even better.  Splay trees are described in a number of texts
  and papers [1,2,3,4,5].

  The code here is adapted from simple top-down splay, at the bottom of
  page 669 of [3].  The chief modification here is that the splay operation works even if the
  item being splayed is not in the tree, and even if the tree root of the
  tree is NULL.  

  So the line:

                              t = splay(i, t);

  causes it to search for item with key i in the tree rooted at t.  If it's
  there, it is splayed to the root.  If it isn't there, then the node put
  at the root is the last one before NULL that would have been reached in a
  normal binary search for i.  (It's a neighbor of i in the tree.)  This
  allows many other operations to be easily implemented, as shown below.

  [1] "Fundamentals of data structures in C", Horowitz, Sahni,
       and Anderson-Freed, Computer Science Press, pp 542-547.
  [2] "Data Structures and Their Algorithms", Lewis and Denenberg,
       Harper Collins, 1991, pp 243-251.
  [3] "Self-adjusting Binary Search Trees" Sleator and Tarjan,
       JACM Volume 32, No 3, July 1985, pp 652-686.
  [4] "Data Structure and Algorithm Analysis", Mark Weiss,
       Benjamin Cummins, 1992, pp 119-130.
  [5] "Data Structures, Algorithms, and Performance", Derick Wood,
       Addison-Wesley, 1993, pp 367-375.

*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct Tree {
    struct Tree* left;
    struct Tree* right;
    int item;
}Tree;

Tree* splay(int insert_val, Tree* t) {

    /* Simple top down splay, not requiring i to be in the tree t.  */
    /* What it does is described above.                             */
    Tree N, *l, *r, *y;

    if (t == NULL) 
        return t;

    N.left = N.right = NULL;
    l = r = &N;

    while(1) {

        if (insert_val < t->item) {

            if (t->left == NULL) 
                break;

            if (insert_val < t->left->item) {
                y = t->left;                           /* rotate right */
                t->left = y->right;
                y->right = t;
                t = y;
                if (t->left == NULL) 
                    break;
            }
            
            r->left = t;                               /* link right */
            r = t;
            t = t->left;
        } 
        else if (insert_val > t->item) {

            if (t->right == NULL) 
                break;

            if (insert_val > t->right->item) {
                y = t->right;                          /* rotate left */
                t->right = y->left;
                y->left = t;
                t = y;

                if (t->right == NULL) 
                    break;
            }

            /* Link Left */
            l->right = t;
            l = t;
            t = t->right;
        } 
        else {
            // We found the item
            break;
        }
    }

    /* Assemble the new Splay tree */
    l->right = t->left;
    r->left = t->right;
    t->left = N.right;
    t->right = N.left;

    return t;
}

/* Matt, here is how bob sedgewick would have written this.          */
/* It does the same thing.                                           */
Tree* sedgewickized_splay(int i, Tree* t) {
    Tree N, *l, *r, *y;
    if (t == NULL) return t;
    N.left = N.right = NULL;
    l = r = &N;

    for (;;) {
	if (i < t->item) {
	    if (t->left != NULL && i < t->left->item) {
		y = t->left; t->left = y->right; y->right = t; t = y;
	    }
	    if (t->left == NULL) break;
	    r->left = t; r = t; t = t->left;
	} else if (i > t->item) {
	    if (t->right != NULL && i > t->right->item) {
		y = t->right; t->right = y->left; y->left = t; t = y;
	    }
	    if (t->right == NULL) break;
	    l->right = t; l = t; t = t->right;
	} else break;
    }
    l->right=t->left; r->left=t->right; t->left=N.right; t->right=N.left;
    return t;
}

Tree* insert(int insert_val, Tree* t) {

    /* Insert insert_val into the tree t, unless it's already there.    */
    /* Return a pointer to the resulting tree.                 */

    Tree* new = (Tree*) calloc (1, sizeof (Tree));
    if (new == NULL) {
        fprintf(stdout, "Ran out of space\n");
        exit(1);
    }

    new->item = insert_val;
    if (t == NULL) {
        new->left = new->right = NULL;
        return new;
    }

    t = splay(insert_val,t);

    if (insert_val < t->item) {
        new->left = t->left;
        new->right = t;
        t->left = NULL;
        return new;
    } 
    else if (insert_val > t->item) {
        new->right = t->right;
        new->left = t;
        t->right = NULL;
        return new;
    } 
    
    else { /* We get here if it's already in the Tree*/
             /* Don't add it again                      */
        free(new);
        return t;
    }
}

Tree* delete(int delete_val, Tree* t) {
/* Deletes i from the tree if it's there.               */
/* Return a pointer to the resulting tree.              */
    Tree* x;

    /* Dr. Morrison's Golden Rule of Pointers */
    if (t==NULL) 
        return NULL;

    /* Splay the element to the top of the tree */
    t = splay(delete_val,t);

    /* Item was found and splayed to the top of the tree */
    if (delete_val == t->item) {     
                  
        if (t->left == NULL) {
            x = t->right;
        } 

        else {
            x = splay(delete_val, t->left);
            x->right = t->right;
        }

        free(t);
        return x;
    }

    /* delete_val wasn't found */
    return t;
}

int main( const int argc, const char* argv[] ) {
/* A sample use of these functions.  Start with the empty tree,         */
/* insert some stuff into it, and then delete it                        */

    if( argc != 3 ){
        fprintf(stdout, "Error: ./dllist_timed [num_items] [num_tests]");
        return EXIT_FAILURE;
    }

    int num_items = atoi(argv[1]);
    int num_tests = atoi(argv[2]);

    /* Design an empty tree */
    Tree* root = NULL;

    // Call push_front with as many as we want to insert
    clock_t start_inserts = clock();
    int iter;
    for( iter = 0; iter < num_items; ++iter ){
        
        int the_value = rand() % num_items;
        
        root = insert( the_value , root);
        
    }

    clock_t end_inserts = clock();

    double total_inserts = (double)(end_inserts - start_inserts) / (double)(CLOCKS_PER_SEC);

    clock_t start_tests = clock();

    int loop_tests = 0;
    for(loop_tests = 0; loop_tests < 100; ++loop_tests){

        int i;
        for (i = 0; i < num_tests; ++i) {

            int delete_num = rand() % num_items;
            root = delete( delete_num, root);

            int insert_num  = rand() % num_items;
            root = insert( insert_num, root);
        }
    
    }

    clock_t end_tests = clock();
    
    double total_tests = (double)(end_tests - start_tests) / (double)(CLOCKS_PER_SEC * loop_tests);
    
    fprintf( stdout, "--------------------------------\n");
    fprintf( stdout, "Splay Tree Size        : %d\n", num_items);
    fprintf( stdout, "Clocks Per Second      : %ld\n", CLOCKS_PER_SEC );
    fprintf( stdout, "Clocks for all inserts : %ld\n", end_inserts - start_inserts);
    fprintf( stdout, "Average time per insert: %.6lf us\n", total_inserts / (double)num_tests * 1000000 );
    fprintf( stdout, "Number of tests        : %d\n", num_tests);
    fprintf( stdout, "Clocks for all tests   : %ld\n", end_tests - start_tests );
    fprintf( stdout, "Average time per tests : %.6lf us\n", total_tests / (double)num_tests * 1000000 );
    fprintf( stdout, "--------------------------------\n");


    return EXIT_SUCCESS;

}