.data
	message: .asciiz "After while loop is done"
	newLine: .asciiz "\n"
.text
	main: 
		addi $t0, $zero, 0  # i = 0
		
		while:
			bgt $t0, 10, exit
			jal printNumber
			addi $t0, $t0, 1  # i++
			
			# jump back to the begin of while loop
			j while
		
		exit:
			li $v0, 4
			la $a0, message
			syscall
			
		# End program
    	li $v0, 10
    	syscall 
    	
    printNumber:
    	# Print the counter value
    	li $v0, 1          # Set $v0 to 1 for syscall print_int
    	add $a0, $t0, $zero      # Add the counter value into $a0
    	syscall
    	
    	li $v0, 4
    	la $a0, newLine
    	syscall
    	
    	jr $ra
    	
    	