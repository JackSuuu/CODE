.data
	newLine: .asciiz "\n"
.text
	main:
		addi $s0, $zero 10
		
		jal increaseMyRegesiter
		
		# Print a new line
		li $v0, 4
		la $a0, newLine
		syscall
		
		# Print value
		li $v0, 1
		move $a0, $s0
		syscall
	
	# signal end of program
	li $v0, 10
	syscall
	
	increaseMyRegesiter:
		# "sp" stands for stack pointer
		addi $sp, $sp, -4
			# 0() 's 0 is offset
		sw   $s0, 0($sp)  # save it to the stack to store old val
		
		addi $s0, $s0, 30 # add val to the regesiter
		
		# Print new val in function
		li $v0, 1
		move $a0, $s0
		syscall
		
		# restore the value back
		lw $s0, 0($sp)
		addi $sp, $sp, 4
		
		jr $ra
		
		