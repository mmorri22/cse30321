#pragma qtrvsim show registers
#pragma qtrvsim show memory

.globl _start
.option norelax

.text

_start:

	lui x5, 0x7ffff
	addi x20, x5, 0x3a0
	lw  x18, 40(x20)
	add x19, x18, x20
	sub x22, x19, x21
	sw x22, 20(x20)

	ebreak

.data