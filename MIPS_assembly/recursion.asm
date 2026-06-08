.data
	promptMessage: .asciiz "Enter a number to find its factorial: "
	resultMessage: .asciiz "\nThe factorial of the number is "
	theNumber: .word 0
	theAnswer: .word 0
.text
	.globl main
	main:
		# Read the number from the user
		li $v0, 4
		la $a0, promptMessage
		syscall
		
		# Take input
		li $v0, 5
		syscall
		
		sw $v0, theNumber
		
		# Call factorial()
		lw $a0, theNumber
		jal findFactorial
		sw $v0, theAnswer
		
		# Display the result
		li $v0, 4
		la $a0, resultMessage
		syscall
		
		li $v0, 1
		lw $a0, theAnswer
		syscall
		
		# Tell the OS that the end
		li $v0, 10
		syscall
		
	# =====================================================
	.globl findFactorial
	findFactorial:
		subu $sp, $sp, 8
		sw $ra, ($sp)
		sw $s0, 4($sp)  # store the next value into stack
		
		# Base case -> if $a0 = 0: backtrack
		li $v0, 1
		beq $a0, 0, factorialDone
		
		# Recursive step -> subtracting one from the argumemnt
		move $s0, $a0
		sub $a0, $a0, 1
		jal findFactorial
		
		# The magic happens here -> when return, this line execute
		mul $v0, $s0, $v0
		
		factorialDone:
			# load ra from stack: restore stack so ADD
			lw $ra, ($sp)
			lw $s0, 4($sp)
			addu $sp, $sp, 8
			jr $ra
		