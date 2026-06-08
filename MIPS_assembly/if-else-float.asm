.data
	message: .asciiz "It was true\n"
	message2: .asciiz "It was false\n"
	number1: .float 10.4
	number2: .float 10.4
.text
	main:
		lwc1 $f0, number1
		lwc1 $f1, number2
		
		c.eq.s $f0, $f1
		
		bc1t exit
		
		li $v0, 4
		la $a0, message2
		syscall
	
	# End program: like return 0 in C++
	li $v0, 10
	syscall
	
	exit:
		li $v0, 4
		la $a0, message
		syscall
