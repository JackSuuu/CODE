.data

.text
	sort: 
		# saving registers
		addi $sp, $sp, -20
		sw $ra, 16($sp)
		sw $s3, 12($sp)
		sw $s1, 4($sp)
		sw $s0, 0($sp)
		
		# move parameters
		move $s2, $a0
		move $s3, $a1
		
		# outer loop
		move $s0, $zero
		for1st:
			slt $t0, $s0, $s3
			beq $t0, $zero, exit1
		# inner loop
			addi $s1, $s0, -1
		for2st:
			slti $t0, $s1, 0
			bne $t0, $zero, exit2
			sll $t1, $s1, 2
			add $t2, $s2, $t1
			lw  $t3, 0($t2)
			lw $t4, 4($t2)
			slt $t0, $t4, $t3
			beq $t0, $zero, exit2
			
			move $a0, $s2
			move $a1, $s1  # swap parameter
			jal swap
			
			addi $s1, $s1, -1
			j for2st
		
		exit2: 
			addi $s0, $s0, 1
			j for1st
		
		# Restoring registers
		exit1:
			lw $s0, 0($sp)
			lw $s1, 4($sp)
			lw $s2, 8($sp)
			lw $s3, 12($sp)
			lw $ra, 16($sp)
			addi $sp, $sp, 20
			
		# procedure return
		jr $ra
			 