.data

.text
	main:
		# "a" regesiter stands for argument
		addi $a1, $zero, 50
		addi $a2, $zero, 30
		
		jal addNumbers
		
		li $v0, 1
		addi $a0, $v1, 0  # v1 is the return value
		syscall
		
	
	# halt program
	li $v0, 10
	syscall
	
	addNumbers:
		add $v1, $a1, $a2
		
		jr $ra # jr for return values in procedure
