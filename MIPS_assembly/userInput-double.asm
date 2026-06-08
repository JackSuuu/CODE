.data
	message: .asciiz "Enter the value of e: "
.text
	# Display message
	li $v0, 4
	la $a0, message
	syscall
	
	# Get double from user
	li $v0, 7 # 7 means float
	syscall
	
	# Display user input
	li     $v0, 3
	add.d  $f12, $f0, $f10
	syscall
	
	