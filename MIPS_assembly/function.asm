.data
	message: .asciiz "Hi, everyone.\nThis is Jack using MIPS\n"
.text
	main: # main program / procedure
		jal displayMessage # jump and link
		
		addi $s0, $zero, 5
		
		# print number 5 to the screen
		li $v0, 1
		add $a0, $zero, $s0
		syscall
	
	# Tell system the program is done. Halt the program
	li $v0, 10
	syscall
	
	displayMessage:
		li $v0, 4
		la $a0, message
		syscall
		
		jr $ra # go back to the place where it is called