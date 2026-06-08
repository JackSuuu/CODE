.data
	message: .asciiz "Enter the value of PI: "
	zeroFloat: .float 0.0
.text
	lwc1 $f0, zeroFloat
	
	# Display message
	li $v0, 4
	la $a0, message
	syscall
	
	# Read user input
	li $v0, 6 # 6 means float
	syscall
	
	# Display value
	li     $v0, 2
	add.s  $f12, $f0, $f4
	syscall
	
	