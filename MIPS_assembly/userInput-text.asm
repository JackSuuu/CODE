.data 
	prompt: .asciiz "Enter your name:"
	message: .asciiz "Hello, "
	# variable to hold input
	userInput: .space 20
.text
	main:
		# Display prompt
		li $v0, 4
		la $a0, prompt
		syscall
	
		# Getting user's input as text
		li $v0, 8 # 8 means text
		la $a0, userInput # pass the variable to store user input
		li $a1, 20 # how much space need to utlize
		syscall
		
		li $v0, 4
		la $a0, message
		syscall 
		
		# Displays the name
		li $v0, 4
		la $a0, userInput
		syscall
	
	# Tell the system this is the end of main
	li $v0, 10
	syscall
		