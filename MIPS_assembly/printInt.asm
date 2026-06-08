.data
	age: .word 23
.text
	li $v0, 1 # 1 telling system we are print integer
	lw $a0, age
	syscall