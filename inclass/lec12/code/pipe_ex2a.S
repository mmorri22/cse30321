#pragma qtrvsim show registers
#pragma qtrvsim show memory

.globl _start
.option norelax

.text

_start:

	lw  x18, 40(x5)
	add x22, x18, x22
	lw  x19, 40(x6)
	or x23, x18, x19
	lw  x24, 40(x7)
	sub x22, x24, x23

	ebreak

.data