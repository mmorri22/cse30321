// File Name: hw06_arr.S
// Author: Aaron Dingler (modified by Matthew Morrison 3/7/24)
//  based on simple-lw-sw-ia.S, (C) 2021 by Pavel Pisa
//      e-mail:   pisa@cmp.felk.cvut.cz
//      homepage: http://cmp.felk.cvut.cz/~pisa
//      work:     http://www.pikron.com/
//      license:  public domain

// File Name: hw06_arr.S
// Author: Aaron Dingler (modified by Matthew Morrison 3/7/24)

#pragma qtrvsim show registers
#pragma qtrvsim show memory

.globl _start
.option norelax

.text

_start:

	la x5, arr		// Pseudo instruction used to indicate the starting address of array
	la x6, arr_size	// Pseudo instruction used to indicate the array size
	lw x6, 0(x6)

	li x7, 0		//loop index, i = 0

	li x8, 10		//we will fill a large array with values starting at 10

fill_loop:
	bge x7, x6, done_fill
	slli x9, x7, 2	//i * 4
	add x9, x9, x5	//&(arr + i * 4)
	sw x8, 0(x9)	//arr[i] = 10
	addi x7, x7, 1
	addi x8, x8, 1
	j fill_loop
done_fill:

	li x8, 0		//total
	li x7, 0		//i = 0
	//ebreak
sum_loop:	
	bge x7, x6, done_sum
	slli x9, x7, 2	//i * 4
	add x9, x9, x5	//&(arr + i * 4)
	lw x10, 0(x9)	//x8 = arr[i]
	add x8, x8, x10
	addi x7, x7, 1
	j sum_loop
done_sum:
	ebreak

.data
.org 0x400

arr_size:
	.word 1024
arr:
	.word  1

#pragma qtrvsim focus memory arr