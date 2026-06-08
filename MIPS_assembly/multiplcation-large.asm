# Multiplication - large
.data

.text
	addi $t0, $zero, 1000
	addi $t1, $zero, 10
	
	mult  $t0, $t1
	
	mflo  $s0
	
	# Display the product
	li $v0, 1
	add $a0, $zero, $s0
	syscall