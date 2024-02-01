lui x5, 0x051a0
lui x6, 0x61100
srli x6, x6, 16
or x18, x5, x6    # x18 contains sllist* the_list at 0x051a6110
sw x0, 0(x18)     # Put NULL at 0x051a6110 - CALLOC!
addi x19, x0, 1   # x19 (x) = 0
addi x5, x19, -5   # x5 = x - 5
blt x0, x5, 4      # Currently branch 1 instruction, will be much more
lw x7, 0(x18)      # Load the address pointed to by x18 into x7
add x6, x18, x0    # x6 and x18 pointing to most recent alloc
addi x6, x6, 12    # Point (96/12)*3 blocks down
sw x19, 0(x6)      # Store x at the base node value
sw x0, 4(x6)       # Set next node to NULL (0)
sw x6, 0(x18)      # Update head node
add x6, x0, x0     # Free x6 pointer on every loop
addi x19, x19, 1   # ++x;
beq x19, x19, -40  # Branch back to addi x5, x19, -5 (17-7)*4 - Update line 8 to 84 to get to the end!