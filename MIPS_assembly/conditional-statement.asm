.data 
	message: .asciiz "The numbers are equal."
	message2: .asciiz "The numbers are not equal."
.text
	main:
		addi $t0, $zero, 5
		addi $t1, $zero, 10
		
		# branch if equal op1, op2, label
		beq $t0, $t1, numbersEqual
		
		# branch if not equal
		bne $t0, $t1, numbersDifferent
	
		# syscall to end program
		li $v0, 10
		syscall
	
	numbersEqual:
		li $v0, 4
		# The la instruction is used to load the address of a label
		la $a0, message
		syscall
	
	numbersDifferent:
		li $v0, 4
		la $a0, message2
		syscall