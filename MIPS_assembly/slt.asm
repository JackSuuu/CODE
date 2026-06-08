.data
	message: .asciiz "The number is less than the other\n"
.text
	addi $t0, $zero, 1
	addi $t1, $zero, 200
	
	# set less than == java.compareTo()
	# is 1 less than 200
	slt $s0, $t0, $t1
	bne $s0, $zero, printMessage
	
	# End process
	li $v0, 10
	syscall
	
	# label == function
	printMessage:
		li $v0, 4
		la $a0, message
		syscall
