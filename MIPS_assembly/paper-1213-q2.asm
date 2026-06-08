.data

.text

li $t0, 2
li $t1, 1
li $t2, 2
li $t3, 4

loop: 
	beq $t0, $zero, end
	add $t3,$t1,$t2
	add $t2,$zero,$t3
	srl $t0,$t0,2 # shift right logical
	j loop
end:
	# Prepare for syscall to print the value of $t2
    move $a0, $t2        # Move the value of $t2 into $a0 for printing
    li $v0, 1            # Load syscall code 1 (print integer)
    syscall              # Make the syscall to print the value of $t2

    # Exit the program
    li $v0, 10           # Load syscall code 10 (exit)
    syscall              # Make the syscall to exit the program