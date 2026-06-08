# Multiplication
.data

.text
	# $zero is a read-only regesiter
	# $s0-s7 are saved regesiter
	addi $s0, $zero, 10 # add 10 to regeister s0
	addi  $s1, $zero, 4  # add 4 to regesiter s1
	
	# t0 is temporary regesiter
	mul  $t0, $s0, $s1
	
	# Display the product
	li $v0, 1 # v0 is used to specify system call, 1 is data type
	add $a0, $zero, $t0 # a0, a1, a2 are for system call
	syscall