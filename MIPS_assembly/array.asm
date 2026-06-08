.data 
	myArray: .space 12
	newLine: .asciiz "\n"
.text
	main:
	addi $s0, $zero, 4
	addi $s1, $zero, 10
	addi $s2, $zero, 12
	
	# Index = $t0
	addi $t0, $zero, 0
	
	sw $s0, myArray($t0)
		addi $t0, $t0, 4 # increment the index
	sw $s1, myArray($t0) 
		addi $t0, $t0, 4
	sw $s2, myArray($t0)
	
	# increment the retrive index pos
	addi $t1, $zero, 4
	lw $t6, myArray($t1)
	
	# Clear $t0 as 0, note that addi is not add the value to the current number
	addi $t0, $zero, 0
	
	# Begin a while loop
	while:
		beq $t0, 12, exit  # becasue 3 elements * 4 bytes = 12
		
		lw $t6, myArray($t0)
		
		addi $t0, $t0, 4   # repeat the index
		
		# Print current number
		li $v0, 1
		move $a0, $t6
		syscall
		
		# Print a new line
		li $v0, 4
		la $a0, newLine
		syscall
		
		j while
	
	exit:
		# Tell system this is end of program
		li $v0, 10
		syscall
